-- create database VemDeVan;

create table veiculo(
	placa varchar(7) not null,
	primary key(placa)
);

create table usuario(
	cpf varchar(11) not null,
	telefone varchar(11) UNIQUE not null,
	nome varchar(50) not null,
	data_nasc date not null,
	email varchar(50) UNIQUE not null,
	senha varchar(8) not null,
	cnh varchar(11) UNIQUE null,
	veiculo_placa varchar(7) UNIQUE null,
	constraint fk_veiculo_placa foreign key (veiculo_placa) references veiculo(placa),
	primary key(cpf)
);

create table local(
	id serial,
	rua varchar (50) not null,
	numero int not null,
	cidade varchar(50) not null,
	estado varchar (50) not null,
	primary key(id)
);

create table trajeto(
	id serial,
	local_chegada int not null,
	local_saida int not null,
	passageiro_cpf varchar(11) not null,
	motorista_cpf varchar(11) not null,
	constraint fk_passageiro_cpf foreign key (passageiro_cpf) references usuario(cpf),
	constraint fk_motorista_cpf foreign key (motorista_cpf) references usuario(cpf),
	constraint fk_local_chegada foreign key(local_chegada) references local(id),
	constraint fk_local_saida foreign key(local_saida) references local(id),
	primary key(id)
);
