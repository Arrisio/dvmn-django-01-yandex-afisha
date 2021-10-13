FROM python:3.9-slim-buster

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip; \
    pip install -r requirements.txt;

COPY  . /app/

#ENTRYPOINT ["python","-u"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
