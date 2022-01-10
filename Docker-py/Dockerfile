# testing using scikit learn & py in docker
From python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirments.txt
COPY . .

CMD [ "python", "./script.py"]
