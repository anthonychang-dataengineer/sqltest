FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas

CMD ["python", "load_test.py","query_test.py"]