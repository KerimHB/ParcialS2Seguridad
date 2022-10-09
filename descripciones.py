class Descripcion:
    def __init__(self, desc):
        self.desc=desc
       
    
    def __repr__(self) -> str:
        return f'<Descripcion:{self.desc}>' 

descripciones =[]
descripciones.append(Descripcion(desc= 'Profesor'))
descripciones.append(Descripcion(desc= 'Contador'))
descripciones.append(Descripcion(desc= 'Doctor'))
descripciones.append(Descripcion(desc= 'Policia'))
descripciones.append(Descripcion(desc= 'Vendedor'))