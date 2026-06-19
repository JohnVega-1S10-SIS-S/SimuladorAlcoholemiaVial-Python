from colorama import Fore, Style, init
from core import backend, validators
from reports import pdf_export
from tabulate import tabulate

init()

def success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def alert(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

def info(message):
    print(Fore.BLUE + message + Style.RESET_ALL)

def console_menu():
    """
        Muestrar una interfaz de usuario por consola que permita interactuar con el sistema de login. El
        programa muestrar un menú con las opciones de registrar usuario, iniciar sesión, listar usuarios y salir.
    """
    while True:

        print('\n' + '='*31)
        print(' SIMULADOR DE ALCOHOLEMIA VIAL ')
        print('='*31 + '\n')

        print('(a) Agregar nuevo conductor.')
        print('(e) Ver estadísticas.')
        print('(t) Ver tabla de conductores.')
        print('(s) Buscar conductor por Cedula o Placa.')
        print('(p) Exportar PDF')
        print('(d) Eliminar conductor.')
        print('(f) Filtrar tabla.')
        print('(c) Cerrar programa.')

        option = input('\n' + 'Seleccione una opcion: ').lower()

        if option == 'a':

            success('\n' + '='*10 + ' AGREGAR CONDUCTOR ' + '='*10 +'\n')

            while True:

                enter_driver_id = input('Cedula del conductor: ')

                valid_inpt, result_inpt = validators.validate_user_input(enter_driver_id)
                valid_cedl, result_cedl = validators.validate_cedula(enter_driver_id)

                if not valid_inpt:
                    error(f"✖ Error: {result_inpt}")

                if not valid_cedl:
                    error(f"✖ Error: {result_cedl}")

                if not valid_inpt or not valid_cedl:
                    continue

                enter_driver_id = result_cedl
                break
                                
            while True:

                enter_license_plate = input('Placa del coche: ')

                valid_inpt, result_inpt = validators.validate_user_input(enter_license_plate)
                valid_plat, result_plat = validators.validate_license_plate(enter_license_plate)

                if not valid_inpt:
                    error(f"✖ Error: {result_inpt}")

                if not valid_plat:
                    error(f"✖ Error: {result_plat}")

                if not valid_inpt or not valid_plat:
                    continue

                enter_license_plate = result_plat
                break

            while True:

                alcohol_input = input('Nivel de Alcohol: ')
                valid, result = validators.validate_alcohol_level(alcohol_input)

                if valid:
                    enter_alcohol_level = result
                    break

                error(f"✖ Error: {result}")

            if enter_alcohol_level.is_integer():
                enter_alcohol_level = int(enter_alcohol_level)

            data = backend.process_driver(
                enter_driver_id,
                enter_license_plate,
                enter_alcohol_level
            )

            backend.count_offenses(
                enter_driver_id
            )

            exists = backend.driver_exists(
                enter_driver_id,
                enter_license_plate
            )

            if exists:

                alert("\n⚠ Este conductor ya aparece registrado.")

                option = input(
                    "\n¿Desea registrar una nueva multa? (s/n): "
                ).lower()

                if option != "s":
                    continue
            
            valid, table = backend.inser_data(data)

            if valid:
                success('\n' + "✔ Datos guardados correctamente.")
                success('\n' + table)
            else:
                error('\n' + f"✖ Error: {result}")
        
        elif option == 'e':

            info('\n' + '='*10 + ' ESTADISTICA ' + '='*10 +'\n')

            stats = backend.get_statistics()

            table = [
                ["Total de registros", stats["total"]],
                ["Embriaguez ligera", stats["ligera"]],
                ["Embriaguez", stats["embriaguez"]],
                ["Embriaguez extrema", stats["extrema"]]
            ]

            info(tabulate(
                table,
                headers=["Indicador", "Cantidad"],
                tablefmt="fancy_grid"
            ))

        elif option == 't':

            info('\n' + '='*10 + ' TABLA ' + '='*10 +'\n')

            valid, result = backend.load_data()

            if len(result) > 1:
                info('\n' + f"Tienes ({len(result)}) conductores registrados." + '\n')
            elif len(result) == 1:
                info('\n' + "Tienes (1) conductor registrado." + '\n')
            else:
                info('\n' + "Aun no has registrado a ningun conductor." + '\n')

            if valid:
                info(tabulate(result, headers="keys", tablefmt="fancy_grid"))
            else:
                error(f"✖ Error: {result}")

        elif option == 's':

            info('\n' + '='*10 + ' BUSCAR POR CEDULA O PLACA ' + '='*10 +'\n')

            search_term = input("Ingrese Cedula o placa del conductor: ")
            valid, results = backend.search_driver(search_term)

            if valid:
                info('\n' + f"Resultados encontrados: {len(results)}" + '\n')
                info(tabulate(results, headers="keys", tablefmt="fancy_grid"))
            else:
                error('\n' + f"✖ Error: {results}")

        elif option == 'p':

            info('\n' + '='*10 + ' EXPORTAR DATOS A PDF ' + '='*10 + '\n')

            while True:
                print('1. Exportar tabla completa.')
                print('2. Exportar conductor específico.')
                print('3. Exportar estadísticas.')
                print('4. Volver.')

                option = input('\n' + 'Seleccione una opcion: ')

                valid_num, result_bool = validators.validate_number(option)

                if not valid_num:
                    error('\n' + f"✖ Error: {result_bool}" + '\n')
                    continue

                option = int(option)

                if option == 1:
                    
                    while True:

                        valid, drivers_data = backend.load_data()

                        if valid:

                            if pdf_export.export_table_pdf(drivers_data):
                                success('\n' + "✔ Tabla exportada correctamente." + '\n')
                                break
                            else:
                                error('\n' + "✖ Nose pudo exportar los datos." + '\n')
                                break
                        else:
                            print(drivers_data)

                elif option == 2:

                    while True:

                        search_term = input('\n' + "Ingrese Cedula o Placa del conductor: ")
                        valid_inpt_1, result_inpt = validators.validate_user_input(search_term)

                        if not valid_inpt_1:
                            error(f"✖ Error: {result_inpt}")
                            continue                   
                        
                        valid, results = backend.search_driver(search_term)

                        if valid:
                            info('\n' + f"Resultados encontrados: {len(results)}" + '\n')
                            info(tabulate(results, headers="keys", tablefmt="fancy_grid"))
                        else:
                            error('\n' + f"✖ Error: {results}")

                        selected_id = input('\n' + "Ingrese el ID del registro: ")

                        valid_inpt_2, result_inpt_2 = validators.validate_user_input(selected_id)

                        if not valid_inpt_2:
                            error(f"✖ Error: {result_inpt_2}")
                            continue   

                        valid, driver = backend.get_driver_by_id(selected_id)

                        if valid:

                            confirm = input('\n' + "¿Exportar a PDF? (s/n): ").lower()

                            if confirm != "s":
                                continue

                            if pdf_export.export_driver_pdf(driver):
                                success('\n' + "✔ Datos del conductor exportado correctamente." + '\n')
                                break
                            else:
                                error('\n' + "Nose pudo exportar los datos.")
                                break
                        else:
                            print(driver)

                elif option == 3:

                    while True:

                        stats = backend.get_statistics()

                        if pdf_export.export_statistics_pdf(stats):
                            success('\n' + "✔ Reporte estadístico exportado correctamente." + '\n')
                            break
                        else:
                            error('\n' + "Nose pudo exportar los datos." + '\n')
                            break

                elif option == 4:
                    break
                else:
                    alert('\n' + f"⚠ Opcion no valida." + '\n')

        elif option == 'd':

            error('\n' + '='*10 + ' ELIMINAR CONDUCTOR ' + '='*10 + '\n')

            exit_delete_menu = False
            
            while True:

                search_term = input("Ingrese la Cedula o placa del conductor: ")
                valid_inpt, result_inpt = validators.validate_user_input(search_term)

                if not valid_inpt:
                    error('\n' + f"✖ Error: {result_inpt}" + '\n')
                    continue

                valid, result = backend.search_driver(search_term)

                if valid:

                    if len(result) > 1:
                        error('\n' + f"Hemos encontrado a ({len(result)}) conductores. Porfavor escriba el ID del conductor a eliminar." + '\n')
                    else:
                        error('\n' + "Si este es el conductor que desea eliminar. Porfavor escribe su ID." + '\n')

                    error(tabulate(result, headers="keys", tablefmt="fancy_grid"))

                    driver_id = input('\n' + "Ingrese el ID del conductor: ")

                    valid_inpt, result_inpt = validators.validate_user_input(driver_id)
                    valid_num, result_num = validators.is_number(driver_id)

                    if not valid_inpt:
                        error(f"✖ Error: {result_inpt}")

                    if not valid_num:
                        error(f"✖ Error: {result_num}")

                    if not valid_inpt or not valid_num:
                        continue

                    error('\n' + '⚠ Está a punto de eliminar este registro. Esta acción no se puede deshacer.')

                    print('\n' + '(d) ELiminar.')
                    print('(c) Cancelar.')

                    while True:
                        option = input('\n' + 'Seleccione una opcion: ').lower()

                        if (option == 'd'):

                            driver_id = int(driver_id)

                            deleted, message = backend.delete_driver(driver_id)

                            if deleted:
                                success('\n' + f"✔ {message}")
                                exit_delete_menu = True
                                break
                            else:
                                error('\n' + f"✖ {message}")
                                exit_delete_menu = True
                                break
                        elif (option == 'c'):
                            info('\n' + "Eliminación cancelada.")
                            exit_delete_menu = True
                            break
                        else:
                            alert('\n' + f"⚠ Opcion no valida.")

                    if exit_delete_menu:
                        break
                else:
                    error('\n' + f"✖ Error: {result}")

        elif option == 'f':

            while True:

                print('\n' + '='*10 + ' FILTRAR ' + '='*10 +'\n')

                print('1. Embriaguez ligera')
                print('2. Embriaguez')
                print('3. Embriaguez extrema')
                print('4. Volver')
                
                filter_term = input('\n' + "Seleccione: ")

                valid_inpt, result_inpt = validators.validate_user_input(filter_term)
                valid_num, result_num = validators.validate_number(filter_term)

                if not valid_inpt:
                    error(f"✖ Error: {result_inpt}")

                if not valid_num:
                    error(f"✖ Error: {result_num}")

                if not valid_inpt or not valid_num:
                    continue

                filter_term = int(filter_term)

                if filter_term == 1:
                    drunkenness = "Embriaguez ligera"
                elif  filter_term == 2:
                    drunkenness = "Embriaguez"
                elif  filter_term == 3:
                    drunkenness = "Embriaguez extrema"
                elif  filter_term == 4:
                    break
                else:
                    alert('\n' + f"⚠ Opcion no valida.")
                    continue

                valid, results = backend.filter_table(drunkenness)

                if valid:
                    info('\n' + f"Resultados encontrados: {len(results)}" + '\n')
                    info(tabulate(results, headers="keys", tablefmt="fancy_grid"))
                else:
                    info('\n' + results)

        elif option == 'c':
            success('\n' + "✔ Cerrando programa." + '\n')
            break
        else:
            alert('\n' + f"⚠ Opcion no valida.")