FROM python:3.7

COPY ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

VOLUME /app

WORKDIR /app

EXPOSE 8000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8000", "--no-browser", "--allow-root"]
