FROM python:3.8

ADD main.py .

RUN pip install beautifulsoup4 requests

CMD ["python" , "./main.py"]
