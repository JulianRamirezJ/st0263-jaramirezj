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

Para obtener los certificados SSL se ha utilizado certbot, y para realizar el balanceador de carga se ha utilizado el servicio de balanceo de carga de GCP. De esta manera, se asegura una distribución eficiente de la carga de trabajo entre los servidores.

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
Descripción de la arquitectura

## 3. Descripción del ambiente de desarrollo y técnico

- Para implementar el proyecto se han utilizado instancias de GCP e2.micro con 10GB de almacenamiento, lo que ha permitido tener un entorno de desarrollo escalable y rentable.
- Se ha instalado el sistema operativo Ubuntu 22.04 en cada instancia, ya que este sistema operativo es altamente compatible y fácil de manejar con los componentes utilizados en el proyecto.
- Docker ha sido una herramienta fundamental en el proyecto, ya que se ha utilizado para dockerizar los componentes de moodle, lo que ha permitido un despliegue más eficiente y escalable.
- Moodle ha sido el CMS seleccionado para implementar el proyecto, lo que ha permitido desarrollar un sitio web altamente funcional y escalable para la gestión del VPL.
- Para la persistencia de los datos se ha hecho uso de los servicios de GCP Cloud SQL, que ofrece una solución de base de datos escalable y altamente disponible.
- Para la creación de los directorios compartidos se ha utilizado Google Cloud Filestore, que proporciona compatibilidad con el protocolo NFSv3 y acceso seguro a los archivos.
- La obtención de los certificados SSL se ha llevado a cabo utilizando Certbot, una herramienta gratuita y de código abierto que automatiza la obtención y renovación de certificados SSL.
- Para la implementación del balanceador de carga se ha hecho uso de Google Cloud Load Balancing, un servicio administrado que proporciona un enrutamiento inteligente del tráfico y la distribución de carga entre múltiples instancias de backend en diferentes regiones.
# Como se compila y ejecuta.

## 4. Como se compila y ejecuta
Para desarrollar, compilar y ejecutar el proyecto se siguieron los pasos listados a continuación.
 
 1. Crear una instancia de Cloud SQL
 2. 


## 5. Detalles del desarrollo

......

## 6. Detalles técnicos

Al crear las máquinas en GCP con Ubuntu 22 hay que permitir trafico http y https(Para el NGINX).


## 7. Descripción y como se configura los parámetros del proyecto

Para configurar los parametros del proyecto se tienen una env_file.txt con las ips y puertos
para docker, si necesita cambiar algo simplemente especifiquelo ahi.
Para los demás componentes las configuraciones de parametros }se hacen como se presentaron en la guia.


## 8. ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 


## 9. Descripción del ambiente de EJECUCIÓN (en producción)

## 10. IP o nombres de dominio en nube o en la máquina servidor.

Para que se pueda acceder al proyecto sin necesidad de memorizarse una IP especifica se tiene un nombre 
de dominio, que en este caso es julianrjdev.site o www.julianrjdev.site, esto redireccionará por defecto
a https://julianrjdev.site

## 11. Como se lanza el servidor.

Después de la configuración inicial los servicios tanto de NGINX como de Docker se levantan automaticamente
al iniciar la máquina por lo que no se necesita ejecutar nada.


## 12. Guia de como un usuario utilizaría el software o la aplicación



# 13. Referencias:
## Guia y comandos de Edwin Montoya - Profesor
      https://github.com/st0263eafit/st0263-231/tree/main/docker-nginx-wordpress-ssl-letsencrypt
## How To Set Up an NFS Mount on Ubuntu 22.04
      https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04
## certbot instructions (Certbot with NGINX and Ubuntu)
      https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

#### versión README.md -> 1.0 (2023-Marzo)
