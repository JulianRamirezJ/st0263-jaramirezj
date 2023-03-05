#!/bin/bash
cd /home/ubuntu/st0263-jaramirezj/reto2
docker start rabbit-server
sleep 0.5
# Ejecutar microservicio 1
python3 microservice1/ms1_mom.py &
sleep 0.2
# Ejecutar microservicio 2
python3 grpc_client/ms2_grpc.py &
sleep 0.2
# Ejecutar server
python3 server.py &



