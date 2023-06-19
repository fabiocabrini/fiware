# FIWARE Deployment Tool

Ferramenta para a instanciação dos principais GEs (Generic Enablers) destinados a IoT (Internet of Things) e persistência de dados. O FIWARE Deployment Tool é destinado exclusivamente para atividades de pesquisa e desenvolvimento de PoC (Proof of Concepts). **Não sendo recomendado para aplicações de produção!**

## Introdução

Esta ferramenta foi desenvolvida para simplificar o processo de instanciação dos principais GEs disponibilizados pela FIWARE Foundation.

### FIWARE

O FIWARE é uma plataforma de IoT e Cidades Inteligentes que adota uma arquitetura modular e padronizada para capturar, armazenar, consultar e compartilhar dados contextuais em tempo real. Ele oferece recursos avançados e é implementado usando tecnologias e padrões abertos. 

Click <a href="https://www.fiware.org/"> aqui </a> para acessar o site do FIWARE!


### NGSI (Next Generation Service Interface)

O NGSI é um padrão de interface que define um modelo de dados consistente e uma API padronizada para a troca de informações contextuais na plataforma FIWARE e outras aplicações. Ele utiliza o formato JSON e fornece métodos para criar, atualizar, recuperar e excluir dados contextuais, facilitando a interoperabilidade e a comunicação entre diferentes componentes e sistemas.

Click <a href="https://fiware-tutorials.readthedocs.io/en/stable/getting-started/index.html"> aqui </a> para acessar a documentação do NGSI-V2.

### CEF (Connecting Europe Facility)

O CEF é uma iniciativa da União Europeia que oferece financiamento para o desenvolvimento de infraestruturas e serviços digitais, visando promover a interoperabilidade e a conectividade digital em toda a Europa. Ele apoia projetos que eliminam barreiras técnicas e promovem a interconexão e a interoperabilidade de sistemas e serviços digitais, impulsionando a transformação digital e a integração europeia.

Click <a href="https://ec.europa.eu/inea/en/connecting-europe-facility"> aqui </a> para acessar o site do CEF.

## Principais GEs (Generic Enablers)

### Orion Context Broker 

O Orion Context Broker é um componente da plataforma FIWARE que gerencia dados contextuais em tempo real. Ele armazena informações sobre objetos e entidades, permitindo que os desenvolvedores capturem, consultem e compartilhem esses dados. O Context Broker utiliza um modelo de publicação/assinatura para fornecer atualizações em tempo real sobre mudanças no contexto das entidades. Ele oferece uma API RESTful para interação e suporta recursos como geolocalização, histórico de dados e notificações baseadas em condições específicas. Em resumo, o Orion Context Broker facilita o desenvolvimento de soluções inteligentes para IoT e Cidades Inteligentes, permitindo o gerenciamento de dados contextuais em tempo real.

Click <a href="https://fiware-orion.readthedocs.io/en/master/index.html"> aqui </a> para acessar a documentação do Orion Context Broker.

### STH-Comet

O STH-Comet é um componente da plataforma FIWARE que lida com o armazenamento histórico de dados contextuais em larga escala. Ele trabalha em conjunto com o Orion Context Broker para capturar, armazenar e consultar dados históricos. O STH-Comet oferece recursos avançados, como armazenamento eficiente em série temporal, consultas de agregação e consultas de séries temporais. Ele fornece uma API RESTful para interação e permite que os desenvolvedores acessem e analisem dados históricos de forma eficiente. Em resumo, o STH-Comet facilita o armazenamento e consulta de dados contextuais históricos na plataforma FIWARE.

### IoT-Agent MQTT

O IoT Agent MQTT é um componente da plataforma FIWARE que facilita a integração de dispositivos IoT baseados em MQTT. Ele permite a comunicação bidirecional entre dispositivos MQTT e o Orion Context Broker, gerenciando a transformação de mensagens MQTT em atualizações de contexto compreensíveis. Ele também oferece recursos de descoberta automática, normalização de dados e autenticação de dispositivos MQTT.

## Componentes Complementares

### MongoDB
O MongoDB é um sistema de banco de dados NoSQL usado na plataforma FIWARE para armazenar dados contextuais provenientes do Orion Context Broker e de outros componentes. Ele suporta documentos JSON flexíveis, possui recursos avançados para consultas e escalabilidade horizontal, tornando-o adequado para lidar com grandes volumes de dados na plataforma FIWARE.

### Eclipse-Mosquitto

O Eclipse Mosquitto é um broker MQTT usado na plataforma FIWARE para facilitar a troca de mensagens entre dispositivos IoT e outros componentes. Ele suporta recursos de autenticação, segurança e controle de acesso, fornecendo uma solução escalável e configurável para a comunicação MQTT na plataforma FIWARE.

## Arquitetura de Referência 
<br>

<img src="https://github.com/fabiocabrini/fiware/blob/main/FiwareDeploy.png">

<br>

## Requisitos de Software

Docker e Docker-Compose

Click <a href=https://docs.docker.com/get-docker/> aqui </a> para ver as instruções de instalação do Docker e do Docker-Compose!

## Requisitos de Hardware 

Núcleos de Processamento - 1vCPU

Memória RAM - 1GBytes 

Armazenamento Secundário - 20GB HD e/ou SSD (Vai depender da quantidade de entidades e dados históricos armazenados no banco de dados)

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
