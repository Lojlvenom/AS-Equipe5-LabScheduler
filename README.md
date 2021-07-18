# AS-Equipe5-LabScheduler
 Ifam labs scheduling system.

## Integrantes
João Lucas Farias Camilo - 2019008160
Guilherme de Sousa Peixoto - 2019003074
Rebeca Cancelli Archer Pinto - 2019003181
Keven Lucas Paiva de Paula  - 2019003083



## Descrição do Problema
Atualmente o processo de reserva dos labortáios do IFAM, baseando-se na realidade do campus CMZL, ainda é um processo manual e com baixa disponibilidade de acesso, com base nessa realidade densenvolvemos um sisitema para realizar reservas de laboratórios e espaços, com notificação.

## Arquitetura e soluções aplicadas

## Descrição e justificativa de tecnologias


## Funcionalidades Implementadas
### Serviço de notificação
Feito pelo integrante João Lucas Farias Camilo, esta funcionalidade é responsável por notificar via e-mail qualquer evento relacionado a uma reserva de laboratório.

## Padrões de projeto presentes
Decorator - O decorator é amplamente utilizado na definição das rotas presentes no controller princial da aplicação, a utilização deste padrão permite a reusabilidade da mesma estrutura em diferentes definições de rotas.

Factory - O padrão factory é utilizado na criação das filas do sistema de messageria presente no serviço de notificação, com isso é possivel criar várias instâncias do tipo fila dentro do projeto para a comunicação de diferentes módulos.

## Manual de instalação 
