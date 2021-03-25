create database household;
set global local_infile=1;
create table if not exists household.power(
    date date,
    time time,
    global_active_power float,
    global_relative_power float,
    voltage float,
    global_intensity float,
    sub_metering_1 float,
    sub_metering_2 float,
    sub_metering_3 float
);