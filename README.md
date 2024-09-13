# FIWARE Descomplicado

O FIWARE Descomplicado é uma ferramenta que torna simples o processo de configurar os principais GEs (Generic Enablers) oferecidos pela FIWARE Foundation. Desenvolvido como uma solução leve baseada no Docker, este recurso foi projetado para ser flexível, adaptando-se facilmente a várias plataformas computacionais, sistemas operacionais e provedores de serviços em nuvem (CSP, do inglês Cloud Service Provider).

Com o objetivo de simplificar a experiência do usuário, esta ferramenta elimina a complexidade usual associada à instanciação dos GEs da FIWARE. Ao utilizar o FIWARE Descomplicado, usuários de diferentes perfis e níveis de habilidade podem facilmente acessar e aproveitar os benefícios dos serviços oferecidos pela FIWARE Foundation, independentemente do ambiente de computação em que estão trabalhando.

Seja na nuvem ou em ambientes locais, a versatilidade e a facilidade de uso desta ferramenta proporcionam uma integração tranquila e acessível aos recursos disponibilizados pela FIWARE Foundation, abrindo caminho para a exploração e utilização desses serviços em variados cenários e contextos.

### FIWARE

O FIWARE é uma iniciativa inovadora que começou em 2011 como uma resposta às demandas crescentes da era da Internet das Coisas (IoT, do inglês Internet of Things). Esta plataforma de código aberto foi projetada para fornecer um ambiente aberto e padronizado para o desenvolvimento de soluções inovadoras para cidades inteligentes, indústrias, agronegócio, e outros setores.

Ao longo dos anos, o FIWARE evoluiu para se tornar um ecossistema próspero, fornecendo uma série de Generic Enablers que ajudam no desenvolvimento de aplicações inovadoras baseadas em padrões abertos. Estas ferramentas incluem componentes-chave, como o Orion Context Broker para gerenciamento de dados contextuais, IoT Agents para integração de dispositivos, e o STH-Comet para armazenamento e recuperação de dados históricos.

A comunidade FIWARE cresceu, atraindo desenvolvedores, empresas e organizações do mundo todo. Seu sucesso se baseia na promoção da interoperabilidade, permitindo a conectividade entre diferentes sistemas e fornecendo uma base sólida para soluções inteligentes e inovadoras. O FIWARE não apenas promove a colaboração, mas também é uma referência na adoção de padrões abertos para garantir a escalabilidade e a adaptabilidade das soluções, independente do setor ou da aplicação.

O FIWARE não apenas oferece uma plataforma para IoT e Ambientes Inteligentes, mas vai além, promovendo uma abordagem avançada de Smart Data Models e interoperabilidade através do NGSI, sua interface de serviço de próxima geração.

Baseado em Smart Data Models, o FIWARE não apenas reúne informações, mas as organiza e as disponibiliza de forma inteligente. Esses modelos inteligentes permitem uma compreensão e interação aprimoradas com os dados em tempo real, facilitando o desenvolvimento de soluções personalizadas.

O NGSI (Next Generation Service Interface) desempenha um papel crucial ao estabelecer a interoperabilidade. Ele permite a comunicação e a troca de dados entre diferentes dispositivos e sistemas, independentemente de sua origem ou localização. Isso significa que as soluções criadas com o FIWARE podem se conectar facilmente a uma variedade de fontes de dados, tornando-o um catalisador para a inovação ao permitir a criação de soluções integradas e interconectadas para um mundo mais inteligente e conectado. 

Click <a href="https://www.fiware.org/"> aqui </a> para acessar o site do FIWARE.

Click <a href="https://fiwaretourguide.readthedocs.io/en/latest/"> aqui </a> para acessar o tour guide do FIWARE.

## Smart Data Models e MIMs (Minimal Interoperability Mechanisms)

Os Smart Data Models e MIMs representam a espinha dorsal do ecossistema do FIWARE. São modelos padronizados que desempenham um papel vital na facilitação da troca de informações entre sistemas e aplicações.

