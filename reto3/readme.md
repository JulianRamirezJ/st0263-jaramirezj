# Info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiante: Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Wordpress con NGINX, NFS server y MySQL 
#

## 1. Descripción del proyecto
En esta actividad se realizó el desarrollo y montaje de una arquitectura wordpress con 5 componentes, que son:
  
  - Un servidor con balanceador de carga NGINX que balancea entre dos instancias wordpress.
  - Dos servidores con instancias de wordpress, o mejor se pueden ver como dos instancias de wordpress que interpretan el wordpress,
    ya que realmente los archivos de wordpress y la base de datos están en otros servidores.
  - Un servidor con una base de datos de wordpress.
  - Un servidor NFS para los ficheros del wordpress que corren en las maquinas mencionadas anteriormente.
  
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
 
 ## 1.2. Que aspectos no cumplió o no desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 En general se cumplieron practicamente todos los aspectos propuestos.
 
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

# Como se compila y ejecuta.

Para compilar y ejecutar el proyecto se siguieron los pasos listados a continuación.
 
 Primero que todo cree 5 máquinas en GCP y clone el repositorio con los archivos del proyecto. Además posicionese
 en cada servidor en la carpeta que va a hacer uso. Ej: Para montar el servidor de base de datos pocisionarse en 'db_server'.
 A continuación siga los pasos para montar los servicios en cada máquina especifica.
 
  ## WordPress Servers:  
    En las maquinas que va a correr wordpress se debe ejecutar lo siguiente:
    1. Primero docker y git:
        sudo apt update
        sudo apt install docker.io -y
        sudo apt install docker-compose -y
        sudo apt install git -y
        sudo systemctl enable docker
        sudo systemctl start docker
        
    2. Luego montar el nfs:
        sudo apt update
        sudo apt install nfs-common
        sudo mkdir -p /var/www/html
        sudo mount {$nfs_server_ip}:/var/www/html /mnt/wordpress
        
    3. Montar el nfs en boot
       En el archivo
          sudo nano /etc/fstab
       Añadimos esta linea
           host_ip:/var/www/html    /mnt/wordpress  nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
       
    4.Asegurarse de que el puerto y la ip sea el indicado en la env_file.txt
    
    5. Finalmente ejecutamos el composer:
        sudo docker-compose -f docker-compose-solo-wordpress.yml up
    *Tenga en cuenta que para los pasos 2 y 4 es prerequisito tener corriendo la base de datos y el nfs.
    
   ## Wordpress DB
      En las maquina que va a correr la DB debe ejecutar lo siguiente:
      1.Docker y git de nuevo:
          sudo apt update
          sudo apt install docker.io -y
          sudo apt install docker-compose -y
          sudo apt install git -y
          sudo systemctl enable docker
          sudo systemctl start docker
        
      2.Asegurarse de que el puerto se el indicado en la env_file.txt
      
      3.Ejecutar el compose:
            docker-compose -f docker-compose-solo-wordpress-db.yml up
            
   ## NFS SERVER
     En las maquina que va a correr el NFS debe ejecutar lo siguiente:
     1.Instalamos.
        sudo apt update
        sudo apt install nfs-kernel-server
      
     2.Creamos el directorio a compartir y modificamos permisos
        sudo mkdir /var/www/html -p
        sudo chown nobody:nogroup /var/www/html
        
     3. Nos dirigimos a 'sudo nano /etc/exports' y añadimos las siguientes lineas con las IPs de los clientes wordpress:
          /var/www/html    client_ip1(rw,sync,no_subtree_check)
          /var/www/html    client_ip2(rw,sync,no_subtree_check)
          
     4.Recargamos y activamos ufw
        sudo systemctl restart nfs-kernel-server
        sudo ufw enable
      
     5. Finalmente permitimos el trafico hacia esas IPs
        sudo ufw allow from client_ip1 to any port nfs
       sudo ufw allow from client_ip2 to any port nfs
      
   ## NGINX
       En las maquina que va a correr el NGINX debe ejecutar lo siguiente:
       1.Instalamos.
           sudo apt update
           sudo add-apt-repository ppa:certbot/certbot
           sudo apt-get install certbot python3-certbot-nginx
           sudo apt install letsencrypt -y
           sudo apt install nginx -y
           
        2. Vamos a 'sudo nano st0263/reto3/proxy-lb/nginx.conf'
           Y debemos editar las IPs de las instancias de wordpress en esta sección:
               upstream wordpress_servers {
                  server 10.128.0.2;
                  server 10.128.0.5;
                }
                
        3. Creamos el siguiente directorio:
             sudo mkdir -p /var/www/letsencrypt
             
        3.Generamos el certificado para registros especificos(1) y para todo el dominio(2)
              (1) sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d julianrjdev.site --manual --preferred-challenges dns-01 certonly
              (2) sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.julianrjdev.site --manual --preferred-challenges dns-01 certonly
           *Para ambos casos seguir las intruscciones de generar un TXT en el dominio.
           
        4.Reemplazar estas rutas en nginx.conf con las de los cretificados generados.
            ssl_certificate /etc/letsencrypt/live/julianrjdev.site-0001/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/julianrjdev.site-0001/privkey.pem;
            
        5. Por ultimo recargamos nginx y ya estaria
           sudo service nginx reload
           
   ## DNS
     Consiga un nombre de dominio y configure los siguientes registros en el DNS:
       julianrjdev.site A @ ip_server 
        www CNAME julianrjdev.site
        
   Cuando ya tenga todo montao ingrese a al dominio)(julianrjdev.site) y  se le pediran algunos datos para completar la instalación
   de wordpress, simplemente llenelos, envielos y terminará el proceso.
 En este punto ya se tendria todo listo, y se podria ingresar a la pagina de wordpress sin problema.
 

