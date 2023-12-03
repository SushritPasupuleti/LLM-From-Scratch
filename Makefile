help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  requirements_freeze to freeze the requirements"
	@echo "  requirements_install to install the requirements"
	@echo "  venv_create         to create the virtual environment"
	@echo "  venv_activate       to activate the virtual environment"

requirements_freeze:
	pip freeze > requirements.txt

requirements_install:
	pip install -r requirements.txt

venv_create:
	python3 -m venv .venv

venv_activate:
	source .venv/bin/activate

nix-shell:
	nix-shell ./shell.nix

notebook:
	jupyter notebook
