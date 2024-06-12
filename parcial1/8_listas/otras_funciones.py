def menu(operacion, peliculas):
    match (operacion):
        case 1: 
            peliculaAgregar = input("Ingrese el titulo de la pelicula a agregar: ")
            peliculas.append(peliculaAgregar)
        case 2:
            peliculaQuitar = input("Ingrese el titulo de la pelicula a quitar: ")
            peliculas.remove(peliculaQuitar)
        case 3:
            peliculaActualizar = input("Ingrese el titulo de la pelicula a actualizar: ")
            if peliculaActualizar in peliculas:
                pos = peliculas.index(peliculaActualizar)
                peliculaActualizada = input("Ingrese el nuevo titulo: ")
                peliculas.pop(pos)
                peliculas.insert(pos, peliculaActualizada)
        case 4:
            print("Peliculas")
            print(peliculas)
        case 5:
            peliculaBuscar = input("Ingrese el titulo de la pelicula a buscar: ")

            for elemento in peliculas:
                if peliculaBuscar == elemento:
                    posicionPelicula = peliculas.index(elemento)
                    print(f"{peliculaBuscar} encontrada en la posicion {posicionPelicula}")
        case 6:
            print("Ha elegido vaciar la lista. Buen trabajo.")
            peliculas.clear()