## Detalles del desarrollo

Durante el desarrollo se me presentaron varios problemas que tarde mucho en resolver, ya que en algunas partes me quede bloqueado con problemas
sobre los que no tenia demasiado control como problemas de GCP. Por ende el el proyecto tomó más tiempo de desarrollo de lo esperado y al igual
que el anterior reto se puede considerar que me tomó el tiempo de un proyecto.

Para enfrentarme a este reto tomé un enfoque de ir configurando y testeando los nodos más bajos en la arquitectura y posteriormente ir 
escalando hacia arriba. Lo primero que se hizo fue montar wordpress monolitico en una máquina, posteriormente se creó otra máquina y se montó
la base de datos mysql y de nuevo el wordpress pero con la base de datos remota. El siguiente paso en el desarrollo fue montar el NFS server
en otra instancia y de nuevo montar el wordpress, pero con la base de datos remota y el sistema de archivos sobre la máquina con el servidor NFS. Posterior
a esto monté una segunda instancia con las mismas caracteristicas.

Luego de tener esta parte baja de la arquitectura terminada, puse manos a la obra sobre una nueva instancia, en la que monté NGINX para
balancear la carga a las dos instancias de Wordpress. Luego de que esto funcionará obtuve un dominio en Hostinger y lo asocié a la IP de 
mi máquina NGINX. Finalmente obtuve los certificados SSL mediante certbot y di por finalizado el proyecto.

## Detalles técnicos

Al crear las máquinas en GCP con Ubuntu 22 hay que permitir trafico http y https(Para el NGINX).
Además se recomienda para la instancia de NGINX configurar una IP estatica.

## Descripción y como se configura los parámetros del proyecto

Para configurar los parametros del proyecto se tienen una env_file.txt con las ips y puertos
para docker, si necesita cambiar algo simplemente especifiquelo ahi.
Para los demás componentes las configuraciones de parametros }se hacen como se presentaron en la guia.


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 

A continuación se puede ver la estructura de directorios del proyecto, hay que tener muy en cuenta que cada carpeta representa
los scripts  o instrucciones para una máquina o nodo en especifico del proyecto. Para el caso de los componentes que están dockerizados el archivo más importante es 
el .yml, Para los demás componentes depende bastante, por ejemplo en DNS solo se tiene un archivo que describe que se hizo para obtener
y configurar el DNS. A continuación se describe cada carpeta:
- Tenemos entonces la carpeta db-server con el archivo para montar la imagen de docker y otros auxiliares con variables de entorno, instalación
  ejecución del composer.
-Tenemos la carpeta DNS con la descripción del proceso de configuración.
- Tenemos la carpeta del NFS con los comandos para montar el servidor.
- Tenemos la carpeta proxy-lb con la instalación de lo necesario, la configuración de nginx y la solicitud del ssl.
- Tenemos la carpeta wordpress_server con el archivo para montar la imagen de docker y otros auxiliares con variables de entorno,
  instalación,montar el nfs y ejecutar el composer.
![image](https://user-images.githubusercontent.com/57159295/227059570-6900a345-c6d0-4e26-bcea-da6ecd488d74.png)



# 4. Descripción del ambiente de EJECUCIÓN (en producción)

El proyecto está montando sobre unas insancias de GCP, luego, se tiene un DNS que apunta a la instancia
con NGINX y a su vez esta balancea carga para wordpress.
Para probar o ejecutar el proyecto basta con tener un browser y acceder a julianrjdev.site

# IP o nombres de dominio en nube o en la máquina servidor.

Para que se pueda acceder al proyecto sin necesidad de memorizarse una IP especifica se tiene un nombre 
de dominio, que en este caso es julianrjdev.site o www.julianrjdev.site, esto redireccionará por defecto
a https://julianrjdev.site

## Como se lanza el servidor.

Después de la configuración inicial los servicios tanto de NGINX como de Docker se levantan automaticamente
al iniciar la máquina por lo que no se necesita ejecutar nada.


## Guia de como un usuario utilizaría el software o la aplicación

Un usuario podría utilizar la aplicación simplemente ingresando en el navegador la URL del
proyecto que es julianrjdev.site o www.julianrjdev.site
Al hacer esto le saldria la pagina por defecto de WordPress.

## Resultados o pantallazos (En producción)

A continuación se muestra el proyecto funcionando:

Sitio wordpress corriendo:
![image](https://user-images.githubusercontent.com/57159295/227061001-00023103-d8f0-4963-b4ce-c26408def943.png)

Acceso por HTTPS(Por defecto):
![image](https://user-images.githubusercontent.com/57159295/227061133-ad707d93-1b10-4217-b6fd-01781ce38837.png)


# referencias:
## Guia y comandos de Edwin Montoya - Profesor
      https://github.com/st0263eafit/st0263-231/tree/main/docker-nginx-wordpress-ssl-letsencrypt
## How To Set Up an NFS Mount on Ubuntu 22.04
      https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04
## certbot instructions (Certbot with NGINX and Ubuntu)
      https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

#### versión README.md -> 1.0 (2023-Marzo)
