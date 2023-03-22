# Info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiante: Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Wordpress con NGINX, NFS server y MySQL 
#

## 1. 
En esta actividad se realizó el desarrollo y montaje de una arquitectura wordpress con 5 componentes, que son:
  
  - Un servidor con balanceador de carga NGINX que balancea entre dos instancias wordpress.
  - Dos servidores con instancias de wordpress, o mejor se pueden ver como dos instancias de wordpress que interpretan el wordpress,
    ya que realmente los archivos de wordpress y la base de datos están en otros servidores.
  - Un servidor con una base de datos de wordpress.
  - Un servidor NFS para los ficheros del wordpress que corren en las maquinas mencionadas anteriormente.
  - 
 Además de esto es importante mencionar que se utilizó docker para poner en contenedores la mayoria de las componentes
 anteriormente mencionadas.
 
 Por otro lado se tiene un dominio y un DNS que apunta a la IP del nginx. De forma adicional se obtuvieron los certificados ssl
 para permitir la conexion por https.
 Para resumir lo logrado en el reto: Tenemos que hay un nombre de dominio con un DNS que apunta a la instancia que corre el NGINX,este
 balancea la carga  entre dos servidores que corren wordpress pero que no tienen los archivos de este en local, sino que estos se encuentran
 en otra instancia que corre un servidor NFS y sirve esos archivos a las dos instancias. Finalmente este wordpress hace uso de una base de datos 
 wordpress que está en otra instancia de GCP.
 Del lado del usuario final lo que se tiene es que se  puede acceder al enlace julianrjdev.site a través de https.
 
 
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 Los aspectos propuestos por el profesor eran implementar la arquitectura con 5 servidores dockerizando algunos de los componentes. Además 
 de esto el reto también exigia obtener un nombre de dominio y obtener los certificados ssl para este. Todos estos aspectos se cumplieron
 y se puede acceder a la pagina perfectamente.
 Por el lado de los no funcionales se cumplió con el hecho de que estos servidores se desplegaron en instancias de GCP.
 Otro requerimiento cumplido es que todos los servicios se levantan al iniciar la instancia.
 
