## ESP32 LED + LDR Sensor
### Sobre

O código abaixo foi desenvolvido para ser aplicado no DOIT ESP32 DEVKIT V1 para funcionar conectado ao FIWARE Descomplicado de forma muito simples e intuitiva através do protocolo MQTT. 

**Observação:** Você deve realizar os passos a seguir utilizando a collection do Postman!

### IoT Agent

1.1: Apresenta a versão do IoT Agent MQTT

1.2: Verifica se já existe um FIWARE Service cadastrado

#### Criação do FIWARE Service:

2: Criação do FIWARE Service (Realizar esse procedimento uma única vez)

#### Criação e registro do dispositivo:

3: Provisionamento do dispositivo no IoT Agent MQTT

4: Registro do dispositivo virtual no Orion Context Broker

#### Operação do dispostivo:

6: Envia comandos on/off para o dispositivo

7: Busca no Orion o valor de luminosidade enviado pelo dispositivo

8: Busca no Orion o status do LED presente no dispositivo

#### Listar e deletar dispositivos:

5: Lista os dispositivos presentes no FIWARE Descomplicado

9: Deleta o dispositivo 

### Orion Context Broker 

1: Apresenta a versão e diversas informações sobre o Orion Context Broker

2: Apresenta os dispositivos cadastrados no FIWARE Descomplicado

### STH-Comet

1: Apresenta a versão do STH-Comet

2: Realiza a ativação do armazenamento temporal

3: Apresenta os valores históricos de acordo com os parâmetros estabelecidos

### Diagrama Elétrico

![](esp32_ldr.png)

### Código para o ESP32

<a href="fiware_ngsi_mqtt_esp32.ino"> Código fonte para o ESP32 DEVKIT V1</a>

<a href="esp32_ntp.ino"> Código fonte para utilizar o NTP para geração de time stamp</a>

