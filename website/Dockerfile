FROM python:alpine3.7 
RUN pip install flask
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 8000
ENV FLASK_APP=app.py:website
CMD ["flask", "run", "--host", "0.0.0.0", "--port","8000"]
