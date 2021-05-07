# test_task_data_ox

**This is simple API for retriving historical data from yahoo finance.**

```git clone https://github.com/ViktorRaboshchuk/test_task_data_ox```


*Endpoint to retriave whole bunch of data:*

http://0.0.0.0:8000/all_data/

*Endpoint to retrive data for specific company:*

http://0.0.0.0:8000/all_data?ticker=RUN

http://0.0.0.0:8000/all_data/?ticker=DOCU


**Commands for docker would be next:**

```
docker-compose build
docker-compose run my_web python finance_api/manage.py migrate
docker-compose run my_web python finance_api/manage.py api_parsing
docker-compose up
docker-compose down
```
