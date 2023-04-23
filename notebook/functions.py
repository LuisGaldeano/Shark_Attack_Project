import pylab as plt
import seaborn as sns
import re
import pandas as pd


####### PARTE 1 #######
def grafico(df):  # Función que devuelve un gráfico
    plt.figure(figsize=(10, 6))  # inicia la figura y establece el tamaño

    sns.heatmap(df.isna(),  # datos
                yticklabels=False,  # quita las etiquetas del eje y
                cmap='viridis',  # mapa de color
                cbar=False,  # sin barra lateral
                )
    plt.show()


#######  PARTE 2  ########
def filas_con_nulos(df, columna):
    valores_nulos = df[columna].isna()

    filas = df[valores_nulos]

    return filas


#######  PARTE 3  #######
def repetidos(df, columna):
    tipos = []

    for valor in df[columna]:
        tip = type(valor)
        tipos.append(tip)

    tipos_unicos = set(tipos)
    cantidad = len(tipos_unicos)
    return cantidad


####### AGREGADO   ########

def dos_num_seguidos(df, columna):
    output_list = []
    for i, valor in enumerate(df[columna]):
        num = re.findall(r'\d{2}', str(valor))
        if len(num) > 0:
            resultado = num[0]
            df.at[i, columna] = resultado
    return df[columna].unique()







#
#
# # Función para que me devuelva un diccionario con todos los tipos de datos que hay y el número que hay de cada tipo de dato
# def tipo_datos(df, column):
#     conteo = {}
#
#     for valor in df[column]:
#         conteo[valor] = df[column].dtype
#
#     valores_agrupados = {}
#
#     # Iterar a través del diccionario original
#     for key, value in conteo.items():
#         if value not in valores_agrupados:
#             # Si el valor no está en el diccionario de valores agrupados, crear una nueva lista con la key actual
#             valores_agrupados[value] = [key]
#         else:
#             # Si el valor ya está en el diccionario de valores agrupados, agregar la key actual a la lista existente
#             valores_agrupados[value].append(key)
#
#     return valores_agrupados.keys()
#
#
# def eliminar_elementos(df, column, *element):
#     e = list(element)
#
#     for index, row in df.iterrows():
#         valor = row[column]
#         for elem in e:
#             valor = valor.replace(elem, '')
#         df.at[index, column] = valor
#
#     return df
#
#
# def remplazar_palabra(df, column, dictionary):
#     df[column] = df[column].str.split()
#     df[column] = df[column].apply(lambda x: ' '.join([dictionary[word] if word in dictionary else word for word in x]))
#     return df
#
#
# def obtener_num_1(df, columna, regex='\d+'):
#     df['num'] = 0
#     filas = []
#     df[columna] = df[columna].astype(str)
#     for i, valor in enumerate(df[columna]):
#         num = re.findall(regex, str(valor))  # busca los valores que cumplan el regex en cada elemento
#         num = [int(n) for n in num]  # guarda el valor encontrado en una nueva columna
#         if len(num) > 0:
#             df.at[i, 'num'] = int(num[0])
#             filas.append(i)
#
#
# def obtener_num_2(df, columna, regex='\d{2}'):
#     df['num'] = 0
#     filas = []
#     df[columna] = df[columna].astype(str)
#     for i, valor in enumerate(df[columna]):
#         num = re.findall(regex, valor)  # busca los valores que cumplan el regex en cada elemento
#         if len(num) >= 2:
#             df.at[i, 'num'] = num  # guarda el valor encontrado en una nueva columna
#             filas.append(i)
#
#
# def repetida(df, columna, regex='\d{2}'):
#     df['num_encontrado'] = None
#     filas = []
#     for i, valor in enumerate(df[columna]):
#         if pd.notna(valor):  # verifica si el valor no es nulo
#             valor_str = str(valor)  # convierte el valor a string
#
#         numeros = re.findall(regex, valor)  # busca los valores que cumplan el regex en cada elemento
#         if len(numeros) >= 2:
#             df.at[i, 'num_encontrado'] = numeros  # guarda el valor encontrado en una nueva columna
#             filas.append[i]  # añade el numero de fila
#
#     for i, valor in enumerate(df[df.columna]):
#         if i in filas:
#             df.at[i, columna] = df.at[i, 'num_encontrado']  # reemplaza el valor con  'num_encontrado'
#
#     df.columna.index()


