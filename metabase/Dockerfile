FROM mysql:8.0.23

RUN mkdir /home/mysql && \
    cd /home/mysql && \
    mkdir contents
COPY contents/reformed_household_power_consumption.txt /home/mysql/contents/reformed_household_power_consumption.txt
RUN chmod -R 777 /home/mysql 
COPY contents/setup.sql /docker-entrypoint-initdb.d/00_setup.sql 
COPY contents/load_data.sh /docker-entrypoint-initdb.d/01_load_data.sh