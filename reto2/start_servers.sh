#!/bin/bash
docker start rabbit-server
# Ejecutar microservicio 2
python3 microservice1/ms1_mom.py &
sleep 0.2
# Ejecutar microservicio 2
python3 grpc_client/ms2_grpc.py &
sleep 0.2
# Ejecutar server
python3 server.py &