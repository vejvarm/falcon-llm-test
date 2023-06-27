Setup
---
``` bash
git clone falcon-llm-test
cd ./falcon-llm-test
conda create --prefix ./env --file requirements-conda.txt
conda activate ./env
pip install -r requirements.txt
```

[conda reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment)


Run
---
``` bash
python main_streaming.py
```