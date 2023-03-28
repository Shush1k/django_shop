FROM python:3.9
ADD requirements.txt /app/requirements.txt
ADD ./myshop/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A myshop worker --concurrency=20 --loglevel=info