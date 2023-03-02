# info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiante(s): Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# <para borrar: EL OBJETIVO DE ESTA DOCUMENTACÍON ES QUE CUALQUIER LECTOR CON EL REPO, EN ESPECIAL EL PROFESOR, ENTIENDA EL ALCANCE DE LO DESARROLLADO Y QUE PUEDA REPRODUCIR SIN EL ESTUDIANTE EL AMBIENTE DE DESARROLLO Y EJECUTAR Y USAR LA APLICACIÓN SIN PROBLEMAS>

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

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
   Para desarrollar el

## como se compila y ejecuta.
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
