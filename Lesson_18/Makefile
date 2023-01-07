start:
	python -m venv .venv
	.venv\Scripts\activate
	python -m pip install --upgrade pip
	pip install –r requirements.txt


lint: #start
	pip freeze > requirements.txt
	black .
	isort .

