# Info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiante: Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# API GATEWAY y microservicios a través de MOM Y gRPC.
#

1. En esta actividad se desarrollaron dos microservicios basicos, que corresponden a listar y
buscar un tipo de archivo especifico. Estos microservicios se implementaron dos veces, ya que se tiene un API Gateway
que actua como balnceador de carga entre los dos servidores que proveen estos microservicios. Aqui hay un punto muy importante
a resaltar, y es que cada servidor que provee los microservicios se comunica de una forma diferente con el API, por un lado tenemos un
servicio que se comunica mediante un MOM haciendo uso de colas. Por otro lado tenemos otro servicio que se comunica mediante gRPC.
Cuando el API recibe una petición este llama a alguno de los dos programas sea el de MOM o el de gRPC para que se comuniquen con el
servicio respectivo, le solicite los recursos, y este los reciba, con lo que el API ya podrá retornar una respuesta.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 Los aspectos propuestos por el profesor era hacer el API, además de implementar los dos servicios con MOM y gRPC, en este caso
 cumplí todos los requerimientos funcionales.
 Por el lado de los no funcionales se cumplió el hecho de desplegar el proyecto en una máquina EC2 de amazon, además de hacer uso
 de RabbitMQ.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 Se desarrolló todo lo que se propuso para este reto 2.
# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

   ![API_MOM_GRPCpng](https://user-images.githubusercontent.com/57159295/222502769-ced250b8-9c67-42cc-a1a1-7a0830886cd3.png)
   
   Como se puede ver en la imagen la arquitectura del proyecto consta de un cliente como puede ser POSTMAN, que se comunica con una petción 
   GET con el API GATEWAY. Este API GATEWAY a su vez se comunica con dos microservicios: microservice1 y microservice2. Para comunicarse con 
   el microservicio 1 se hace a través del MOM RabbitMQ haciendo uso de colas. Para comunicarse con el microservicio 2 se hace a través de gRPC.
   Otro imporrante aspecto a tener en cuenta en la arquitectura, es que el despliegue de el API REST y los microservicios se hizo en una instancia
   de EC2 de amazon,

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

   - Para desarrollar el proyecto se utilizó principamennte el lenguaje de programación python en su versión 3.10.6. En este lenguaje se programó tanto la API REST
     como la comunicación con los microservicios y los mismos microservicios.
   - Para desarrollar el API se utilizó el micro Framework Flask como servidor.
   - En cuanto al MOM se hizo uso de RabbitMQ. Para conectarnos y hacer uso de las utilidades que proveee Rabbit debemos importar la libreria 'pika'.
   - Se hace uso de docker para montar sobre este el servidor de RabbitMQ.
   - Para lograr hacer la comunicación con gRPC se utilizó la libreria 'grpcio',en su  versión 1.37.1 con la utilidad 'grpcio-tools'. 
   - Para el correcto funcionamiento de grpc se utilizó la libreria 'futures'.
   - Se hace uso de la libreria 'os' para obtener la lista de archivos del directorio seleccionado.
   - Se hizo uso de la libreria 'json' para poner los mensajes que retornan los microservicios en formato json.
   - Se utilizó la libreria 'sys' para manejar las importaciones en ciertos directorios.

## Como se compila y ejecuta.

Para compilar y ejecutar el proyecto se siguieron los pasos listados a continuación:
 Las dependencias necesarias para que el proyecto funcione que deben ser instaladas son:
  1. Instalar python 3 (sudo apt install python3 )
  2. Instalar docker:
     sudo apt install docker.io -y
     sudo apt install docker-compose -y
     sudo apt install git -y
     sudo systemctl enable docker
     sudo systemctl start docker
     sudo usermod -a -G docker ubuntu
  3. Instalar la libreria de python pika. ( pip3 install pika ) 
  4. Instalar la libreria de python json. ( pip3 install json ) 
  5. Instalar la libreria de python os. ( pip3 install pika ) 
  6. Instalar la libreria grpcio con la utilidad grpcio-tools ( pip3 install grpcio grpcio-tools )
 
Para ejecutarlo por primera vez se siguen los pasos a continuación:
   1.Estar posicionado en el directorio del proyecto que es 'st0263-jaramirezj/reto2'.
   1.Asegurarse de que todas las reglas de entrada esten configuradas correctamente. Esto se especifica en la sección Detalles Técnicos.
   2. En el directorio del proyecto ejecute este comando para montar el servidor de RabbitMQ:
   docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-   management 
   3. Ingresar a la dirección http://IP:15672, esto lo llevará al panel de administración de rabbitmq, ingrse con user = user y password=password. Luego
      ingrese a la subpagina exchange y cree un nuevo exchange con el nombre 'file_listing'. Luego vaya a la subpagina Queues y cree dos colas de
      tipo 'Classic' con los nombres 'request_files' y 'receive_files'. A continuación regrese a la subpágina de exchange e ingrese a el exchange 'file_listing'
      que creamos anteriormente, dirijase a la parte inferior y donde dice bind hay que asociar las dos colas que creamos a este exchange. Para esto debe
      escribir el nombre de la cola y la routing key. Para 'request_files' routing_key='request' y para 'receive_files' routing_key='receive'
 A partir de aquí se haria cada vez que se quiere ejecutar de nuevo el proyecto
   4. Ejecutar el comando: docker start rabbit-server
   5. Luego se abre 3 terminales en ingrese a la carpeta del proyecto,posteriormente ejecute lo siguiente:
      5.1. En la primera terminal ingrese a la ruta /microservice1 y ejecute 'python3 ms1_mom.py'. Con esto ya tenemos funcionando 
      el microservicio 1.
      5.2. En la segunda terminal ingrese a la ruta /grpc_client y ejecute 'python3 ms2_grpc.py'. Con esto ya tenemos funcionando 
      el microservicio 2.
      5.3. En la tercera terminal ejecute 'python3 server.py' para que se ejecute la API.
 En este punto ya se tendria todo listo, y se podria empezar a hacer peticiones a la API.


##Detalles del desarrollo

Durante el desarrollo se me presentaron varios problemas que tarde mucho en resolver, con lo que el proyecto tomó más tiempo de desarrolo que
lo esperado. Inicialmente empecé programando el MOM para lo que utilicé el tutorial de RabbitMQ como punto de partida, la primera vez que lo
intenté hacer no funcionó, pero después de cierto tiempo pude settear correctamente mi máquina virtual en amazon y ejecutarlo. Luego pasé a hacer
que el microservicio devolviera una respuesta,no sin antes tener varios problemas en los que se destaca }ue no se devolvia un mensaje o se devolvia 
el mismo mensaje que se enviaba. Al final logré hacer que el microservicio devolviera un json con los archivos listados, con lo que tenia la primera
parte del proyecto finalizada. 
Posteriormente puse manos a la obra en hacer el API Gateway, este aparentemente fue fácil de hacer, con la excepciónd de que al principio no lo estaba
configurando bien para que escuchara peticiones de IPs externas, y ademas no habia configurado una regla de entrada para la instancia EC2 para que 
escuchara de IPs externas por este puerto. 
Luego procedí a desarrollar el microservicio y la comunicación con gRPC, esto fue lo que menos tiempo me tomó a pesar de que de nuevo me enfrenté a multiples 
errores y problemas con instalaciones, inclusiones, nombres y otras cosas.
Finalmente hice unos scripts de shell para que se instalaran las dependencias necesarias y se setteara el ptoyecto completo sin necesidad de tener que 


