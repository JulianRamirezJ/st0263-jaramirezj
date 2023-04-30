# Info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiantes:
## Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
## Samuel David Villegas Bedoya, sdvillegab@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Moodle con alta disponibilidad y servicios de GCP. 
#

## 1. Descripción del proyecto

En esta actividad se ha desarrollado y montado un sitio Moodle con alta disponibilidad utilizando servicios administrados en Google Cloud Platform (GCP). El sitio cuenta con un balanceador de carga (LB) y un autoescaler que aseguran que los recursos sean asignados según las necesidades de los usuarios.

Se han utilizado instancias de GCP e2.micro con 10GB de almacenamiento, en las cuales se instaló el sistema operativo Ubuntu 22.04. Para dockerizar la mayoría de los componentes se ha utilizado Docker, y para desarrollar el proyecto se ha utilizado Moodle.

Para la persistencia de la base de datos de Moodle, se ha utilizado una instancia de SQL en GCP. Además, se ha utilizado el servicio administrado de NFS de GCP para crear los directorios compartidos y almacenar los archivos de Moodle.

Para obtener los certificados SSL se han utilizado los que porvee Google y para realizar el balanceador de carga se ha utilizado el servicio de balanceo de carga de GCP. De esta manera, se asegura una distribución eficiente de la carga de trabajo entre los servidores.

Se ha configurado un dominio y un DNS para apuntar al LB, lo que permite que los usuarios accedan al sitio a través del enlace reto4.julianrjdev.site con conexión HTTPS.

En resumen, se ha implementado un sitio Moodle altamente disponible utilizando servicios administrados en GCP, lo que asegura la escalabilidad, disponibilidad y seguridad del sitio para los usuarios finales. Del lado del usuario final, se puede acceder al enlace reto4.julianrjdev.site a través de HTTPS.
 
 
### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

El desafío planteado por el profesor consistía en implementar una arquitectura de alta disponibilidad para Moodle, haciendo uso de servicios administrados. Además, se requería obtener un nombre de dominio y certificados SSL para asegurar la conexión segura a la página.
Estos requisitos se han cumplido satisfactoriamente y ahora es posible acceder a la página sin ningún problema. En cuanto a los aspectos no funcionales, se ha logrado cumplir con la premisa de utilizar exclusivamente servicios nativos de Google Cloud Platform para la base de datos, el NFS, el balanceador y el autoescalamiento.

En definitiva, se ha logrado implementar una solución robusta y escalable para Moodle, haciendo uso de servicios gestionados y asegurando la disponibilidad, seguridad y eficiencia del sitio web.

 ### 1.2. Que aspectos no cumplió o no desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 En general se cumplieron practicamente todos los aspectos propuestos.
 
