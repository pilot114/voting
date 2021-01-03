##################################################
# 
# Dockerfile to build the Application Server
#
##################################################

# Set the base image to ubuntu
FROM ubuntu:focal

# Do not buffer the output from stdout.
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Set the working directory.
WORKDIR /usr/src/onlineballotregulator/

# Copy our python server over.
COPY . /usr/src/onlineballotregulator/

RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        software-properties-common

RUN add-apt-repository -y ppa:ethereum/ethereum

# Install our dependencies
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    libyaml-dev \
    golang \
    git \
    make \
    gcc \
    libc-dev \
    ca-certificates

RUN apt-get install -y postgresql-12 wget

RUN apt-get install -y ethereum solc
#    ethereum-1.9.25 \
#    solc-0.4.24

#RUN git clone --depth 1 https://github.com/ethereum/go-ethereum /usr/src/onlineballotregulator/go-ethereum

# Install our server via pip
RUN pip3 install .
RUN python3 -m solc.install v0.4.24 && mv ~/.py-solc/solc-v0.4.24/bin/solc /usr/bin

# Expose our ports
EXPOSE 5434 8545 30303

# Run load our entrypoint
ENTRYPOINT [ "./bin/docker_entrypoint" ]
