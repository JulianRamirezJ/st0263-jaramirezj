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

El sitio se ha implementado en dos servidores que alojan instancias de Moodle en contenedores Docker. Estas instancias pueden crecer según las necesidades de los usuarios y no incluyen el sistema de archivos de Moodle ni la base de datos, ya que estos están alojados en servicios remotos de GCP.

Para la persistencia de la base de datos de Moodle, se ha utilizado una instancia de SQL en GCP. Además, se ha utilizado una instancia del servicio X de GCP como NFS para almacenar los archivos de Moodle.

Se ha configurado un dominio y un DNS para apuntar al LB, lo que permite que los usuarios accedan al sitio a través del enlace reto4.julianrjdev.site con conexión HTTPS, gracias a los certificados SSL obtenidos.

En resumen, se ha implementado un sitio Moodle altamente disponible utilizando servicios administrados en GCP, lo que asegura la escalabilidad, disponibilidad y seguridad del sitio para los usuarios finales.

 Del lado del usuario final lo que se tiene es que se  puede acceder al enlace reto4.julianrjdev.site a través de https.
 
 
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 Los aspectos propuestos por el profesor eran implementar la arquitectura con alta disponibilidad de Moodle que incluya servicios administrados. Además 
 de esto el reto también exigia obtener un nombre de dominio y obtener los certificados ssl para este. Todos estos aspectos se cumplieron
 y se puede acceder a la pagina perfectamente.
 Por el lado de los no funcionales se cumplió con el hecho de que se hizo uso de servicios propios de GCP para la base de datos, el nfs, el 
 balanceador y el autoscaling.
 
 ## 1.2. Que aspectos no cumplió o no desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 En general se cumplieron practicamente todos los aspectos propuestos.
 
# 2. Información general de diseño de alto nivel y arquitectura


# 3. Descripción del ambiente de desarrollo y técnico

   - Para desarrollar el proyecto se hizo uso de instancias de GCP e2.micro con 10GB de almacenamiento.
   - En cada instancia de GCP se instaló el sistema operativo Ubuntu 22.04, gracias a su buena compatibilidad y facilidad
     para manejar los componentes utilizados en el proyecto.
   - Para desarrollar el proyecto se utilizó docker, para dockerizar la mayoria de los componentes.
   - Para desarrollar el proyecto se utilizó Moodle.
   - Se hizo uso de los servicios de GCP SQL ........,
   - Para crear los directorios compartidos se utilizó ...
   - Para obtener los certificados ssl se hizo uso de certbot.
   - Para realizar el balanceador de carga se hizo uso de .......

# Como se compila y ejecuta.

Para compilar y ejecutar el proyecto se siguieron los pasos listados a continuación.


## Detalles del desarrollo

......
## Detalles técnicos

Al crear las máquinas en GCP con Ubuntu 22 hay que permitir trafico http y https(Para el NGINX).


## Descripción y como se configura los parámetros del proyecto

Para configurar los parametros del proyecto se tienen una env_file.txt con las ips y puertos
para docker, si necesita cambiar algo simplemente especifiquelo ahi.
Para los demás componentes las configuraciones de parametros }se hacen como se presentaron en la guia.


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 


# 4. Descripción del ambiente de EJECUCIÓN (en producción)

# IP o nombres de dominio en nube o en la máquina servidor.

Para que se pueda acceder al proyecto sin necesidad de memorizarse una IP especifica se tiene un nombre 
de dominio, que en este caso es julianrjdev.site o www.julianrjdev.site, esto redireccionará por defecto
a https://julianrjdev.site

## Como se lanza el servidor.

Después de la configuración inicial los servicios tanto de NGINX como de Docker se levantan automaticamente
al iniciar la máquina por lo que no se necesita ejecutar nada.


## Guia de como un usuario utilizaría el software o la aplicación



# referencias:
## Guia y comandos de Edwin Montoya - Profesor
      https://github.com/st0263eafit/st0263-231/tree/main/docker-nginx-wordpress-ssl-letsencrypt
## How To Set Up an NFS Mount on Ubuntu 22.04
      https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04
## certbot instructions (Certbot with NGINX and Ubuntu)
      https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

#### versión README.md -> 1.0 (2023-Marzo)