## 2. Información general de diseño de alto nivel y arquitectura
![Reto4Arquitectura](https://user-images.githubusercontent.com/57159295/234411215-8416c54e-d745-4544-ae2b-cb624c5d565e.png)

La arquitectura del proyecto se compone de cinco componentes esenciales, tal como se ilustra en la imagen anterior. El punto de entrada es el DNS, administrado por Hostinger, donde se aloja el dominio. A continuación, en el siguiente nivel de la arquitectura, se encuentra el balanceador de carga provisto por GCP, llamado Cloud Load Balancing. Este balanceador distribuye la carga a dos o más instancias de Moodle según la necesidad, ya que se cuenta con configuración de autoscaling en función del tráfico.

En el siguiente nivel de la arquitectura, se encuentran las instancias de Moodle que están montadas sobre Docker y se ejecutan sobre instancias de Compute Engine. Estas instancias de Moodle no tienen el sistema de archivos de Moodle ni la base de datos alojados localmente, sino que se encuentran en servicios separados que se describen a continuación. La base de datos que sirve a Moodle se encuentra alojada en una instancia de Cloud SQL, mientras que el sistema de archivos de Moodle se aloja en un directorio compartido en Cloud Filestore.

## 3. Descripción del ambiente de desarrollo y técnico

- Para implementar el proyecto se han utilizado instancias de GCP e2.micro con 10GB de almacenamiento, lo que ha permitido tener un entorno de desarrollo escalable y rentable.
- Se ha instalado el sistema operativo Ubuntu 22.04 en cada instancia, ya que este sistema operativo es altamente compatible y fácil de manejar con los componentes utilizados en el proyecto.
- Docker ha sido una herramienta fundamental en el proyecto, ya que se ha utilizado para dockerizar los componentes de moodle, lo que ha permitido un despliegue más eficiente y escalable.
- Moodle ha sido el CMS seleccionado para implementar el proyecto, lo que ha permitido desarrollar un sitio web altamente funcional y escalable para la gestión del VPL.
- Para la persistencia de los datos se ha hecho uso de los servicios de GCP Cloud SQL, que ofrece una solución de base de datos escalable y altamente disponible.
- Para la creación de los directorios compartidos se ha utilizado Google Cloud Filestore, que proporciona compatibilidad con el protocolo NFSv3 y acceso seguro a los archivos.
- La obtención de los certificados SSL se ha llevado a cabo utilizando los que provee Google, lo que permitió la generación y uso de estos de una forma rapida y confiable.
- Para la implementación del balanceador de carga se ha hecho uso de Google Cloud Load Balancing, un servicio administrado que proporciona un enrutamiento inteligente del tráfico y la distribución de carga entre múltiples instancias de backend en diferentes regiones.

## 4. Como se compila y ejecuta
Para desarrollar, compilar y ejecutar el proyecto, se siguieron los siguientes pasos:

1. Se creó una instancia de Filestore con las siguientes configuraciones:
- Tipo de Básica
- HDD

2. Se creó una instancia de Cloud SQL de MySQL con los recursos mínimos posibles, y se estableció el grupo de seguridad por defecto para conexiones en el mismo entorno.

3. Se creó una base de datos llamada "bitnami_moodle".

4. Se levantó una instancia de prueba para montar datos en la base de datos y en el NFS utilizando el siguiente script:

```docker
#! /bin/bash
sudo apt-get -y update &&
sudo apt-get install nfs-common -y
sudo mkdir -p $HOME/mnt/moodle
sudo mount 10.73.129.2:/moodle /mnt/moodle
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
sudo systemctl enable docker
sudo systemctl start docker
git clone https://github.com/JulianRamirezJ/st0263-jaramirezj.git
cd st0263-jaramirezj/reto4/moodle-instance 
sudo docker-compose -f docker-compose.yml up -d
```

Antes de levantar el "docker-compose", se debe cambiar la propiedad "MOODLE_SKIP_BOOTSTRAP" por "no" para que haga el bootstrap inicial.

5. Se creó un template de instancia de Compute Engine con las siguientes características:
- Ubuntu 22.04
- e2-micro
- Se habilitó HTTP
- Grupo de seguridad default

En el "start up" script se incluyó lo siguiente:

```bash
#! /bin/bash
sudo apt-get -y update &&
sudo apt-get install nfs-common -y
sudo mkdir -p $HOME/mnt/moodle
sudo mount 10.73.129.2:/moodle /mnt/moodle
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
sudo systemctl enable docker
sudo systemctl start docker
git clone https://github.com/JulianRamirezJ/st0263-jaramirezj.git
cd st0263-jaramirezj/reto4/moodle-instance 
sudo docker-compose -f docker-compose.yml up -d
```

6. Se creó un grupo de instancias con autoscaling con las siguientes características:
- Se eligió el template de instancia previamente creado.
- Zona única (us-east1)
- Número mínimo de instancias: 2
- Número máximo de instancias: 6

Se agregó un health check, pero no es necesario para el montado.

7. Se creó el balanceador de cargas:
 - Se eligió Balanceo de cargas HTTP(S)
 - Se eligió De Internet a mis VMs o servicios sin servidores
 - Se eligió Balanceador de cargas HTTP(S) global (clásico)
 -  Se creó el backend, eligiendo el grupo de instancias creadas en el punto anterior.
 - Se creó el frontend, utilizando el protocolo HTTPS, creando una IP o eligiendo una existente, creando un certificado con GCP referenciado al dominio "reto4.samuelvillegas.online" y habilitando la redirección automática http - https.

8. Finalmente el DNS se asoció la IP del frontend del balanceador y se creó el subdominio correspondiente.

## 5. Detalles del desarrollo

El desarrollo se hizo de una forma ágil y eficiente gracias al trabajo en equipo de dos personas. Inicialmente, se realizaron pruebas con una arquitectura monolítica de Moodle que permitieron entender el funcionamiento del sistema y definir los siguientes pasos.
Luego, se procedió a implementar la base de datos en Cloud SQL y conectarla con el Moodle. 
Posteriormente, se configuró Cloud Filestore para alojar el sistema de archivos de Moodle y al mismo tiempo se hizo el cambio de almacenamiento local
del Moodle a almacenamiento en File Store
Después de tener la base de datos y el sistema de archivos en servicios administrados de GCP, se procedió a configurar el Load Balancing y el autoscaling en GCP, lo que permitió tener un sitio Moodle altamente disponible y escalable en función de la demanda de los usuarios.
Finalmente, se configuró el DNS con certificados SSL obtenidos a través de Certbot, lo que permitió tener un sitio seguro y accesible a través de HTTPS. En resumen, se logró implementar un sitio Moodle altamente disponible, escalable y seguro, utilizando servicios administrados en GCP.

## 6. Detalles técnicos

Teniendo en cuenta que todos estos servicios utilizados comsumen muchos creditos, se recomienda no tenerlos habilitados mientras
no se esten utilizando y elegir simempre las caracteristicas minimas.

Es importante tener un cuenta que antes de levantar el "docker-compose" en la instancia de prueba, se debe cambiar la propiedad "MOODLE_SKIP_BOOTSTRAP" por "no" para que haga el bootstrap inicial.


## 7. Descripción y como se configura los parámetros del proyecto

Para configurar los parametros del proyecto debe hacer todo el proceso descrito en eñl numeral #4 y configurar los diferentes
parametros según la necesidad. 

## 8. ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
file:///home/julianramirezj/Pictures/Screenshots/Screenshot%20from%202023-04-30%2012-26-18.png![image](https://user-images.githubusercontent.com/57159295/235367269-6c32d222-5ffd-4ef4-9ed3-04d04f7649ae.png)

Esta es la estructura de directorios basica para el proyecto, hay que tener en cuenta que dado que muchos de los servicios se deben configurar
manualmente no se tienen scripts para hacerlo, asi que como script solo se tiene el docker-compose para montar las instancias de moodle.

## 9. Descripción del ambiente de EJECUCIÓN (en producción)

En un navegador se ingresa a la URL o dominio del proyecto y se puede interactuar con la pagina de moodle.

## 10. IP o nombres de dominio en nube o en la máquina servidor.

Para que se pueda acceder al proyecto sin necesidad de memorizarse una IP especifica se tiene un nombre 
de dominio, que en este caso es .reto4.samuelvillegas.online, esto redireccionará por defecto
a https://reto4.samuelvillegas.online

## 11. Screenshots del proceso de montado
Creación filestore
![image](https://user-images.githubusercontent.com/57159295/235367471-4349e9b2-1bf6-4faa-aff4-ff12c722c429.png)

Creación Cloud SQL y base de datos
![image](https://user-images.githubusercontent.com/57159295/235367479-a7b641fb-383a-4260-a4d0-02b108e30e4e.png)

Montado de Bootstrap inicial a NFS y base de datos
![image](https://user-images.githubusercontent.com/57159295/235367484-a52059b3-ab56-47c2-8d1d-dd3fdb41053a.png)

Instancia de prueba conectada a BD y NFS
![image](https://user-images.githubusercontent.com/57159295/235367490-f1ac2eaf-ce60-40b3-b71f-bee4b92f7a28.png)

Instancia de template compute Engine
![image](https://user-images.githubusercontent.com/57159295/235367496-07850820-bd04-4a67-85ce-09379d014498.png)
![image](https://user-images.githubusercontent.com/57159295/235367505-775b4638-b5a4-40c8-bd4a-77900a89effb.png)

Grupo de instancia
![image](https://user-images.githubusercontent.com/57159295/235367511-7efd7b55-3186-4716-b675-36723b4d9bc6.png)

Balanceador
![image](https://user-images.githubusercontent.com/57159295/235367518-1844afab-8d59-438c-a601-2681166a4c15.png)

DNS
![image](https://user-images.githubusercontent.com/57159295/235367527-07c167ca-ae9c-407c-837d-8fcdfc297229.png)


## 12. Resultado final
Al final se tiene la aplicación de Moodle corriendo en un browser:
![image](https://user-images.githubusercontent.com/57159295/235367545-ecd01661-6586-4886-8252-fcda88973374.png)



# 13. Referencias:
## Guia y comandos de Edwin Montoya - Profesor
      https://github.com/st0263eafit/st0263-231/tree/main/docker-nginx-wordpress-ssl-letsencrypt

#### versión README.md -> 1.0 (2023-Marzo)
