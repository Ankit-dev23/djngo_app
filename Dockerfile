FROM python:3.9.23

WORKDIR /app

COPY . .

RUN pip install -r requirment.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



