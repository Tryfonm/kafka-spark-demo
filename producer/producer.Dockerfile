FROM ubuntu:20.04

RUN apt update && apt upgrade -y
RUN apt install screen iproute2 nano iputils-ping make wget -y
RUN apt install python3-pip -y

WORKDIR /workdir

COPY producer_script.py requirements.txt ./

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "producer_script.py" ]
