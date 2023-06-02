# Laboratorio 6 - Parte 1
### Estudiante: Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
### Profesor: Edwin Nelson MOntoya Munera, emontoya@eafit.edu.co

### Conexión al cluster
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/8408e857-b853-4aef-9dbf-0e6dc74fdf4c)


## 1. Hive
### Cargando datos
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/fadc203c-a970-4baa-ad7c-02d84ee86002)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/42a87070-6dc0-420d-bafc-b1d736fe5b3f)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/20e2c0cf-27be-47d8-9c74-ec5f6afc1a81)

### Creando tabla externa
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/fcff71fe-5e4e-4782-927b-d00101da2897)

### Creando tabla externa (S3)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/e46a4cb4-5367-4743-8b0c-18ee9cec4423)


### Algunas consultas
#### Select basico en local y s3
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/aa9148a5-705f-4264-9478-fc0de4244fdd)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/97e4a8ee-a202-4fc0-9f30-2e26dd390f74)

#### Crear tabla expo
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/f4c3a8d4-a0df-489f-a67f-c83c447a2fcf)

##### Join de dos tablas
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/027a24ca-ca6b-412b-a4c9-29465c2b3096)

### WordCount
#### Crear tabla
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/26beb8df-3292-4e28-a70d-c3a36bcb3ce3)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/59af70ea-4f35-4b32-aa59-1a6aa565c8e8)

### Realizar conteo y ordenamiento
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/49556fa1-816a-46ec-acdd-b4db7c354a25)
 
 ### Almacenando en una tabla el diccionario de frecuencia de palabras en el wordcount
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/7f83ebb3-2dfb-4156-96f7-c80fc017681c)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/f4c1f6da-6cb8-4267-96bd-99562b78963c)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/52ae51f2-a009-47dc-87e1-0f6eb033d563)+

### Con SparkSQL
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/5493a250-a740-4a76-9029-3815da6c3414)

## 2. AWS Athena & Glue
### Crear y ejecutar el Crawler
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/20cf3748-fcb6-4e37-a64c-e853cab7ac71)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/5a107af6-c60e-41d0-92ff-55dd56dd9c5d)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/a808fe67-37f9-4756-8b7c-00c6a1e501a7)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/614811b4-79bc-4df1-a60c-d020d0f32701)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/bc0bf5cc-4663-4873-a178-f276f956c946)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/56c05930-989e-4362-a46c-467b1cd880da)

### Querys desde Athena
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/990c6434-b033-42e4-be6d-2789c6a84462)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/509ad823-1818-4fed-a67b-0673e52c5c99)

### Querys desde Hive
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/a67d4f27-9a36-4cd3-89de-cb2519822943)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/0f15cb16-1eb1-45df-9c11-b8c66c747a28)

## 3. AWS RedShift
### Creando el cluster
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/11b4e3c0-d3c9-405f-8558-132b6c61c10d)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/518e1564-49f2-41d1-9020-c610b0414760)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/4ed558fa-2d23-4774-bea9-c845c3d3a176)

### Crear la base de datos externa:
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/d86c33ef-a767-4fb1-8631-229cb83c6159)

### Crear una table con datos externos en S3.
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/48f981c7-ec6d-4b67-abe1-1974ab38f677)

### Consultar datos
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/282a2a7c-bfff-4f6e-845e-c90b6b2377ea)

### Crear una tabla nativa en redshit para combinarla con la tabla externa en un query:
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/9a0842bd-caf8-49f5-bd73-61fc105109ab)

### Cargar datos en la table ‘event2’
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/57001f79-4b8b-4f9c-bb87-4d6b724974ad)

### Realizar una consulta con tablas externas y nativas:
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/1ccfc9f3-7eb8-4878-901c-db18176c25bd)


