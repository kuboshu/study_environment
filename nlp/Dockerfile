FROM jupyter/base-notebook:python-3.8.8

ARG NB_USER="jovyan"

USER root
RUN apt-get update && apt-get -y upgrade && pip install --upgrade pip
RUN apt-get install -y mecab libmecab-dev mecab-ipadic gcc g++

USER ${NB_USER}
RUN pip install mecab-python3 unidic-lite scikit-learn pandas keras tensorflow neologdn
RUN pip install PyPDF2 pdfminer.six

