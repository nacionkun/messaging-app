FROM python:3.6.4-slim-jessie
EXPOSE 4001
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]

# EXPOSE 27017 or 2001
