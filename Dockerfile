# Use an official Python runtime as a parent image
FROM python:3.6.8

# Install any needed packages specified in requirements1.txt -i https://mirrors.aliyun.com/pypi/simple
WORKDIR app

COPY / .
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple


# Run app.py when the container launches
# CMD ["python", "server.py"]
# gunicorn --workers 2 -b 0.0.0.0:8081 server:app -t 3000
CMD gunicorn -c gunicorn.conf server:app