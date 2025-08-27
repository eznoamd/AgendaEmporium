create database bancoEmporium;
use bancoEmporium;
create table status(
id int auto_increment,
nome varchar(45),
cor varchar(7),
ativo bool,
primary key(id)
);
create table tipo(
id int auto_increment,
nome varchar(45),
filtros varchar(300),
ativo bool,
primary key(id)
);
create table tecnica(
id int auto_increment,
nome varchar(45),
ativo bool,
primary key(id)
);
create table cliente(
id int auto_increment,
nome varchar(128),
codigo varchar(300),
primary key(id)
);
create table agendamento(
id int auto_increment,
data_agendamento date,
hora_inicio time,
hora_fim time,
reagendado bool,
status_id int,
tipo_id int,
tecnica_id int,
primary key(id),
foreign key (status_id) references status(id),
foreign key (tipo_id) references tipo(id),
foreign key (tecnica_id) references tecnica(id)
);