# Evidencias de realización del laboratio 5 
## Julian Andres Ramirez Jimenez

## Parte 1 - Ejercicios MapReduce

### 1.1 Estadisticas de salarios
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/75b0f232-060f-4ad4-b68d-a858835110be)

Aqui se puede encontrar el código: https://github.com/JulianRamirezJ/st0263-jaramirezj/blob/main/laboratorio5/Parte3/mr-scripts/salary.py

### 1.2 Estadisticas de empresas

![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/15dcfb1c-1053-49df-afb4-d3a3678c39d7)

Aqui se puede encontrar el código: https://github.com/JulianRamirezJ/st0263-jaramirezj/blob/main/laboratorio5/Parte3/mr-scripts/stock_analysis.py

### 1.3 Estadisticas de peliculas
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/ee14947f-48f4-49eb-931d-aa74defbe397)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/d0addf95-ae2b-43f3-8d98-b70195238804)


Aqui se puede encontrar el código: https://github.com/JulianRamirezJ/st0263-jaramirezj/blob/main/laboratorio5/Parte3/mr-scripts/movies.py


## Parte 2

### Conexión al nodo master
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/bcf06386-0241-46aa-972f-7902a9209de8)
### Linea de comandos pyspark
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/7b7c7f53-f8b2-415e-b836-04ae04f17531)


### 2.1 WordCount con PySpark y HDFS
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/efb1b3e4-8158-4f0b-8ff8-e47c9a379283)


### 2.2 Wordcount con pyspark y s3
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/605e50d8-17de-4be7-b064-2cc8973846ab)
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/8d76a8a3-37e4-4aba-83ac-2d4753eab69d)

![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/5c513d9c-2fc9-4104-9484-d39ce0f3574f)

![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/a0bb9258-1c03-4d79-a319-c7c8fbeea497)

### 2.3 WordCount con JupyterHub
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/739a4ddc-2af7-4f2d-a1d4-356c53df54ce)


### 2.4 Replicacion del notebook en JupyterHub
Esta parte se hizo en jupyterhub

