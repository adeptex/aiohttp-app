FROM ubuntu:latest

ENV SERVICE_HOME /opt/service

RUN apt update
RUN apt -y install python3 python3-pip python3-yaml

ADD . ${SERVICE_HOME}
WORKDIR ${SERVICE_HOME}

RUN pip3 install -r requirements.txt
RUN apt autoremove

RUN useradd -m -d ${SERVICE_HOME} -s /bin/bash app
RUN chown -R app:app ${SERVICE_HOME}

USER app

CMD ["make", "run"]