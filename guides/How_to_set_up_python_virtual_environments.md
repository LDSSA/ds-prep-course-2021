# How to set up python virtual environments

## Initial Setup for Ubuntu: _pip_ and _venv_

If you have a Mac, you don't need to do this part.
```console
mig@ubuntu$ sudo apt update && sudo apt upgrade && sudo apt install python3-pip python3-venv
```

## Setup for both Mac and Ubuntu

### Install _pip_

_pip_ is the reference Python package manager. It’s used to install and update packages. You’ll need to make sure you have the latest version of pip installed.

To install _pip_, type the following on your terminal:
```console
mig@MacBook-Pro$ python3 -m pip install --user --upgrade pip setuptools wheel
```

Afterwards, you should have the newest pip installed:
```console
mig@MacBook-Pro$ python3 -m pip --version
pip 20.0.2 from /Users/mig/Library/Python/3.7/lib/python/site-packages/pip (python 3.7)
```

### Set up a virtual environment

_venv_ is a Python Standard Library module that allows us to create isolated Python environments (called virtual environments).  
We'll use it to keep an isolated Python environment where we will install the specific python packages we use in the Learning Units.  
You should always be using a virtual environment to install python packages (such as jupyter notebook, pandas, numpy, etc) and should never install packages outside of a virtual environment. This is because Linux based Operating Systems (OS) use python as a part of their system, and installing python packages onto the OS's python may leave the OS in an inconsistent state.   

We'll be storing all our virtual environments in the `~/.virtualenvs` folder.  
The following command will create a virtual environment called `prep-venv`, which will be stored inside the `~/.virtualenvs/`.  
To create a virtual environment called `prep-venv` (you may use whatever name you like), type:
```console
mig@MacBook-Pro$ python3 -m venv ~/.virtualenvs/prep-venv
```

We will now activate our virtual environment (in order to install and use the specific libraries we want for the prep course) by typing the command below.
Notice that once we do, on the leftmost side of the command line, the name of our virtual environment appears in parenthesis.  
```console
mig@MacBook-Pro$ source ~/.virtualenvs/prep-venv/bin/activate
(prep-venv) mig@MacBook-Pro$
```

By using the `which` command, we can see that after we activate our virtual environment, we start using a different python installation, and are now safe to start installing python packages to it.
```console
mig@MacBook-Pro$ which python3
/usr/bin/python3
mig@MacBook-Pro$ source ~/.virtualenvs/prep-venv/bin/activate
(prep-venv) mig@MacBook-Pro$ which python
source ~/.virtualenvs/prep-venv/bin/activate/prep-venv/bin/python
```

The first thing we will do at this point is upgrade our virtual environment's version of pip:
```bash
pip install -U pip
```

Notice that because we used the default python3 to create our virtual environment, when we have the virtual environment active, we can refer to python3 as just python, and to pip3 as just pip.



We can also deactivate our virtual environment (note that deactivating a virtual environment **does not** remove it) by typing the command below.  
By doing this, we stop working in our isolated Python environment.
Notice that once we do, on the leftmost side of the command line, the name of our virtual environment disappears:
```console
(prep-venv) mig@MacBook-Pro$ deactivate
mig@MacBook-Pro$
```

Using the `ls` command, followed by the directory where we store our virtual environments (`~/.virtualenvs`) we can see which virtual environments we have created:
```console
(prep-venv) mig@MacBook-Pro$ ls ~/.virtualenvs
prep-venv
```

To remove a virtual environment, we need to deactivate it and remove the folder it's stored in.
To do this we use the `rm` command with the `-r` flag and the location of the virtual environment we want to remove (note that if you remove a virtual environment, you can create it again, so we encourage you to try it out):
```console
(prep-venv) mig@MacBook-Pro$ deactivate
mig@MacBook-Pro$ rm -r ~/.virtualenvs/prep-venv
```

### Installing python packages using _pip_

For installing python packages, make sure you have your virtual environment active:
```console
mig@MacBook-Pro$ source ~/.virtualenvs/prep-venv/bin/activate
(prep-venv) mig@MacBook-Pro$ 
```

To install one package, simply type `pip install` followed by the name of the package:
```console
mig@MacBook-Pro$ source ~/.virtualenvs/prep-venv/bin/activate
(prep-venv) mig@MacBook-Pro$ pip install numpy
```

To install multiple python packages in one go, type `pip install` followed by the name of the python packages, separated by a single space:
```console
mig@MacBook-Pro$ source ~/.virtualenvs/prep-venv/bin/activate
(prep-venv) mig@MacBook-Pro$ pip install matplotib pandas
```

In each Learning Unit, you be provided with a `requirements.txt` file that will contain a list with all the python packages you need to install for a particular project. 
To install python packages from a `requirements.txt` file, type `pip install` followed by the `-r` flag and `requirements.txt`:
```console
(prep-venv) mig@MacBook-Pro$ pip install -r requirements.txt
```

## References

* https://packaging.python.org/guides/installing-using-linux-tools/
* https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
* https://docs.python.org/3/library/venv.html
* https://packaging.python.org/tutorials/installing-packages/#id12