FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 9001

COPY . .

CMD [ "python",  "./run_app.py"]
