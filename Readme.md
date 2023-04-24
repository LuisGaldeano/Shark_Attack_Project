Sharks Attack

En este notebook voy a realizar las explicaciones necesarias del proyecto de Ironhack donde se nos pide que limpiemos un DataFrame sobre ataques de tiburón.

El proyecto lo voy a dividir en 4 partes y cada una de ellas tendrá un notebook que lo argumente. De esta manera se podrá acceder a cada parte del proyecto por separado.

Las partes van a ser:

1.- Análisis inicial
2.- Valores nulos
3.- Valores Inconsistente
4.- Arreglo de datos
5.- Bonus: Análisis de hipótesis

Al finalizar cada apartado exportaré un csv que se llamará sharkattack_parteX.csv, donde la x especificará a que parte corresponde. Por lo que al finalizar el proyecto en la carpeta data se podrá encontrar el csv inicial, otros 5 por cada parte y el csv ya con todos los datos limpios que se llamará sharkattack_limpio.csv

Dicho esto, comencemos:

SharkAttack - Parte 1 (Análisis inicial)

SharkAttack - Parte 2 (Valores nulos)

SharkAttack - Parte 3 (Valores Inconsistente)

SharkAttack - Parte 4 (Arreglo de datos)

SharkAttack - Parte 5 (Bonus: Análisis de hipótesis)
Estructura seguida en cada parte:
Parte 1

En la primera parate me he centrado en el análisis de la tabla, en aberiguar que representa cada columna y establecer que columnas son irrelevantes para mi análisis.

En este caso procedo a explicar que representa cada columna y cuales van a ser a priory las acciones a realizar en cada una de ellas y las posibles complicaciones que me puedo encontrar.

    CaseNumber: Número de caso en formato tipo FECHA, separado por puntos → (2021.04.12)
        Acciones:
            Separar día mes y año
            Eliminar espacios al principio y al final
        Posibles complicaciones
            A veces finaliza con un .a o .b
    Date: Fecha de cuando se produjo el ataque separado por guiones → (02-05-2015)
        Acciones:
            Poner todos en el mismo formato
        Posibles complicaciones:
            A veces está separado por / → (02/05/2015) → Cambiar a guion
            A veces los años puestos con 2 dígitos → Convertir a 4
            A veces los años tienen solo 4 dígitos → Poner fecha 01/01/año
            Todo lo que no ponga una fecha en formato completo poner como 01/01/año
    Year: Año del ataque (2015)
        Acciones:
            Valores float que hay que convertir a int
    Type: Especifica si fue provocado o no y si fue desde barco
        Acciones:
            Sin acciones específicas
    Country: Pais donde se produjo
        Acciones:
            Sin acciones específicas
    Area: Áreas donde se produjo
        Acciones:
            Revisar si hay nombres extraños
    Location: Ciudades donde se produjo
        Acciones:
            Revisar si hay nombres extraños
    Activity: Actividad que se estaba realizando durante el ataque
        Acciones:
            Revisar si hay nombres extraños
    Name: Nombre de los atacados:
        Acciones:
            Revisar que solo estén los nombres
        Posibles complicaciones:
            Algunos nombres acaban con : y una explicación
            En algunos solo identifica si son hombres o mujeres, pero no el nombre
    Sex: Hombres o mujeres
        Acciones:
            Sin acciones específicas
    Age: Edad del atacado
        *Acciones: *
            Revisar que todos los datos sean int
        Posibles complicaciones:
            En algunos casos viene la edad en formato década (60s)
    Injury: Tipo de lesiones provocadas:
        Acciones:
            Revisar que no haya ninguna descripción rara
    Fatal: Define si el accidente fue letal o no con Y/N
        Acciones:
            Revisar que no haya valores extraños
        Posibles complicaciones:
            Hay un valor M
    Time: Hora y minuto en el que se produzco el ataque en formato 18h45
        Acciones:
            Cambiar a formato Time
        Posibles complicaciones:
            Algunos datos no especifica la hora y si el momento del día (Afternoon…)
            Algunos valores tienen strings después de la fecha
    Species: (DIFICIL —> DEJAR PARA EL FINAL) Especie de tiburón que realizó el ataque junto con su longitud en metros
        Acciones:
            Separar todos los metros y ponerlos en una columna aparte llamada sharksize
            Dejar en la columna solo la especie de tiburón o ‘Unknown’ si no se conoce
        Posibles Complicaciones:
            Muchos registros muestran solo la especie del tiburón o su longitud, no ambas cosas
    Investigator or Source: Nombre del investigador o paper donde se obtiene la información:
        Acciones:
            Muchos de ellos tienen fecha al final
        Posibles Complicaciones
            Muchos de los nombres se repiten pero coambia en formato del string
    pdf: Nombre del pdf del estudio → (2018.06.25-Wolfe.pdf):
        Acciones:
            Todos empiezan por una fecha
            El nombe del PDF corresponde al nombre de la columna name
            Los que sean Nan → Unir la fecha del ataque + ‘-’ + nombre + ‘.pdf’
    href formula: link del pdf.
        Acciones:
            Como todos tienen el mismo formato, aunque luego no se pueda enlazar a una dirección real, como no es un dato que a priori considere relevante, para eliminar las nan une lo siguiente:
                ‘http://sharkattackfile.net/spreadsheets/pdf_directory/’ + columna pdf
    href: link del pdf
        Acciones:
            Revisar si los valores son iguales a los de href.
            En caso de serlos, los valores nan rellénalos de la misma manera.
    Case Number2: Especifica la fecha del ataque
        Acciones:
            Revisa si son todos iguales a caseNumber → En caso de serlo poner un 0
    Case Number3: Misma columna que case Number
        Acciones:
            Revisa si son todos iguales a caseNumber → En caso de serlo poner un 0
    original order: Número de caso
        Acciones:
            Revisar que estén todos en formato int → En caso de estarlo no hacer nada más.

