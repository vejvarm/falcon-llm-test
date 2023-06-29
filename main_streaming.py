import argparse
import os
import pathlib

from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer

# os.environ["RWKV_CUDA_ON"] = "1"


def generate_config(model_path, tokenizer):
    config = GenerationConfig.from_pretrained(model_path, trust_remote_code=True)

    config.max_new_tokens = 100
    config.penalty_alpha = 0
    config.top_k = 10
    config.num_beams = 1
    config.temperature = 0.0
    config.num_return_sequences = 1

    config.pad_token_id = tokenizer.pad_token_id
    config.eos_token_id = tokenizer.eos_token_id
    config.save_pretrained("./configs")


def main(args):
    model_path = args.model
    path_to_prompt = pathlib.Path(args.prompt_file)

    if path_to_prompt.exists():
        prompt = path_to_prompt.open().read()
    else:
        raise FileNotFoundError(f"No file found at given 'prompt-file' path ({path_to_prompt})")

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, load_in_8bit=True, trust_remote_code=True)  # TODO: add args for 8bit/4bit quantizations
    streamer = TextStreamer(tokenizer, skip_prompt=args.skip_prompt)

    # generate_config(model_path, tokenizer)
    config = GenerationConfig.from_pretrained(args.config_folder)

    inputs = tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to('cuda')  # https://huggingface.co/tiiuae/falcon-40b/discussions/7

    output_ids = model.generate(**inputs, streamer=streamer, generation_config=config)
    # print(tokenizer.batch_decode(output_ids, skip_special_tokens=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-file", type=str, default="inputs/example-0.prompt", help="path to .prompt file")
    parser.add_argument("--model", type=str, default="tiiuae/falcon-7b-instruct", help="HF model name/local path")
    parser.add_argument("--config-folder", type=str, default="configs/default", help="path to config folder")
    parser.add_argument("--skip-prompt", action='store_true', help="Skip printing the input prompt.")

    args = parser.parse_args()
    main(args)
