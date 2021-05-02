FROM python:alpine as base

FROM base as build
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM base
COPY --from=build /root/.local /root/.local
ADD *.py ./
ADD templates/ ./templates/
ENTRYPOINT ["gunicorn"]
CMD ["app:app","-b",":8080","--capture-output"]