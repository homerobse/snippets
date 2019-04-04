# virtualenv 

## create virtualenv
$ virtualenv -p python3 envname

or using conda and creating with some pre-installed pkgs

$ conda create --name envname pkg1 pkg2 

## activate
$ source envname/bin/activate

with conda:
$ conda activate <env-name>

## deactivate
$ deactivate

with conda:
$ conda deactivate <env-name>

## install all requirements
pip install -r requirements.txt

## remove

$ conda env remove -n ENV_NAME

## Enable jupyter-notebook with a specific environment 
### https://stackoverflow.com/a/44786736/1273751

$ conda activate myenv
$ conda install ipykernel
$ python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

# Python

## Get the index of elements in an array with value 15

    arr = np.array([15,1,15,20])
    result = np.where(arr == 15)

## String format

    x = 10
    print(f'I have {x} pets')
