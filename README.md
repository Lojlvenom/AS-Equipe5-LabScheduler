# AS-Equipe5-LabScheduler
 Ifam labs scheduling system.

## Integrantes
João Lucas Farias Camilo - 2019008160  
Guilherme de Sousa Peixoto - 2019003074  
Rebeca Cancelli Archer Pinto - 2019003181  
Keven Lucas Paiva de Paula  - 2019003083  



## Descrição do Problema
Atualmente o processo de reserva dos laboratórios do IFAM, baseando-se na realidade do campus CMZL, ainda é um processo manual e com baixa disponibilidade de acesso, com base nessa realidade densenvolvemos um sisitema para realizar reservas de laboratórios e espaços, com notificação.

## Arquitetura e soluções aplicadas

<p align="center">
    <img width="50%" src="https://user-images.githubusercontent.com/72761456/126085063-b7f6fe0e-521a-47fa-be74-a23254d0e81d.png" />
</p>
  
## Descrição e justificativa de tecnologias


Como a solução implementada se tratava de microserviços que deveriam se comunicar, foram contruidas uma API para cada serviço. Para realizar essa comunicação foi decidido utilizar JSON como padrão, assim foram utilizadas as seguintes tecnologias. 

Flask-RESTful é uma extensão do Flask que adiciona suporte para a construção rápida de APIs REST. É uma abstração leve que funciona com seus ORM / bibliotecas existentes. Foi utilizado para que todos os serviços se comuniquem com mais facilidade e usado esta tecnologia, construindo pacotes json.

HTTP é um protocolo de camada de aplicação para transmissão de documentos hipermídia, utilizando seus metodos de transmissão para realizar a troca dos pacotes JSON entre os serviços de Login/Usuários, Laboratórios e Reservas.

Mensageria usando a lib RabbitMQ o serviço de notificação orientado a eventos, assim que o serviço de Reserva confirma a criação da reserva, por meio do request enviado, pega uma lista de emails, e envia a confirmação do evento. 

## Funcionalidades Implementadas

### Serviço de Login/Usuários
Feito pelo integrante Keven Lucas Paiva de Paula, este serviço é responsável por realizar o cadastro, login e autenticação de usuários no sistema.


### Serviço de Laboratórios
Feito pelo integrante Guilherme de Sousa Peixoto, este serviço é responsável por cadastrar, listar e deletar os laboratórios. 

### Serviço de Reserva dos Laboratórios (Booking)

Feito pela integrante Rebeca Cancelli Archer Pinto, este serviço é responsável por fazer a reserva dos laboratórios para o usuário, verificando a disponibilidade da data e turno do laboratório desejado, a listagem e a remoção das reservas.


### Serviço de Notificação
Feito pelo integrante João Lucas Farias Camilo, esta funcionalidade é responsável por notificar via e-mail qualquer evento relacionado a uma reserva de laboratório.

## Padrões de projeto presentes

Adapter - O padrão de projeto Adapter permite com que os serviços de diferentes interfaces interajam entre si, usando notação JSON para trocar informações abstraindo a complexidade de como opera cada classe.

Decorator - O decorator é amplamente utilizado na definição das rotas presentes no controller princial da aplicação, a utilização deste padrão permite a reusabilidade da mesma estrutura em diferentes definições de rotas.

Factory - O padrão factory é utilizado na criação das filas do sistema de messageria presente no serviço de notificação, com isso é possivel criar várias instâncias do tipo fila dentro do projeto para a comunicação de diferentes módulos.


## Manual de instalação 
1. Instalar pacotes nescessários
```bash
sudo apt-get install rabbitmq-server python3 python3-venv moreutils

```
2. Habilitar o serviço de messageria(rabbitmq).
```bash
sudo service rabbitmq-server start

```
3. Criar um ambiente virtual usando o python3 e ativar esse ambiente
```bash
python3 -m venv nome_do_env
source nome_do_env/bin/activate

```

4. Com o ambiente ativado, instalar todas as dependências nescessárias utilizando o pip localizados no arquivo requirements.txt

```bash
pip install -r requirements.txt
```
4. Executar o arquivo run.sh

```bash
sudo chmdo a+x run.sh
./run.sh
```

