FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /test_task_data_ox
COPY requirements.txt /test_task_data_ox/
RUN pip install -r requirements.txt
COPY . /test_task_data_ox/
