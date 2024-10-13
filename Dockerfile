FROM ubuntu:20.04

RUN mkdir -p /_build/
WORKDIR /_build/
ADD . /_build/

ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install packages and build the environment
# NOTE:
# - A non-priv user named `oscar` will be created with home dir at `/srv/oscar`
# - tmux trigger is `CTRL+t`
RUN apt-get update && apt-get install -y \
       build-essential \
       python3-dev \
       python3-pip \
       openssh-server \
       tmux \
       htop \
       sudo
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN pip3 install -U pip
RUN make initialize_env
RUN chown bayc: -R /srv/bayc
RUN mkdir /var/run/sshd

# Clean up
RUN apt-get autoclean
RUN apt-get autoremove
RUN apt-get purge
RUN rm -Rf /_build/