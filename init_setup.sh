echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.8 venv"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activating the enviroment"

source activate ./env

echo [$(date)]: "installing the dev requriments"

pip install -r requirements.txt

echo [$(date)]: "END"