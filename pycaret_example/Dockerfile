FROM python:3.8-buster as builder

RUN pip install --upgrade pip setuptools \
  && pip install matplotlib pandas pycaret

FROM python:3.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

RUN pip install --upgrade pip setuptools \
  && pip install jupyterlab

ENTRYPOINT [ "jupyter-lab" ]
CMD [ "--no-browser", "--allow-root", "--ip=0.0.0.0", "--port=8886", "--notebook-dir=/opt", "--NotebookApp.token=''" ]
