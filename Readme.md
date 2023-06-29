Setup
---
## Prerequisites:
Requires Anaconda or Miniconda installed ([guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)).

## Installation:
### Create environment and install packages:
``` bash
git clone https://github.com/vejvarm/falcon-llm-test.git
cd ./falcon-llm-test
conda create -p ./env python=3.10 -y
conda activate ./env
conda install cudatoolkit
pip install -r requirements.txt
```
([conda reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment))

### Add CUDA libraries to path:
on Linux:
``` bash
export LD_LIBRARY_PATH=./env/lib:$LD_LIBRARY_PATH
```
on Windows:
``` cmd
set LD_LIBRARY_PATH=.\env\lib;%LD_LIBRARY_PATH%
```


Test run:
---
``` bash
python main_streaming.py
```