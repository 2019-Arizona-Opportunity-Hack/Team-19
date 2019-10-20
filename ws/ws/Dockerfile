FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 80:80
EXPOSE 80:5555
ENTRYPOINT [ "python" ]

CMD [ "runserver.py" ]
