Setup
---
## Prerequisites:
Requires Anaconda or Miniconda installed ([guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)).

## Installation:
In conda-enabled terminal:
``` bash
git clone https://github.com/vejvarm/falcon-llm-test.git
cd ./falcon-llm-test
conda create --prefix ./env --file requirements-conda.txt
conda activate ./env
pip install -r requirements.txt
```
([conda reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment))

Test run:
---
``` bash
python main_streaming.py
```