# 2. Información general de diseño de alto nivel y arquitectura

   ![reto3](https://user-images.githubusercontent.com/57159295/227046402-29a4d279-4f71-4d06-b231-bc991c8505c1.png)
   
   Como se puede ver en la imagen, la arquitectura del proyecto consta de 5 nodos que corresponden a instancias e2.micro de Google Cloud Platform con Ubuntu 22.04
   instalado en cada uno de ellas y adicionalmente una parte de DNS administrado por un proveedor externo como lo es Hostinger. En cuanto al Hostinger, en 
   este se tiene el nombre de dominio y los servidores con los registros DNS que permiten administrar la zona, claramente uno de esos registros apunta a la
   máquina en que está corriendo el NGINX.  La máquina que corre el NGINX actúa como balanceador de carga para las peticiones que llegan a través del DNS, en este
   segmento del proyecto fue muy importante obtener los certificados ssl a través de certbot y configurar correctamente NGINX para que todo el trafico sea
   a través de HTTPS. Este NGINX balancea la carga de trabajo a dos instancias con wordpress dockerizado, y a su vez ambas instancias se sirven de una 
   instancia que corre la base de datos MySQL y de otra instancia con un servidor NFS de Ubuntu.

# 3. Descripción del ambiente de desarrollo y técnico

   - Para desarrollar el proyecto se hizo uso de instancias de GCP e2.micro con 10GB de almacenamiento.
   - En cada instancia de GCP se instaló el sistema operativo Ubuntu 22.04, gracias a su buena compatibilidad y facilidad
     para manejar los componentes utilizados en el proyecto.
   - Para desarrollar el proyecto se utilizó en gran medida docker, para dockerizar la mayoria de los componentes.
   - Para desarrollar el proyecto se utilizó WordPress y MySQL.
   - Para crear los directorios compartidos se utilizó un servidor NFS de Ubuntu.
     como la comunicación con los microservicios y los mismos microservicios.
   - Para obtener los certificados ssl se hizo uso de certbot.
   - Para realizar el balanceador de carga se hizo uso de NGINX.

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
  5. Instalar la libreria de python os. ( pip3 install os ) 
  6. Instalar la libreria grpcio con la utilidad grpcio-tools ( pip3 install grpcio grpcio-tools )
 
Para ejecutarlo por primera vez se siguen los pasos a continuación(En un entorno de desarrollo):

   1.Estar posicionado en el directorio del proyecto que es 'st0263-jaramirezj/reto2'.
   
   1.Asegurarse de que todas las reglas de entrada esten configuradas correctamente. Esto se especifica en la sección Detalles Técnicos.
   
   2. En el directorio del proyecto ejecute este comando para montar el servidor de RabbitMQ:
   docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-   management 
   
   3. Ingresar a la dirección http://IP:15672, esto lo llevará al panel de administración de rabbitmq, ingree con user = user y password=password. Luego
      ingrese a la subpagina exchange y cree un nuevo exchange con el nombre 'file_listing'. Luego vaya a la subpagina Queues y cree dos colas de
      tipo 'Classic' con los nombres 'request_files' y 'receive_files'. A continuación regrese a la subpágina de exchange e ingrese a el exchange 'file_listing'
      que creamos anteriormente, dirijase a la parte inferior y donde dice bind hay que asociar las dos colas que creamos a este exchange. Para esto debe
      escribir el nombre de la cola y la routing key. Para 'request_files' routing_key='request' y para 'receive_files' routing_key='receive'
   
   4. En caso de que aún no se haya compilado el archivo service.proto(Ya estan incluidos los archivos compilados en el repositorio), se debe 
    ejecutar el siguiente: python3 -m grpc_tools.protoc -I ./grpc_client --python_out=. \ --grpc_python_out=. ./service.proto
   
   5. Ejecutar el comando: docker start rabbit-server
  
   6. Luego se abre 3 terminales en ingrese a la carpeta del proyecto,posteriormente ejecute lo siguiente:
     
     6.1. En la primera terminal ingrese a la ruta /microservice1 y ejecute 'python3 ms1_mom.py'. Con esto ya tenemos funcionando 
      el microservicio 1.
      
      6.2. En la segunda terminal ingrese a la ruta /grpc_client y ejecute 'python3 ms2_grpc.py'. Con esto ya tenemos funcionando 
      el microservicio 2.
      
      6.3. En la tercera terminal ejecute 'python3 server.py' para que se ejecute la API.
     
 En este punto ya se tendria todo listo, y se podria empezar a hacer peticiones a la API.
 
 En la sección de como se lanzan los servidores en el ambiente de ejecución, se ilustra una forma mejor y más rapida de poner
 todo a funcionar luego de que ya se han hecho las configuraciones iniciales


## Detalles del desarrollo

Durante el desarrollo se me presentaron varios problemas que tarde mucho en resolver, con lo que el proyecto tomó más tiempo de desarrollo de
lo esperado. Inicialmente empecé programando el MOM para lo que utilicé el tutorial de RabbitMQ como punto de partida, la primera vez que lo
intenté hacer no funcionó, pero después de cierto tiempo pude descubrir que el error era que estaba usando la misma routing key para las dos colas. 
Posterior a esto pude settear correctamente mi máquina virtual en amazon y ejecutar la comunicación por RabbitMQ. Luego pasé a hacer
que el microservicio devolviera una respuesta, no sin antes tener varios problemas en los que se destaca que no se devolvia un mensaje o se devolvia 
el mismo mensaje que se enviaba. Al final logré hacer que el microservicio devolviera un json con los archivos listados, con lo que tenia la primera
parte del proyecto finalizada. 
Posteriormente puse manos a la obra en hacer el API Gateway, este aparentemente fue fácil de hacer, con la excepción de que al principio no lo estaba
configurando bien para que escuchara peticiones de IPs externas, y ademas no habia configurado una regla de entrada para la instancia EC2 para que 
escuchara de IPs externas por este puerto. 
Luego procedí a desarrollar el microservicio y la comunicación con gRPC, esto fue lo que menos tiempo me tomó a pesar de que de nuevo me enfrenté a multiples 
errores y problemas con instalaciones, inclusiones, nombres y otras cosas.
Luego hice unos scripts de shell para que se instalaran las dependencias necesarias y se setteara el ptoyecto completo sin necesidad de tener que 
entrar a la consola. Y por ultimo programe un servicio del sistema para que se lanzen todos los servidores al iniciar


## Detalles técnicos

Hay que configurar las reglas de entrada para la instancia EC2, para que la comunicación por los puertos se de sin problemas. 
A continuación se muestra como están configuradas las reglas de entrada:
    ![image](https://user-images.githubusercontent.com/57159295/222557811-ee45f35e-d8f1-4345-bd2a-19b99e8881b7.png)
Nota: Tenga en cuenta que si modifica los puertos en los archovos de configuración, deberá por ende modificar las
reglas de entrada.

## Descripción y como se configura los parámetros del proyecto

Para configurar los parametros con los que se va a ejecutar el proyecto se tiene un archivo de configuración por cada nodo en el proyecto que
recibe o envia datos. Por ejemplo para la api se tiene un archivo llamado api_config.py en donde se ponen parametros básicos como puerto y host.
De la misma forma cada microservicio tiene su archivo de configuración, al igual que los clientes que solicitan recursos a los microservicios.
.
Configuración de un microservicio:
   ![image](https://user-images.githubusercontent.com/57159295/222545629-f78550dd-8861-4cc5-a883-1c60cc58753c.png)


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 
Los archivos más importantes del proyecto son 'server.py' que contiene la API, los archivos mom/mom.py y grpc_client/grpc_c.py que 
permiten establecer comunicación con los microservicios(Clientes). Y los archivos microservice1/ms1_mom.py y grpc_client/ms2_grpc.py que son
los que contienen el codigo de los microservicios.
![image](https://user-images.githubusercontent.com/57159295/222546363-0aaf4c82-1c02-4905-8192-aeed1cf697fd.png)


## Resultados o pantallazos (En desarollo)

A continuación se muestran los servicios funcionando:

Servidor(API) funcionando:
![image](https://user-images.githubusercontent.com/57159295/222574650-3b0ded24-4c08-4b40-932e-296d21f33815.png)

Microservicio 1 Funcionando:
![image](https://user-images.githubusercontent.com/57159295/222574724-cac070b8-83f8-45d8-bd26-8b1bcdcdfd53.png)

Microservicio 2 Funcionando:
![image](https://user-images.githubusercontent.com/57159295/222574798-63e149d9-f4ae-48a2-ad99-ea3aaa9d896d.png)


# 4. Descripción del ambiente de EJECUCIÓN (en producción)

# IP o nombres de dominio en nube o en la máquina servidor.

Para que se puedan hacer peticiones al la API sin necesidad de volver a consultar la IP de la instancia EC2, 
la IP de la máquina se fijó a través de una IP elastica, esta es: 44.213.230.177, además se debe tener en cuenta que
para conectarse a la api se tiene que usar el puerto '5000' e interiormente la api está configurada para funcionar sobre la
dirección '/api?list', donde list puede enviarse sin parametros o con un parametro del tipo '.txt' o '.py'.
Una dirección completa para conectarse a la api sería '44.213.230.177:5000/api?list=.txt'

## Como se lanza el servidor.

Para lanzar el servidor y los microservicios luego de que todo se haya configurado todo, dirijase al
directorio del proyecto y ejecute el comando './start_servers.sh'. Este archivo pondrá a funcionar el proyecto.
En este script se encuentra el siguiente código:

    docker start rabbit-server
    python3 microservice1/ms1_mom.py &
    sleep 0.2
    python3 grpc_client/ms2_grpc.py &
    sleep 0.2
    python3 server.py &
    
Para evitar tener que hacer estos pasos de manera manual, se tiene una forma alternativa que lo que hace es 
ejecutar el script anterior cuando se inicia la instancia. Esto se logra a partir
de crear un archivo .service en la carpeta /etc/systemd/system , que contiene el siguiente código:

    [Unit]
    Description=Start servers
    [Service]
    Type=simple
    ExecStart=/home/ubuntu/st0263-jaramirezj/reto2/start_servers.sh
    [Install]
    WantedBy=multi-user.target



## Guia de como un usuario utilizaría el software o la aplicación

Un usuario podría utilizar la aplicación mediante POSTMAN o similares, o desde una terminal.
Para POSTMAN simplemente seria configurar el tipo de petición cómo GET y poner la dirección del proyecto, 
en este caso http://IP:5000/api?list , también podria ser http://IP:5000/api?list=.txt o http://IP:5000/api?list=.py
Desde la terminal podriamos ejecutar el comando curl así: curl -X GET  http://IP:5000/api?list=.txt

## Resultados o pantallazos (En producción)

Ejecución de solicitud GET desde la misma máquina:
![image](https://user-images.githubusercontent.com/57159295/222576023-46c1df0a-e0dc-4e7d-8c8e-b2ad1b5563a7.png)

Ejecución desde POSTMAN y un IP externa:
Petición simple
![image](https://user-images.githubusercontent.com/57159295/222915689-61cda0d6-b7a2-410c-b857-934cc5d8e860.png)

Petición para buscar un tipo de archivo especifico(.txt)
![image](https://user-images.githubusercontent.com/57159295/222916140-cb488173-ec07-4d41-9798-73d7309c2c58.png)

Petición para buscar un tipo de archivo especifico(.py)
![image](https://user-images.githubusercontent.com/57159295/222973420-0ee03303-92dd-48aa-b8d9-af5391f9a82f.png)


# referencias:
## Codigo de Edwin Montoya - Profesor
       https://github.com/st0263eafit/st0263-231/tree/main/rabbitmq-python
## Quickstart - Oficial Flask documentation
      https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
## Oficial RabbitMQ documentation
      https://www.rabbitmq.com/getstarted.html

#### versión README.md -> 1.0 (2023-Marzo)
