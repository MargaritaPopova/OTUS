FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ADD . /app/

# pipenv istallation

RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv lock --requirements > requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

#EXPOSE 8000
#CMD ["python", "expences/manage.py", "runserver"]