class Usuario:
    def __init__(self, id, username, password, nombre, apellido, email, edad, descripcion, img, back, followers):
        self.id=id
        self.username=username
        self.password=password
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.edad=edad
        self.descripcion=descripcion
        self.img=img
        self.back=back
        self.followers=followers
    
    def __repr__(self) -> str:
        return f'<Usuario:{self.username}>' 

usuarios=[]
usuarios.append(Usuario(id=1, username='RB66', password='123456', nombre='Reaper', apellido='Borja', email='reaperhenrandez270@gmail.com', edad=23, descripcion='Streamer/Desarrollador', img='streamerH.jpg', back='streamerHback.jpg', followers='400k'))
usuarios.append(Usuario(id=2, username='JM98', password='654321', nombre='Jasmin', apellido='Molina', email='kerimhernandez9@gmail.com', edad=29, descripcion='Abogada', img='abogada.jpg', back='abogadaback.jpg', followers='50k'))
usuarios.append(Usuario(id=3, username='RR87', password='456789', nombre='Ricardo', apellido='Rodriguez', email='kerimhernandez9@gmail.com', edad=26, descripcion='Contador', img='contador.jpg', back='contadorback.jpg', followers='50k'))
usuarios.append(Usuario(id=4, username='GM65', password='987654', nombre='Gilberto', apellido='Molina', email='kerimhernandez9@gmail.com', edad=23, descripcion='Abogado', img='abogado.jpg', back='abogadoback.jpg', followers='60k'))
usuarios.append(Usuario(id=5, username='JP88', password='147258', nombre='Juan', apellido='Perez', email='kerimhernandez9@gmail.com', edad=45, descripcion='Doctor', img='doctor.jpg', back='doctorback.jpg', followers='250k'))
usuarios.append(Usuario(id=6, username='MH69', password='020299', nombre='Merlin', apellido='Hernandez', email='badgirl23x3@gmail.com', edad=24, descripcion='Streamer/Desarrolladora', back='streamerMback.jpg', img='streamerM.jpg', followers='500k'))
usuarios.append(Usuario(id=7, username='MC81', password='258369', nombre='Monica', apellido='Canizales', email='kerimhernandez9@gmail.com', edad=23, descripcion='Doctora', img='doctora.jpg', back='doctoraback.jpg', followers='75k'))
usuarios.append(Usuario(id=8, username='CM32', password='963852', nombre='Carlos', apellido='Mendez', email='kerimhernandez9@gmail.com', edad=35, descripcion='Policia', img='policia.jpeg', back='policiaback.jpg', followers='20k'))
usuarios.append(Usuario(id=9, username='RM78', password='159236', nombre='Roxana', apellido='Moran', email='kerimhernandez9@gmail.com', edad=25, descripcion='Modelo', img='modelo.jpg', back='modeloback.jpg', followers='1M'))
usuarios.append(Usuario(id=10, username='SC77', password='159478', nombre='Sofia', apellido='Castro', email='kerimhernandez9@gmail.com', edad=28, descripcion='Secretaria', img='secretaria.jpg', back='secretariaback.jpg', followers='120k'))