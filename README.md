# test_task_data_ox

**This is simple API for retriving historical data from yahoo finance.**

*Endpoint to retriave whole bunch of data:*
all_data/

*Endpoint to retrive data for specific company:*
all_data?ticker=RUN

all_data?ticker=DOCU

**Commands for docker would be next:**

- docker-compose build

- docker-compose run my_web python finance_api/manage.py migrate

- docker-compose run my_web python finance_api/manage.py api_parsing

- docker-compose up

- docker-compose down
