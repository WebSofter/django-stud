FROM python:3.11.3-slim-bullseye

# set work deirectory
WORKDIR /usr/src/app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install mysql dependencies
RUN apt-get update
RUN apt-get install gcc default-libmysqlclient-dev pkg-config -y

COPY ./app/requirements.txt .
COPY ./init.docker.sh .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

# running migrations
# RUN python manage.py migrate

# # gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]

# Convert plain text files from Windows or Mac format to Unix
RUN apt-get install dos2unix
RUN dos2unix --newfile init.docker.sh /usr/local/bin/init.docker.sh

# Make entrypoint executable
RUN chmod +x /usr/local/bin/init.docker.sh

# Entrypoint dependencies
RUN apt-get install netcat -y

# run entrypoint.sh
ENTRYPOINT ["bash", "/usr/local/bin/init.docker.sh"]