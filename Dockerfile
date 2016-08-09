FROM ubuntu:latest
MAINTAINER Hemant Kumar <hemant.kumar3@hpe.com>


ENV http_proxy=http://web-proxy.cup.hp.com:8080
ENV https_proxy=https://web-proxy.cup.hp.com:8080

RUN apt-get update && apt-get -y install \
        git

RUN git clone https://github.com/gseteam/dashboard_app.git
