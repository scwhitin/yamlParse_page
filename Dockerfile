FROM python:alpine as base

FROM base as build
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD *.py ./
ADD templates/ ./templates/
ENTRYPOINT ["gunicorn"]
CMD ["app:app","-b",":8080","--capture-output"]