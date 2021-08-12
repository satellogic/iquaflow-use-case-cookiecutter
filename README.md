# Cookiecutter for AI projects

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

### To start a new project, run:
------------
	git clone https://gitlab+deploy-token-37:TyK24S-Dfso92GHnUds2@publicgitlab.satellogic.com/iqf/use-cases/cookiecutter-iqf-use-case.git
	cookiecutter cookiecutter-iqf-use-case 

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
