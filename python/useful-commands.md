# conda and virtualenv 

## create virtualenv
`$ virtualenv -p python3 envname`

or using conda and creating with some pre-installed pkgs

`$ conda create --name envname pkg1 pkg2 `

## activate
`$ source envname/bin/activate`

with conda:
`$ conda activate <env-name>`

## deactivate
`$ deactivate`

with conda:
`$ conda deactivate <env-name>`

## install all requirements
`pip install -r requirements.txt`

with conda:
`conda install --file requirements.txt`

## remove environment

`$ conda env remove -n ENV_NAME`

## Enable jupyter-notebook with a specific environment 
https://stackoverflow.com/a/44786736/1273751

    $ conda activate myenv
    $ conda install ipykernel
    $ python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

## Install package using a specific channel

Search channel at https://anaconda.org/, then run:

`conda install -c <channel> <package>`

# Jupyter notebook

## use remote notebook https://amber-md.github.io/pytraj/latest/tutorials/remote_jupyter_notebook

run on the remote server
`jupyter-notebook --no-browser --port=8889`
then locally:
`ssh -N -f -L localhost:8888:localhost:8889 username@your_remote_host_name`

Or choose another local port instead of 8888. Eg. 9000 also works.

Then copy the token in the field in the local browser.

---

-f: Requests ssh to go to background just before command execution

-N Do not execute a remote command.  This is useful for just forwarding ports.

-L local_socket:remote_socket

Option -L: Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side.

---

# Python

## Get the index of elements in an array with value 15

    arr = np.array([15,1,15,20])
    result = np.where(arr == 15)

## String format

    x = 10
    print(f'I have {x} pets')
