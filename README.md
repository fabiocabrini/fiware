# FIWARE Deployment Tool

Ferramenta para instanciação dos GEs (Generic Enablers) destinados a IoT (Internet of Things) e persistência de dados.

## Introdução

Esta ferramenta foi criada para simplificar o processo de instanciação do Orion Context Broker, STH-Comet, MongoDB, IoT-Agent e Eclipse-Mosquitto.

## Arquitetura de Referência 
<br>

<img src="https://github.com/fabiocabrini/fiware/blob/main/FiwareDeploy.png">

<br>

## Requisitos de Software

Docker e Docker-Compose

Click <a href=https://docs.docker.com/get-docker/> aqui </a> para ver as instruções de instalação do Docker e do Docker-Compose!

## Requisitos de Hardware Mínimos

Núcleos de processamento - 1vCPU

Memória RAM - 1GBytes 

Armazenamento secundário - 20GB HD e/ou SSD (Vai depender da quantidade de entidades e dados históricos que serão armazenados no banco de dados.)

## Liberação de Portas no Firewall

1026  - API Orion

1883  - Eclipse-Mosquito 

4041  - API IoT-Agent

8666  - API STH-Comet

27017 - MongoDB

## Collection do Postman (demonstração!)

Click <a href="https://github.com/fabiocabrini/fiware/blob/main/FIWARE.postman_collection.json"> aqui </a> para acessar a collection do Postman!

## Reference

Esse material foi simplificado e adaptado da [Fiware Foundation](https://github.com/FIWARE/tutorials.IoT-over-MQTT)

#### © Fábio Henrique Cabrini 2023, All rights reserved.
