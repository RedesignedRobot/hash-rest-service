FROM ubuntu:latest
LABEL maintainer="Amir Ayub, dev.amirayub@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "./core.py" ]