Esses modelos definem uma estrutura comum e atributos específicos para representar conceitos de domínio, promovendo a interoperabilidade e a reutilização de dados. São desenvolvidos pela vibrante comunidade do FIWARE, garantindo que diferentes sistemas possam conversar entre si de forma coesa e eficiente.

Ao estabelecer uma base comum para a representação de dados, os Smart Data Models e os MIMs abrem as portas para a integração simplificada de diversas fontes de dados. Isso impulsiona a inovação, permitindo o desenvolvimento de soluções inteligentes e inovadoras que utilizam informações provenientes de várias origens. Esses modelos não apenas simplificam a integração, mas também fomentam a criação de soluções práticas e interoperáveis para um mundo cada vez mais conectado.

A missão da Open & Agile Smart Cities (OASC) é unir cidades e comunidades globalmente, construindo um mercado de soluções, serviços e dados baseados nas necessidades locais. Para realizar isso, a OASC promove os Mecanismos de Interoperabilidade Mínima (MIMs), que representam capacidades práticas fundamentadas em especificações técnicas abertas.

Os MIMs, desenvolvidos pelo Conselho de Tecnologia da OASC e governados pelo Conselho das Cidades e pelo Conselho Diretor, desempenham um papel crucial. Eles permitem que cidades e comunidades implementem soluções em escala global, promovendo a replicação e ampliação de soluções práticas.

Esses mecanismos fornecem a base técnica para aquisição e implementação de plataformas de dados urbanos e soluções abrangentes em cidades e comunidades em todo o mundo. Por meio dos MIMs, a OASC capacita a implementação de tecnologias interoperáveis, facilitando a inovação e o desenvolvimento de soluções inteligentes adaptadas às necessidades específicas de cada localidade.

Click <a href="https://github.com/smart-data-models"> aqui </a> para acessar o repositório com os Smart Data Models usados pelo FIWARE.

Click <a href="https://oascities.org/minimal-interoperability-mechanisms/"> aqui </a> para acessar o repositório dos MIMs definidos pela OASC.


### NGSI

O NGSI é um padrão de interface que define um modelo de dados consistente e uma API (Application Programming Interface) padronizada para a troca de informações contextuais na plataforma FIWARE e outras aplicações. Ele utiliza o formato JSON e fornece métodos para criar, atualizar, recuperar e excluir dados contextuais, facilitando a interoperabilidade e a comunicação entre diferentes componentes e sistemas.

Click <a href="https://fiware-tutorials.readthedocs.io/en/stable/getting-started/index.html"> aqui </a> para acessar a documentação do NGSI-v2.

### CEF (Connecting Europe Facility)

O CEF, uma iniciativa da União Europeia, desempenha um papel crucial na promoção da interoperabilidade e conectividade digital em toda a Europa. Por meio do fornecimento de financiamento para o desenvolvimento de infraestruturas e serviços digitais, o CEF apoia projetos destinados a superar barreiras técnicas e aprimorar a interconexão e a interoperabilidade de sistemas e serviços digitais.

Essa iniciativa é um motor fundamental na jornada rumo à transformação digital e à integração europeia. Ao impulsionar o desenvolvimento de infraestruturas e serviços digitais, o CEF contribui para a facilitação do acesso, melhoria da qualidade e ampliação do alcance dos serviços digitais em toda a Europa.

Com um foco central na eliminação de obstáculos e no estímulo à colaboração entre sistemas e serviços, o CEF desempenha um papel fundamental na concretização de uma Europa mais conectada e unificada, impulsionando o progresso digital e a coesão entre os países membros.

Click <a href="https://ec.europa.eu/inea/en/connecting-europe-facility"> aqui </a> para acessar o site do CEF.

## Principais GEs (Generic Enablers)

### Orion Context Broker 

O Orion Context Broker é um componente da plataforma FIWARE que gerencia dados contextuais em tempo de execução. Ele armazena informações sobre objetos e entidades, permitindo que os desenvolvedores capturem, consultem e compartilhem esses dados. O Context Broker utiliza um modelo de publicação/assinatura para fornecer atualizações em tempo real sobre mudanças no contexto das entidades. Ele oferece uma API RESTful para interação e suporta recursos como geolocalização, histórico de dados e notificações baseadas em condições específicas.