Parte 2

Para la parte dos he establecido una estructura de trabajo que me permita limpiar los valores nulos de una manera homogénea.
Pasos a seguir para cada columna:

    Imprimir el gráfico para ver si tiene valores nulos
    Ver las primeras 10-20 filas de la columna para ver como está estructurado el tipo de dato
    Ver si es posible hacer una pequeña modificación de los datos antes de limpiar los nulos
        Si la modificación es muy grande dejarla para la parte 3 de análisis de inconsistencias
    Ver que porcentaje del total de la columna representan los valores nulos
        % < 25% → En este caso se establece un valor acorde con el tipo de dato que permita reconocer que el valor era nulo, pero se entiende que a priori es un dato que no se va a obtener, ya que por el bajo peso que tiene en el total de la columna no merece la pena investigar más a fondo. (Si sobra tiempo se volverá a este punto)
        % > 25% → Debido a que los nulos tienen un peso importante sobre el total de la columna, se establecerá un proxy que se entienda que esos valores son anómalos y que hay que analizarlos más adelante en la parte 3.
    Una vez analizado el %, realizar un fillna(’valor’, inplace=True) para eliminar los valores nulos de la columna

Parte 3

Para la parte tres he establecido una estructura de trabajo que me permita limpiar los valores inconsistentes de una manera homogénea.
Pasos a seguir para cada columna:

    Nombre de la columna en markdown
    Identificar de que clase son los datos
        Crea una función que se llame repetidos y que revise el número de datos diferentes que hay en la columna
    Imprime las 10-20 primeras lineas para ver cual es su estructura
    Obten un array con los valores únicos
    Analizar si es necesario realizar cambios y modificaciones en la columna
        Si es necesario → Realiza las operaciones necesarias para transformar los datos al tipo más adecuado en función de la columna
        No es necesario → Deja la columna como está y explica en un markdown la razón

Parte 4

En esta parte estableceré el objetivo que me he marcado y arreglaré los datos de las columnas necesarias una a una para poder luego analizarlas en la parte 5:

Las columnas que he decidido que son necesarias para mi análisis son:

    date
    year
    hora
    activity
    sex
    fatal
    species

Parte 5

En esta parte analizo los datos que he considerado relevantes para mi análisis, realizo gráficos que lo soporten y expreso mis conclusiones.
*Conclusión

Como conclusión se puede afirmar que si practicas surf, especialmente entre las 12:00 y las 19:00 tienes más probabilidades de que te ataque un tiburón, que probablemente sea blanco
