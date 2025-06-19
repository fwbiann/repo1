turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def obtener_opcion_menu():
    while True:
        try:
            opcion_str = input("Ingrese opción: ").strip()
            opc = int(opcion_str)
            
            if 1 <= opc <= 4:
                return opc
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def turistas_por_pais(pais_buscado):
    pais_buscado_lower = pais_buscado.lower()
    
    encontrados = []
    for datos_turista in turistas.values():
        nombre_turista, pais_origen, _ = datos_turista 
        
        if pais_origen.lower() == pais_buscado_lower:
            encontrados.append(nombre_turista)
            
    if encontrados:
        print(encontrados)
    else:
        print("No hay turistas de ese pais.")

def turistas_por_mes(mes_param):
    while not (1 <= mes_param <= 12):
        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
        try:
            mes_input_str = input("Ingrese mes a buscar: ").strip()
            mes_param = int(mes_input_str)
        except ValueError:
            print("Entrada inválida. Ingrese un número entero para el mes.")
            mes_param = 0
    
    conteo_en_mes = 0
    total_de_turistas = len(turistas)

    if total_de_turistas == 0:
        return 0.0

    for datos_turista in turistas.values():
        _, _, fecha_ingreso_str = datos_turista 
        
        try:
            mes_ingreso = int(fecha_ingreso_str.split('-')[1])
            if mes_ingreso == mes_param:
                conteo_en_mes += 1
        except (ValueError, IndexError):
            continue

    porcentaje = (conteo_en_mes / total_de_turistas) * 100
    return round(porcentaje, 1)

def eliminar_turista():
    nombre_a_eliminar = input("Ingrese nombre del turista a eliminar: ").strip()
    nombre_a_eliminar_lower = nombre_a_eliminar.lower()

    turista_encontrado_y_eliminado = False
    claves_a_eliminar = [] 

    for id_turista, datos_turista in turistas.items():
        nombre_en_registro, _, _ = datos_turista 
        
        if nombre_en_registro.lower() == nombre_a_eliminar_lower:
            claves_a_eliminar.append(id_turista)
            turista_encontrado_y_eliminado = True

    if turista_encontrado_y_eliminado:
        for key in claves_a_eliminar:
            del turistas[key]
        print("Turista eliminado con éxito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")

def main():
    opcion_elegida = 0

    while opcion_elegida != 4:
        print("""\n*** MENU PRINCIPAL ***)
        (1.- Turistas por país.)
        (2.- Turista por mes.)
        (3.- Eliminar turista.)
        (4.- Salir.""")

        opcion_elegida = obtener_opcion_menu()

        if opcion_elegida == 1:
            pais_input = input("Ingrese pais a buscar: ")
            turistas_por_pais(pais_input)
        elif opcion_elegida == 2:
            mes_input_str = input("Ingrese mes a buscar: ").strip()
            
            try:
                mes_para_buscar = int(mes_input_str)
                porcentaje_mes = turistas_por_mes(mes_para_buscar)
                print(f"El número de turistas equivale al {porcentaje_mes:.1f} % del total.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero para el mes.")

        elif opcion_elegida == 3:
            eliminar_turista()
        elif opcion_elegida == 4:
            print("Programa terminado...")

if __name__ == "__main__":
    main()