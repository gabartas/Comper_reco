FROM python:3.11

COPY . /app 
WORKDIR /app

RUN pip install -r requirements_prod.txt

RUN chmod +x /app/entrypoint.sh

# run server
CMD ["/app/entrypoint.sh"]