Click <a href="https://fiware-orion.readthedocs.io/en/3.10.1/index.html"> aqui </a> para acessar a documentação do Orion Context Broker.

### STH-Comet

O STH-Comet é um componente da plataforma FIWARE que lida com o armazenamento histórico de dados contextuais em larga escala. Ele trabalha em conjunto com o Orion Context Broker para capturar, armazenar e consultar dados históricos. O STH-Comet oferece recursos avançados, como armazenamento eficiente em série temporal, consultas de agregação e consultas de séries temporais. Ele fornece uma API RESTful para interação e permite que os desenvolvedores acessem e analisem dados históricos de forma eficiente. Em resumo, o STH-Comet facilita o armazenamento e consulta de dados contextuais históricos na plataforma FIWARE.

A API do STH-Comet pode ser consumida por programas desenvolvidos em Python que podem gerar gráficos históricos através da biblioteca Matplotlib.

<br>
<p align="center">
<img src="https://github.com/fabiocabrini/fiware/blob/main/sth-comet-m.jpg">
</p>
<br>

Click <a href="README_STH_Comet_dashboard.md"> aqui </a> para acessar a documentação do código que implementa o dashboard dinâmico para o STH-Comet.

Click <a href="api-sth.py"> aqui </a> para acessar o arquivo que implementa um dashboard dinâmico para o STH-Comet.


### Documentação

Click <a href="https://fiware-sth-comet.readthedocs.io/en/latest/"> aqui </a> para acessar a documentação do STH-Comet.

Click <a href="https://documenter.getpostman.com/view/513743/RWEgqe8Q"> aqui </a> para acessar a documentação sobre queries do STH-Comet utilizando a API v2.

### IoT-Agent MQTT

O IoT Agent MQTT é um componente da plataforma FIWARE que facilita a integração de dispositivos IoT baseados em MQTT (Message Queuing Telemetry Transport). Ele permite a comunicação bidirecional entre dispositivos MQTT e o Orion Context Broker, gerenciando a transformação de mensagens MQTT em atualizações de contexto compreensíveis. Ele também oferece recursos de descoberta automática, normalização de dados e autenticação de dispositivos MQTT.

O Orion Context Broker apresenta a capacidade de se integrar facilmente a uma ampla variedade de IoT Agents, incluindo OPC UA, CoAP, e até mesmo formatos de dados como JSON, proporcionando uma conexão versátil e adaptável a diferentes protocolos e dispositivos na plataforma FIWARE.

Click <a href="https://github.com/FIWARE/tutorials.IoT-Agent"> aqui </a> para acessar a documentação do IoT Agent.

## Componentes Complementares

### MongoDB
O MongoDB, um sistema de banco de dados NoSQL, desempenha um papel essencial na plataforma FIWARE ao armazenar dados contextuais provenientes do Orion Context Broker e de outros componentes. Com suporte a documentos flexíveis no formato JSON, o MongoDB oferece uma estrutura dinâmica e escalável para lidar com uma variedade de informações na plataforma FIWARE.

Sua flexibilidade e recursos avançados para consultas não apenas simplificam o armazenamento de dados, mas também fornecem uma base robusta para lidar com grandes volumes de informações. Com a capacidade de escalar horizontalmente, o MongoDB é altamente adequado para atender às demandas crescentes de dados na plataforma FIWARE, garantindo eficiência e desempenho em meio a um ambiente em constante evolução.

Click <a href="https://www.mongodb.com/pt-br/products/compass"> aqui </a> para instalar o Mongo Compass, uma interface gráfica de gerenciamento do MongoDB.

### Eclipse-Mosquitto

