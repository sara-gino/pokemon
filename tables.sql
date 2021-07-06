drop  database DB_Pokemon;
create database DB_Pokemon;
use DB_Pokemon;

create table pokemon(
id int primary key,
name  varchar(50),
height  int,
weight int
);

create table trainer(
id int AUTO_INCREMENT  primary key,
name  varchar(50),
town varchar(50)
);

create table type(
id int,
name  varchar(50),
foreign key (id) references pokemon(id)
);

 create table owner_by(
 id_pokemon int,
 id_trainer int,
 primary key(id_pokemon,id_trainer),
 foreign key (id_pokemon) references pokemon(id),
 foreign key (id_trainer) references trainer(id)
);