Aquí puede encotrar el notebook: https://github.com/JulianRamirezJ/st0263-jaramirezj/blob/main/laboratorio5/Parte3/Data_processing_using_PySpark.ipynb
![image](https://github.com/JulianRamirezJ/st0263-jaramirezj/assets/57159295/c85f0ec5-9250-4155-9c8c-840c9f4f029a)

Bloque 3-4: Se crea y asigna una sesión de Spark.

Bloque 5: Se lee el archivo de datos desde S3 's3://st0263spulido1/datasets/sample_data.csv'.

Bloques 6-7: Se muestran las columnas y sus longitudes.

Bloque 7: Se muestra el número de filas.

Bloque 8: Se muestra la forma de los datos.

Bloque 9: Se imprime el esquema.

Bloque 10: Se consultan e imprimen las primeras cinco filas.

Bloque 11: Se consultan e imprimen las primeras cinco filas, mostrando solo las columnas de edad y móvil.

Bloque 12: Se imprimen algunas estadísticas sobre el dataframe.

Bloque 13: Se importan algunos tipos de SQL.

Bloque 14: Se agrega una nueva columna llamada "age_after_10_yrs" al DataFrame tomando los valores de la columna existente "age" y sumándoles 10 a cada valor. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 15: Se agrega una nueva columna llamada "age_double" al DataFrame convirtiendo los valores de la columna existente "age" a un tipo de datos Double utilizando la función cast(). La función cast() se utiliza para cambiar el tipo de datos de una columna. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 16: Se agrega una nueva columna llamada "age_after_10_yrs" al DataFrame tomando los valores de la columna existente "age" y sumándoles 10 a cada valor. Esta nueva columna representa la edad de cada individuo después de 10 años. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 17: Se filtra el DataFrame df en base a una condición. Específicamente, se seleccionan las filas donde el valor en la columna "mobile" es igual a "Vivo". Se utiliza el método filter() para aplicar la condición, y df['mobile']=='Vivo' crea una expresión booleana que verifica si el valor en la columna "mobile" es igual a "Vivo". Finalmente, se llama al método show() para mostrar el DataFrame filtrado resultante, mostrando todas las filas que cumplen la condición.

Bloque 18: Se filtra el DataFrame df en base a una condición donde el valor en la columna "mobile" es igual a "Vivo". Luego se seleccionan columnas específicas, en este caso "age", "ratings" y "mobile", del DataFrame filtrado. Finalmente, se muestra el DataFrame resultante, mostrando solo las columnas seleccionadas para las filas que cumplen la condición.

Bloque 19: Se filtra el DataFrame df para seleccionar las filas donde el valor en la columna "mobile" es igual a "Vivo" y el valor en la columna "experience" es mayor que 10. Se aplican múltiples filtros de forma secuencial para reducir el conjunto de datos. Finalmente, se muestra el DataFrame resultante, mostrando todas las columnas para las filas
filtradas que cumplen ambas condiciones.

Bloque 20: Se filtra el DataFrame df para seleccionar las filas que cumplen dos condiciones simultáneamente. La primera condición verifica si el valor en la columna "mobile" es igual a "Vivo", y la segunda condición verifica si el valor en la columna "experience" es mayor que 10. El operador & combina estas dos condiciones mediante el operador lógico AND. El DataFrame resultante solo incluirá filas donde se cumplan ambas condiciones.

Bloque 21: Se selecciona la columna "mobile" del DataFrame df. Luego se aplica la función distinct(), que elimina los valores duplicados, asegurando que solo se retengan los valores únicos. Finalmente, se muestran los valores distintos en la columna "mobile".

Bloque 22: Se selecciona la columna "mobile" del DataFrame df. Luego se aplica la función distinct(), que elimina los valores duplicados, asegurando que solo se retengan los valores únicos. Finalmente, se llama a la función count() para calcular el número de valores distintos en la columna "mobile".

Bloque 23: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el conteo de ocurrencias para cada marca de móvil única utilizando la función count(). Finalmente, se muestra el DataFrame agrupado resultante, mostrando la marca de móvil y su conteo correspondiente.

Bloque 24: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el conteo de ocurrencias para cada marca de móvil única utilizando la función count(). A continuación, se ordena el DataFrame agrupado resultante en orden descendente basado en la columna "count" utilizando la función orderBy().

Bloque 25: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el valor promedio (media) para cada columna numérica en el DataFrame agrupado utilizando la función mean().

Bloque 26: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula la suma de cada columna numérica dentro de cada grupo utilizando la función sum().

Bloques 27-28: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el valor máximo/mínimo para cada columna numérica dentro de cada grupo utilizando las funciones min()/max().

Bloque 29: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se aplica la función agg() para calcular una agregación en una columna específica. En este caso, se calcula la suma de la columna "experience" dentro de cada grupo.

Bloque 30-32: Se aplica una función definida por el usuario (UDF) llamada brand_udf a la columna 'mobile' de un DataFrame df. Esta UDF transforma los valores en la columna 'mobile' y agrega una nueva columna llamada 'price_range' al DataFrame. Finalmente, el código muestra las primeras 10 filas del DataFrame modificado, mostrando las columnas originales junto con la columna recién agregada 'price_range'.

Bloque 33: Se define una función definida por el usuario (UDF) utilizando una función lambda. La UDF se llama age_udf y toma una 'edad' como entrada. Devuelve "joven" si la edad es menor o igual a 30, y "mayor" en caso contrario. El tipo de retorno se especifica como StringType(). Luego, se aplica la UDF al DataFrame df utilizando la función withColumn(). Se agrega una nueva columna llamada 'age_group' al DataFrame aplicando la función age_udf a la columna 'edad'.

Bloque 36: Desafortunadamente, jupyterhub se quejaba de que no estaba instalado Pandas >= 1.0.5 y no pude resolver este problema. Por lo tanto, no pude ejecutar la sección de pandas.

Bloque 38-43: Todo este código está relacionado con guardar los resultados en AWS S3.


