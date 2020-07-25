FROM python:3.8-buster

RUN pip install --upgrade pip setuptools \
  && pip install matplotlib jupyter pandas pycaret

CMD ["jupyter", "notebook", "--allow-root"]
