## Supermarket Simulation - Turtlebot3 Bugger

Este repositório foi criado com a finalidade de simular a plataforma Turtlebot3 (Bugger model) em modelo simplificado de Supermercado. A simulação foi divida em 3 etapas.
### Etapa 1:
Realizar mapeamento remoto do ambiente utilizando o *SLAM Gmapping*.

### Etapa 2:
Utilizar o mapa criado na etapa anterior e, através de comando via *Rviz* ou publicação via terminal, realizar movimentos entre pontos determinados do mapa.

### Etapa 3:
Com uso de um simples *script* em python, realizar um loop em 9 pontos do ambiente de forma intermitente. Esse *loop* será então quebrado através de um comando via terminal, indicando o desejo do usuário de concluir a tarefa.

## Ambiente de simulação
O ambiente escolhido foi simplificado para melhorar o desempenho e velocidade da simulação. Conforme a figura abaixo.

![World](https://github.com/rodrigoformiga/supermarket_turtlebot/images/world.png)

## Criação do mapa

O mapa foi remotamente criado e então capturado para utilizar em etapas seguintes. O vídeo e a imagem abaixo mostram detalhes dessa etapa.

![Mapping](https://github.com/rodrigoformiga/supermarket_turtlebot/images/etapa1.gif)

![Map](https://github.com/rodrigoformiga/supermarket_turtlebot/images/map.png)

## Navegação - move_base

Com o pacote move_base foram enviados comandos de posição via *Rviz* e via terminal. O vídeo demonstra esse teste.

![Move_base](https://github.com/rodrigoformiga/supermarket_turtlebot/images/etapa2.gif)

## Loop de navegação (8 pontos)

Por fim, a simulação contou com um *loop* de navegação entre pontos determinados, conforme apresentado na imagem e vídeo.

![Points](https://github.com/rodrigoformiga/supermarket_turtlebot/images/points/map.gif)

![Loop Navigation](https://github.com/rodrigoformiga/supermarket_turtlebot/images/etapa3.gif)


# Requisitos para simulação
* ROS Kinetic (outras versões não foram testas) 
* Instalar pacotes:

        * Gmapping (sudo apt-get install ros-kinetic-gmapping-*)
        * Turtlebot3 (sudo apt-get install ros-kinetic-turtlebot3-*)
        * Teleop_twist (sudo apt-get install ros-kinetic-teleop_twist-*)

# Run 

    ~$ roslaunch supermarket seletivo.launch

    ~$ export TURTLEBOT3_MODEL=burger

    ~$ roslaunch supermarket nave.launch

    ~$ rosrun supermarket mission.py