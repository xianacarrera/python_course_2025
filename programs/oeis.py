def leer_dataset_oeis(ruta_archivo):
    secuencias = {}
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()  # Leemos todas las líneas a la vez
        
        for linea in lineas:
            linea = linea.strip()
            # El primer split es sobre el espacio que hay entre el título y la secuencia
            partes = linea.split()
            id_secuencia_actual = partes[0]
            try:
                lista_numeros = partes[1].split(",")[1:-1]  # Ignorar primera y última coma
                numeros_secuencia = list(map(int, lista_numeros))
                secuencias[id_secuencia_actual] = numeros_secuencia
            except Exception as e:
                print(f"Error inesperado al leer la secuencia {id_secuencia_actual}: {str(e)}")
                
        return secuencias
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return {}
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo {ruta_archivo}")
        return {}
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return {}

def calcular_estadisticas(secuencias):
    # Longitud máxima de las secuencias
    long_max = max(len(seq) for seq in secuencias.values())  
    
    # Inicializamos las listas de cuentas, promedios y máximos
    totales, promedios, maximos = [], [], []
    
    # Calculamos estadísticas "por columnas"
    for i in range(long_max):
        # Total de secuencias encontradas con elemento iésimo y suma de todos estos elementos iésimos
        total_encontradas, suma = 0, 0
        # Mayor valor encontrado en el elemento iésimo de las secuencias, e ID de esta
        secuencia_maxima, valor_maximo = None, float('-inf')
        for seq_name, seq in secuencias.items():
            if i < len(seq):                             
                suma += seq[i]                         
                total_encontradas += 1 
                if seq[i] > valor_maximo:
                    valor_maximo = seq[i]
                    secuencia_maxima = seq_name
        promedios.append(suma / total_encontradas)
        totales.append(total_encontradas)
        maximos.append((secuencia_maxima, valor_maximo))
    return totales, promedios, maximos

# Pedimos la ruta del dataset
ruta_dataset = input("Introduzca la ruta al dataset de OEIS: ")

# Leemos todas las secuencias
secuencias = leer_dataset_oeis(ruta_dataset)

print(f"Se han leído {len(secuencias)} secuencias del dataset")

# Hallamos algunas estadísticas para el dataset
totales, promedios, maximos = calcular_estadisticas(secuencias)

for i in range(len(totales)):
    seq_max, valor_max = maximos[i]
    print(
        f"Hay {totales[i]} secuencias con {i}-ésimo elemento. "
        f"El promedio de todos los elementos {i}-ésimos es {promedios[i]:.2f}. "
        f"El máximo es {valor_max} en la secuencia {seq_max}.\n"
    )