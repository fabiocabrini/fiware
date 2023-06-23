# FIWARE Descomplicado

Ferramenta para a instanciação dos principais GEs (Generic Enablers) destinados a operação como back-end para aplicações de IoT (Internet of Things) com persistência de dados. O FIWARE Deployment Tool é destinado exclusivamente para atividades de pesquisa e desenvolvimento de PoCs (Proof of Concepts) que implementam soluções baseadas no processamento de informações de contexto padronizadas.

**Não é recomendado para aplicações de produção!**

## Introdução

Esta ferramenta foi desenvolvida para simplificar o processo de instanciação dos principais GEs disponibilizados pela FIWARE Foundation.  O FIWARE Deployment Tool permite através do uso do Docker Compose que é uma ferramenta que facilita a definição e o gerenciamento de aplicativos multi-container no Docker. Sua principal função é permitir a definição de um ambiente de aplicativo completo, que pode consistir em vários serviços, cada um executado em seu próprio conteiner Docker. 

### FIWARE

O FIWARE é uma plataforma de IoT e Ambientes Inteligentes que adota uma arquitetura modular e padronizada para capturar, armazenar, consultar e compartilhar dados contextuais em tempo de execução. Oferece recursos avançados e sua implementação utiliza tecnologias e padrões abertos. 

Click <a href="https://www.fiware.org/"> aqui </a> para acessar o site do FIWARE.

## Smart Data Models e MIMs (Minimal Interoperability Mechanisms)

Os Smart Data Models (Modelos de Dados Inteligentes) e MIMs (Minimal Interoperability Mechanisms) são modelos padronizados que facilitam a troca de informações entre sistemas e aplicações no contexto do FIWARE. Eles definem uma estrutura comum e atributos para representar conceitos específicos de domínio, promovendo a interoperabilidade e reutilização de dados. Esses modelos são desenvolvidos pela comunidade do FIWARE e visam facilitar a integração de diferentes fontes de dados, impulsionando a inovação e o desenvolvimento de soluções inteligentes. 

A missão da Open & Agile Smart Cities (OASC) é unir cidades e comunidades ao redor do mundo para criar um mercado global de soluções, serviços e dados com base nas necessidades dessas cidades e comunidades. Para isso, a OASC promove os Mecanismos de Interoperabilidade Mínima (MIMs), que são capacidades práticas baseadas em especificações técnicas abertas. Os MIMs permitem que cidades e comunidades repliquem e dimensionem soluções globalmente. Eles são desenvolvidos pelo Conselho de Tecnologia da OASC e são governados pelo Conselho das Cidades e pelo Conselho Diretor. Os MIMs fornecem a base técnica para aquisição e implantação de plataformas de dados urbanos e soluções abrangentes em cidades e comunidades ao redor do mundo.

Click <a href="https://github.com/smart-data-models"> aqui </a> para acessar o repositório com os Smart Data Models usados pelo FIWARE.

Click <a href="https://oascities.org/minimal-interoperability-mechanisms/"> aqui </a> para acessar o repositório dos MIMs definidos pela OASC.


### NGSI (Next Generation Service Interface)

O NGSI é um padrão de interface que define um modelo de dados consistente e uma API padronizada para a troca de informações contextuais na plataforma FIWARE e outras aplicações. Ele utiliza o formato JSON e fornece métodos para criar, atualizar, recuperar e excluir dados contextuais, facilitando a interoperabilidade e a comunicação entre diferentes componentes e sistemas.

Click <a href="https://fiware-tutorials.readthedocs.io/en/stable/getting-started/index.html"> aqui </a> para acessar a documentação do NGSI-v2.

### CEF (Connecting Europe Facility)

O CEF é uma iniciativa da União Europeia que oferece financiamento para o desenvolvimento de infraestruturas e serviços digitais, visando promover a interoperabilidade e a conectividade digital em toda a Europa. Ele apoia projetos que eliminam barreiras técnicas e promovem a interconexão e a interoperabilidade de sistemas e serviços digitais, impulsionando a transformação digital e a integração europeia.

Click <a href="https://ec.europa.eu/inea/en/connecting-europe-facility"> aqui </a> para acessar o site do CEF.

## Principais GEs (Generic Enablers)

### Orion Context Broker 

O Orion Context Broker é um componente da plataforma FIWARE que gerencia dados contextuais em tempo de execução. Ele armazena informações sobre objetos e entidades, permitindo que os desenvolvedores capturem, consultem e compartilhem esses dados. O Context Broker utiliza um modelo de publicação/assinatura para fornecer atualizações em tempo real sobre mudanças no contexto das entidades. Ele oferece uma API RESTful para interação e suporta recursos como geolocalização, histórico de dados e notificações baseadas em condições específicas.

Click <a href="https://fiware-orion.readthedocs.io/en/3.10.1/index.html"> aqui </a> para acessar a documentação do Orion Context Broker.

### STH-Comet

O STH-Comet é um componente da plataforma FIWARE que lida com o armazenamento histórico de dados contextuais em larga escala. Ele trabalha em conjunto com o Orion Context Broker para capturar, armazenar e consultar dados históricos. O STH-Comet oferece recursos avançados, como armazenamento eficiente em série temporal, consultas de agregação e consultas de séries temporais. Ele fornece uma API RESTful para interação e permite que os desenvolvedores acessem e analisem dados históricos de forma eficiente. Em resumo, o STH-Comet facilita o armazenamento e consulta de dados contextuais históricos na plataforma FIWARE.

Click <a href="https://fiware-sth-comet.readthedocs.io/en/latest/"> aqui </a> para acessar a documentação do STH-Comet.

### IoT-Agent MQTT

