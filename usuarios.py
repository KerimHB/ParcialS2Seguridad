class Usuario:
    def __init__(self, id, username, password, nombre, apellido, edad, descripcion, img):
        self.id=id
        self.username=username
        self.password=password
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.descripcion=descripcion
        self.img=img
    
    def __repr__(self) -> str:
        return f'<Usuario:{self.username}>' 

usuarios=[]
usuarios.append(Usuario(id=1, username='RB66', password='123456', nombre='Reaper', apellido='Borja', edad=23, descripcion='Streamer/Desarrollador', img='streamerH.jpg'))
usuarios.append(Usuario(id=2, username='JM98', password='654321', nombre='Jasmin', apellido='Molina', edad=29, descripcion='Abogada', img='abogada.jpg'))
usuarios.append(Usuario(id=3, username='RR87', password='456789', nombre='Ricardo', apellido='Rodriguez', edad=26, descripcion='Contador', img='contador.jpg'))
usuarios.append(Usuario(id=4, username='GM65', password='987654', nombre='Gilberto', apellido='Molina', edad=23, descripcion='Abogado', img='abogado.jpg'))
usuarios.append(Usuario(id=5, username='JP88', password='147258', nombre='Juan', apellido='Perez', edad=45, descripcion='Doctor', img='doctor.jpg'))
usuarios.append(Usuario(id=6, username='MH69', password='020299', nombre='Merlin', apellido='Hernandez', edad=24, descripcion='Streamer/Desarrolladora', img='streamerM.jpg'))
usuarios.append(Usuario(id=7, username='MC81', password='258369', nombre='Monica', apellido='Canizales', edad=23, descripcion='Doctora', img='doctora.jpg'))
usuarios.append(Usuario(id=8, username='CM32', password='963852', nombre='Carlos', apellido='Mendez', edad=35, descripcion='Policia', img='policia.jpg'))
usuarios.append(Usuario(id=9, username='RM78', password='159236', nombre='Roxana', apellido='Moran', edad=25, descripcion='Modelo', img='modelo.jpg'))
usuarios.append(Usuario(id=10, username='SC77', password='159478', nombre='Sofia', apellido='Castro', edad=28, descripcion='Secretaria', img='secretaria.jpg'))