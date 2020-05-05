FROM jupyter/scipy-notebook

USER root

RUN apt-get update
RUN apt-get install -y libcurl3-gnutls gnupg2
RUN apt-get install -y curl
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y yarn
RUN yarn global add deepl-translator-cli
ENV PATH $PATH:~/.yarn/bin
