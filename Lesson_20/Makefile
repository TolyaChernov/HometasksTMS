start:
	python -m venv .venv
	.venv\Scripts\activate
	python -m pip install --upgrade pip
	pip install –r requirements.txt


lint: #start
	pip freeze > requirements.txt
	black .
	isort .
	autopep8 ./ --recursive --in-place -a
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./
	python app.py

djang:
	pip install django
	django-admin startproject mysite
	cd mysite
	python manage.py startapp music
	python manage.py makemigrations
	python manage.py migrate
