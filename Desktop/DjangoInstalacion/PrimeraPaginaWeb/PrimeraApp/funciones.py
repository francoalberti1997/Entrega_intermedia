def devuelve_buenas_experiencias(objeto):
    for objetos in objeto:
        if int(objetos.evaluacion) > 2:
            return objetos

