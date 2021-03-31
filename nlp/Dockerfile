FROM jupyter/base-notebook:python-3.8.8

ARG NB_USER="jovyan"

USER root
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y mecab libmecab-dev mecab-ipadic && \
    pip install mecab-python3 unidic-lite scikit-learn

USER ${NB_USER}