FROM python:3.7-alpine
LABEL maintainer="Amir Ayub, dev.amirayub@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "./core.py" ]