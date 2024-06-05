def menu(operacion, peliculas):
    match (operacion):
        case 1: 
            peliculaAgregar = input("Ingrese el titulo de la pelicula a agregar: ")
            peliculas.append(peliculaAgregar)
        case 2:
            peliculaQuitar = input("Ingrese el titulo de la pelicula a quitar: ")
            peliculas.remove(peliculaQuitar)
        case 3:
            print("Peliculas")
            print(peliculas)

