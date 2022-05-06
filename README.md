# Cookiecutter for IQF use cases

## To start a new project, run:
------------
``` bash
cookiecutter git@github.com:satellogic/iquaflow-use-case-cookiecutter.git
``` 

or

``` bash
git clone git@github.com:satellogic/iquaflow-use-case-cookiecutter.git
cookiecutter iquaflow-use-case-cookiecutter
``` 

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```
### Installing development requirements
------------
``` bash
pip install -r requirements.txt
```
### Running the tests
------------
``` bash
py.test tests
```