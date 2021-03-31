FROM focal_py38_gdal_postgres12:2
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
#RUN python3 manage.py migrate
#RUN python3 manage.py createsuperuser --noinput
#RUN export PGPASSWORD=$POSTGRES_PASSWORD
#RUN psql -h $POSTGRES_HOST -d $POSTGRES_DB -U $POSTGRES_USER  -p $POSTGRES_PORT -f cynr_ini.psql 