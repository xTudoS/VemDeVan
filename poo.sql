create database VemDeVan;

create table veiculo(placa varchar(7) not null,
					marca varchar(12) not null, 
					modelo varchar(15) not null, 
					cor varchar(10), 
					primary key(placa));

create table local1(id_local serial not null, 
			rua varchar (50) not null, 
			numero int not null, 
			cidade varchar(50) not null, 
			estado varchar (50) not null, 
			primary key(id_local));

create table trajeto(id_trajeto serial not null, local_chegada int not null,
					local_saida int not null,
					horario time not null,
					distancia_km int not null, 
					constraint fk_local_chegada foreign key(local_chegada) references local1(id_local), 
					constraint fk_local_saida foreign key(local_saida) references local1(id_local),
					primary key(id_trajeto));


create table usuario(cpf varchar(11) not null, cnh varchar(11) set null, telefone varchar(11) not null, 
						nome varchar(50) not null, 
						data_nasc date not null,  
						placa varchar(7) set null, 
						email varchar(50) not null, 
						senha varchar(8) not null,
						primary key(cpf));


create table historico_trajetos(id serial, 
								trajeto int not null,
								passageiro_cpf varchar(11) not null,
								motorista_cpf varchar(11) not null,
								constraint fk_trajeto foreign key (trajeto) references trajeto(id_trajeto),
								constraint fk_passageiro_cpf foreign key (passageiro_cpf) references usuario(cpf),
								constraint fk_motorista_cpf foreign key (motorista_cpf) references usuario(cpf),
								primary key(id));

create table denuncias (id_denun serial not null, denuncia text,
						cpf_user varchar(11),
						foreign key (cpf_user) references usuario(cpf),
						primary key(id_denun));
						
create table passageiro_caixa( id_caixapass serial, dinheiro_passageiro float, primary key(dinheiro_passageiro));

create table motorista_caixa(id_caixamot serial, dinheiro_motorista float, primary key(dinheiro_motorista));

create table caixa (id_caixa serial not null, dinheiro_motorista float, dinheiro_passageiro float,
						foreign key (dinheiro_motorista) references motorista_caixa(dinheiro_motorista),
						foreign key (dinheiro_passageiro) references passageiro_caixa(dinheiro_passageiro),
						primary key (id_caixa));
						
						
'constraint fk_placa foreign key (placa) references veiculo(placa),'