## Detalles técnicos

Hay que configurar las reglas de entrada para la instancia EC2, para que la comunicación se por los puertos se de sin problemas. 
A continuación se muestra como están configuradas las reglas de entrada:
    ![image](https://user-images.githubusercontent.com/57159295/222557811-ee45f35e-d8f1-4345-bd2a-19b99e8881b7.png)
Nota: Tenga en cuenta que si modifica los puertos en los archovos de configuración, deberá por ende modificar las
reglas de entrada.

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

Para configurar los parametros con los que se va a ejecutar el proyecto se tiene un archivo de configuración por cada nodo en el proyecto que
recibe o envia datos. Por ejemplo para la api se tiene un archivo llamado api_config.py en donde se ponen parametros básicos como puerto y host.
De la misma forma cada microservicio tiene su archivo de configuración, al igual que los clientes que solicitan recursos a los microservicios.
Configuración de un microservicio:
   ![image](https://user-images.githubusercontent.com/57159295/222545629-f78550dd-8861-4cc5-a883-1c60cc58753c.png)


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 
Los archivos más importantes del proyecto son 'server.py' que contiene la API, los archivos mom/mom.py y grpc_client/grpc_c.py que 
permiten establecer comunicación con los microservicios(Clientes). Y los archivos microservice1/ms1_mom.py y grpc_client/ms2_grpc.py que son
los que contienen el codigo de los microservicios.
![image](https://user-images.githubusercontent.com/57159295/222546363-0aaf4c82-1c02-4905-8192-aeed1cf697fd.png)


## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## Descripción y como se configura los parámetros del proyecto
Para configurar los parametros del proyecto se debe ingresar a los archivos de configuración que cada nodo tiene.

## como se lanza el servidor.
Para lanzar el servidor 

## Un mini guia de como un usuario utilizaría el software o la aplicación
Un usuario podría utilizar la aplicación mediante POSTMAN o similares, o desde una terminal.
Para POSTMAN simplemente seria configurar el tipo de petición cómo GET y poner la dirección del proyecto, 
en este caso http://IP:5000/api?list , también podria ser http://IP:5000/api?list=.txt o http://IP:5000/api?list=.py
Desde la terminal podriamos ejecutar el comando curl así: curl -X GET  http://IP:5000/api?list=.txt

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. Otra información que considere relevante para esta actividad.

# referencias:
## Codigo de Edwin Montoya - Profesor
       https://github.com/st0263eafit/st0263-231/tree/main/rabbitmq-python
## Quickstart - Oficial Flask documentation
      https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
## Oficial RabbitMQ documentation
      https://www.rabbitmq.com/getstarted.html
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2023-Marzo)
