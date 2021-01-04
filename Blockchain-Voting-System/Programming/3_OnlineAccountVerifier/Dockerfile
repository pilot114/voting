##################################################
# 
# Dockerfile to build the Application Server
#
##################################################

FROM ubuntu:focal

# Do not buffer the output from stdout.
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Set the working directory.
WORKDIR /usr/src/onlineaccountverifier/

# Copy our python server over.
COPY . /usr/src/onlineaccountverifier/

# Install our dependencies
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        libpq-dev \
        libffi-dev \
        libssl-dev \
        libyaml-dev \
        postgresql-12

# Install our server via pip
RUN pip3 install .

# Expose our ports
EXPOSE 5435

# Run load our entrypoint
ENTRYPOINT [ "./bin/docker_entrypoint" ]
