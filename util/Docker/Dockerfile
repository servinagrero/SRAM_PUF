FROM python:3.7

# Install the necessary modules
COPY ./jupyter/requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Copy the notebooks and the data
COPY ./jupyter /app

WORKDIR /app

EXPOSE 8000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8000", "--no-browser", "--allow-root"]
