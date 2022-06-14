FROM python:3.9.6
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/tsahli/volcano-insurance.git /volcano_insurance

WORKDIR /volcano-insurance

ADD . /volcano-insurance/

RUN pip install -r requirements.txt

VOLUME /volcano-insurance

EXPOSE 8080

CMD python ./volcano_insurance/manage.py makemigrations && python ./volcano_insurance/manage.py migrate && python ./volcano_insurance/manage.py runserver 0.0.0.0:8000