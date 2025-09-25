create database SE;

use SE;

-- TODO template below
-- create table User
-- (
--     id       int auto_increment	primary key,
--     name     varchar(128) unique not null,
--     email    varchar(128) unique not null,
--     password varchar(128) default '' not null
-- )charset = utf8mb4;

-- create table Device
-- (
--     id          int auto_increment primary key,
--     user_id     int references User(id),
--     client_id   varchar(128) default '' not null,
--     type        varchar(128) not null,
--     name        varchar(128) unique not null,
--     description text not null,
--     create_time datetime default CURRENT_TIMESTAMP not null
-- )charset = utf8mb4;

-- create table Message
-- (
--     id        int auto_increment primary key,
--     client_id varchar(128) default '' not null,
--     longitude double default 0.0 not null,
--     latitude  double default 0.0 not null,
--     alert     boolean default 0 not null,
--     time      datetime default CURRENT_TIMESTAMP not null,
--     info      varchar(128) default '' not null,
--     value     int default 0 not null
-- )charset = utf8mb4;