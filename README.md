conda create -n env_name python=3.7 -y
conda activate env_name
source activate env_name
pip install dvc
git init
dvc init
dvc repro
dvc dag