O Eclipse Mosquitto é um broker MQTT usado na plataforma FIWARE para facilitar a troca de mensagens entre dispositivos IoT e outros componentes. Ele suporta recursos de autenticação, segurança e controle de acesso, fornecendo uma solução escalável e configurável para a comunicação MQTT na plataforma FIWARE. Os dados são armazenados no tópico TEF (Thing Event Function).

Click <a href="https://mosquitto.org/"> aqui </a> para acessar a documentação do Eclipse-Mosquitto MQTT Broker.

## Arquitetura Básica para Projetos de IoT

**Aplicação** atua como a face visível da aplicação, responsável pelo front-end e pelas ferramentas que interagem com dispositivos de IoT e os consumidores/provedores de contexto. Além disso, ela é a casa de inovações tecnológicas como algoritmos de machine learning, inteligência artificial, análises avançadas, dashboards e aplicativos móveis.

**Back-end** é o núcleo operacional da plataforma, onde residem elementos vitais como o Orion Context Broker, STH-Comet, IoT Agent MQTT, e o banco de dados NoSQL MongoDB. Esses componentes desempenham um papel fundamental no armazenamento e gerenciamento de entidades, registros, subscrições e dados históricos (time series). Para facilitar a comunicação, também encontramos o Eclipse-Mosquitto, um popular broker MQTT.  Além desses componentes-chave, a Camada de Back-end é um hub para a integração de outros GEs oferecidos pela FIWARE Foundation e ferramentas de terceiros. Esta camada não só proporciona a infraestrutura robusta para suportar a troca de informações, mas também serve como a espinha dorsal para a construção de soluções complexas e escaláveis.

Click <a href=https://www.fiware.org/catalogue/> aqui </a> para ver acessar a lista completa dos componentes oferecidos pela FIWARE Foundation.

**IoT** é responsável por acomodar os dispositivos de IoT que estabelecem comunicação com o back-end através dos protocolos de comunicação MQTT ou HTTP/NGSIv2.

**Observação:** Esta ferramenta **não inclui recursos de segurança**, pois é destinada a pesquisa e a construção de PoCs! Para que a sua aplicação atenda a requisitos de segurança exigidos pelo mercado é necessário acrescentar os GEs indicados pela FIWARE (Keyrock, Wilma PEP Proxy e AuthZForce PDP/PAP), habilitar os recursos de segurança do sistema operacional hospedeiro/CSP, além de protocolos com suporte a criptografia, ao exemplo do HTTPs e MQTTs. Para alta disponibilidade e escalabilidade é recomendado o uso de orquestradores como Docker Swarm ou Kubernetes.

<br>
<p align="center">
<img src="https://github.com/fabiocabrini/fiware/blob/main/FiwareDeploy_new_v4.png">
</p>
<br>
Click <a href="FiwareDeploy_new_v4.drawio"> aqui </a> para acessar o arquivo da arquitetura no formato drawio.

## Requisitos Mínimos de Hardware para operação no Ubuntu Server LTS

Núcleos de Processamento - **1vCPU**

Memória RAM - **1GB** 

Armazenamento Secundário Mínimo - **20GB HD e/ou SSD** (Depende dos requisitos da aplicação!).

## Requisitos de Software

Docker e Docker-Compose

Click <a href=https://docs.docker.com/engine/install/ubuntu/> aqui </a> para ver as instruções de instalação do Docker e do Docker-Compose no Ubuntu Server LTS.

## Vamos instalar o FIWARE Descomplicado? 

### Instalação

git clone https://github.com/fabiocabrini/fiware

### Inicialização

cd fiware

docker compose up -d

### Encerramento

docker compose down

**Observação:** O FIWARE Descomplicado utiliza volumes para que seus dados não sejam perdidos ao desligá-lo!

**Volume:** /var/lib/docker/volumes/fiware_db-data/_data

## Liberação de Portas no Firewall

1026/TCP  - **Orion Context Broker**

1883/TCP  - **Eclipse-Mosquito MQTT** 

4041/TCP  - **IoT-Agent MQTT**

8666/TCP  - **STH-Comet**

27017/TCP - **MongoDB** - Não é uma boa prática abrir essa porta em ambiente de nuvem!

