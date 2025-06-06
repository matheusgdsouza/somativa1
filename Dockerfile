FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "fastapi[standard]"

EXPOSE 80
COPY . .
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "main.py" ]