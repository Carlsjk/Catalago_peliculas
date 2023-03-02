from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:
        print("opciones:")
        print("1. Agregar pelicula")
        print("2. Listar peliculas")
        print("3. Eliminar catalogo de peliculas")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliucula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as  e:
        print(f'Error: {e}')
        opcion = None
else:
    print('Salimos del programa...')