## Recursos Avançados

<a href="https://fiware-tutorials.readthedocs.io/en/1.0.0/index.html">FIWARE - Step by Step</a>  - Manual Avançado do Orion Context Broker
   
<a href="https://documenter.getpostman.com/view/513743/fiware-entity-relationships/RVu8gSCh">FIWARE - Entity Relationships - Postman Collections</a> - Relacionamento entre Entidades

<a href="http://telefonicaid.github.io/fiware-orion/archive/api/v2/">FIWARE - NGSI v2 Subscriptions - Postman Collections</a> - Subscrições Condicionadas

<a href="https://fiware-orion.readthedocs.io/en/3.10.1/orion-api.html#geospatial-properties-of-entities">FIWARE - NGSI v2 API Orion 3.10.1 </a> - Novo

## Collection do Postman (Material para experimentação)

Aqui você vai encontrar um conjunto de collections desenvolvidas para serem importadas pela ferramenta Postman.  Essa collection vai ajudá-lo a interagir com os componetes Orion Context Broker, IoT Agent MQTT e STH-Comet, presentes na arquitetura do FIWARE Descomplicado.

**Observação:** Recurso disponível para a PoC - Smart Lamp.  

*Lembre-se que você pode adaptá-la as necessidades do seu projeto!*

Click <a href="https://github.com/fabiocabrini/fiware/blob/main/FIWARE Descomplicado.postman_collection.json"> aqui </a> para acessar a collection do Postman.

## PoC - Smart Lamp

Esta documentação vai ajudá-lo a construir uma PoC (Proof of Concept) baseada no exemplo do Smart Lamp, utilizando a plataforma de prototipação ESP32 DEVKIT V1, microntrolador de 32 bits da Espressif, equipado com as tecnologias de comunicação wireless Wi-Fi IEEE802.11n e Bluetooth IEEE802.15.

### Smart Lamp

Uma entidade "Smart Lamp" (ou "Lâmpada Inteligente") é um conceito dentro da plataforma FIWARE que representa uma lâmpada conectada, capaz de interagir com um ecossistema de IoT. Ela é modelada como uma entidade de dados que possui atributos e metadados associados que definem seu comportamento e características.

Uma "Smart Lamp" é caracterizada por uma série de propriedades e funcionalidades que podem incluir:

**Atributos de Estado:** Pode conter informações sobre o estado atual da lâmpada, como ligada/desligada, brilho, cor ou qualquer outra propriedade controlável.

**Atributos de Sensoriamento:** Além dos atributos de controle, a entidade "Smart Lamp" pode incluir sensores que monitoram informações ambientais, como luminosidade ambiente, temperatura ou consumo de energia.

**Comandos:** Define as ações que podem ser realizadas na lâmpada, como ligar, desligar, ajustar brilho, alterar cor, entre outros.

**Metadados e Identificadores:** Informações de identificação e metadados, como ID da entidade, tipo de entidade, protocolos de comunicação e outras informações relevantes.

A entidade "Smart Lamp" é projetada para ser parte de um ecossistema mais amplo, permitindo a integração com outras entidades e sistemas por meio de padrões abertos, promovendo a interoperabilidade e facilitando a construção de soluções inteligentes e conectadas para ambientes residenciais, urbanos ou industriais. Ela representa a base para o controle, monitoramento e interação de lâmpadas conectadas em uma infraestrutura de IoT baseada no FIWARE.

<a href="mqtt_esp32.md"> Vamos criar juntos nossa Smart Lamp?</a>

Click <a href="https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf"> aqui </a> para acessar o data sheet do ESP32.

**Tutoriais no YouTube** 

Click <a href="https://www.youtube.com/watch?v=8oHkAlXdWo8"> aqui </a> para acessar o vídeo no Youtube.

## Referências

Esse material foi simplificado e adaptado da [Fiware Foundation](https://github.com/FIWARE/tutorials.IoT-over-MQTT)

#### © Fábio Henrique Cabrini 2024, todos os direitos reservados.