O IoT Agent MQTT é um componente da plataforma FIWARE que facilita a integração de dispositivos IoT baseados em MQTT (Message Queuing Telemetry Transport). Ele permite a comunicação bidirecional entre dispositivos MQTT e o Orion Context Broker, gerenciando a transformação de mensagens MQTT em atualizações de contexto compreensíveis. Ele também oferece recursos de descoberta automática, normalização de dados e autenticação de dispositivos MQTT.

Click <a href="https://github.com/FIWARE/tutorials.IoT-Agent"> aqui </a> para acessar a documentação do IoT Agent.

## Componentes Complementares

### MongoDB
O MongoDB é um sistema de banco de dados NoSQL usado na plataforma FIWARE para armazenar dados contextuais provenientes do Orion Context Broker e de outros componentes. Ele suporta documentos JSON flexíveis, possui recursos avançados para consultas e escalabilidade horizontal, tornando-o adequado para lidar com grandes volumes de dados na plataforma FIWARE.

Click <a href="https://www.mongodb.com/pt-br/products/compass"> aqui </a> para instalar o Mongo Compass, uma interface gráfica de gerenciamento do MongoDB.

### Eclipse-Mosquitto

O Eclipse Mosquitto é um broker MQTT usado na plataforma FIWARE para facilitar a troca de mensagens entre dispositivos IoT e outros componentes. Ele suporta recursos de autenticação, segurança e controle de acesso, fornecendo uma solução escalável e configurável para a comunicação MQTT na plataforma FIWARE.

Click <a href="https://mosquitto.org/"> aqui </a> para acessar a documentação do Eclipse-Mosquitto MQTT Broker.

## Arquitetura Básica de IoT

**Camada de Aplicação** é responsável pelo front-end da aplicação e ferramentas que irão consumir e interagir com os dispositivos de IoT e com consumidores/provedores de contexto, bem como, acomodar algoritmos de machine learning, inteligência artificial, analytics, dashboards, app mobile e muito mais.

**Camada de back-end** abriga o Orion Context Broker, STH-Comet e o IoT Agent MQTT, também é possível encontrar o banco de dados NoSQL MongoDB responsável pelo armazenamento das entidades, registros, subscrições e dados históricos (time series), além do Eclipse-Mosquitto, um popular broker MQTT.  Nesta camada é possível incluir os demais GEs oferecidos pela FIWARE Foundation e ferramentas de terceiros.

Click <a href=https://www.fiware.org/catalogue/> aqui </a> para ver acessar a lista dos demais componentes oferecidos pela FIWARE Foundation.

**Camada IoT (Internet of Things)** é responsável pelos dispositivos de IoT que estabelecem comunicação com a aplicação através dos protocolos MQTT ou HTTP/NGSIv2.

**Observação** A ferramenta não inclui recursos de segurança, pois é destinada a pesquisa e PoCs! Para que sua aplicação atenda a requisitos de segurança e acrescentar os GEs indicados pela FIWARE (Keyrock, Wilma PEP Proxy e AuthZForce PDP/PAP), habilitar os recursos de segurança do sistema operacional hospedeiro/CSP e protocolos com suporte a criptografia, ao exemplo do HTTPs e MQTT.


<br>
<p align="center">
<img src="https://github.com/fabiocabrini/fiware/blob/main/FiwareDeploy.png">
</p>
<br>
Click <a href="FiwareDeploy.drawio"> aqui </a> para acessar o arquivo da arquitetura no formato drawio.

## Requisitos de Software

Docker e Docker-Compose

Click <a href=https://docs.docker.com/engine/install/ubuntu/> aqui </a> para ver as instruções de instalação do Docker e do Docker-Compose no Ubuntu Server LTS.

## Instalação 

git clone https://github.com/fabiocabrini/fiware

cd fiware

docker-compose up -d

## Requisitos de Hardware 

Núcleos de Processamento - **1vCPU**

Memória RAM - **1GB** 

Armazenamento Secundário - **20GB HD e/ou SSD** (Depende da quantidade de entidades e dados históricos armazenados no banco de dados).

## Liberação de Portas no Firewall

1026/TCP  - **API Orion Context Broker**

1883/TCP  - **Eclipse-Mosquito MQTT** 

4041/TCP  - **API IoT-Agent MQTT**

8666/TCP  - **API STH-Comet**

27017/TCP - **MongoDB**

## Recursos Avançados

<a href="https://smartdatamodels.org/">FIWARE - Smart Data Models</a> - Modelos de Dados
   
<a href="https://fiware-tutorials.readthedocs.io/en/1.0.0/index.html">FIWARE - Step by Step</a>  - Manual Avançado do Orion Context Broker
   
<a href="https://documenter.getpostman.com/view/513743/fiware-entity-relationships/RVu8gSCh">FIWARE - Entity Relationships - Postman Collections</a> - Relacionamento entre Entidades

<a href="http://telefonicaid.github.io/fiware-orion/archive/api/v2/">FIWARE - NGSI v2 Subscriptions - Postman Collections</a> - Subscrições Condicionadas

<a href="https://fiware-orion.readthedocs.io/en/3.10.1/orion-api.html#geospatial-properties-of-entities">FIWARE - NGSI v2 API Orion 3.10.1 </a> - Novo

## Collection do Postman (material para demonstração)

Click <a href="https://github.com/fabiocabrini/fiware/blob/main/FIWARE.postman_collection.json"> aqui </a> para acessar a collection do Postman.

## Referências

Esse material foi simplificado e adaptado da [Fiware Foundation](https://github.com/FIWARE/tutorials.IoT-over-MQTT)

#### © Fábio Henrique Cabrini 2023, All rights reserved.
