start:
	sudo docker build -t volcano-insurance ../ ;
	docker run -d -p 8080:8000 -v src:/volcano-insurance --name volcano-insurance volcano-insurance

test:
	python manage.py test

migrate-all:
	python ./volcano_insurance/manage.py makemigrations rest_api ;
	python ./volcano_insurance/manage.py migrate rest_api

format:
	black .