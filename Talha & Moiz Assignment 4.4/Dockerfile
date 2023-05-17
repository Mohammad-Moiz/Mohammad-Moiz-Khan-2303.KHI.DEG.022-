FROM python:3.8-slim-buster
WORKDIR /home/app/
COPY ./ /home/app/
ENV PYTHONPATH=${PYTHONPATH}:/home/app/

VOLUME /app/todo_data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]


