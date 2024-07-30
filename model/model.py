from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            Database.__instance = self
            # Asegúrate de que la cadena de conexión es correcta
            self.engine = create_engine('mysql+pymysql://root:123456@localhost/JyV', echo=True)
            self.Base = declarative_base()
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()

    def get_session(self):
        return self.session

# Define las clases ORM después de la definición de la clase Database
Base = Database.get_instance().Base

class Puesto(Base):
    __tablename__ = 'Puestos'
    id_puesto = Column(Integer, primary_key=True, autoincrement=True)
    puesto = Column(String(50))
    # Definir la relación con la clase Perfil
    perfiles = relationship("Perfil", back_populates="puesto")


class Perfil(Base):
    __tablename__ = 'Perfil'
    id_perfil = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellidoPaterno = Column(String(50))
    apellidoMaterno = Column(String(50))
    telefono = Column(String(20))
    correo_electronico = Column(String(100))
    direccion = Column(String(255))
    id_puesto = Column(Integer, ForeignKey('Puestos.id_puesto'))
    puesto = relationship("Puesto", back_populates="perfiles")

class CuestionarioJung(Base):
    __tablename__ = 'Cuestionario_jung'
    id_cuestionario = Column(Integer, primary_key=True, autoincrement=True)
    id_perfil = Column(Integer, ForeignKey('Perfil.id_perfil'))
    id_puesto = Column(Integer, ForeignKey('Puestos.id_puesto'))
    seccion = Column(String(50))
    puntos = Column(Integer)

class CategoriaJung(Base):
    __tablename__ = 'Categoria_Jung'
    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    id_perfil = Column(Integer, ForeignKey('Perfil.id_perfil'))
    id_puesto = Column(Integer, ForeignKey('Puestos.id_puesto'))
    categoria = Column(String(50))

class ComparacionSecciones(Base):
    __tablename__ = 'Comparacion_secciones'
    id_comparacion = Column(Integer, primary_key=True, autoincrement=True)
    id_perfil = Column(Integer, ForeignKey('Perfil.id_perfil'))
    id_puesto = Column(Integer, ForeignKey('Puestos.id_puesto'))
    seccion_mayor = Column(String(50))
    puntos_seccion_mayor = Column(Integer)

class Pregunta(Base):
    __tablename__ = 'Preguntas'
    id_pregunta = Column(Integer, primary_key=True, autoincrement=True)
    enunciado = Column(String(255), nullable=False)
    opciones = relationship("OpcionRespuesta", back_populates="pregunta")


class OpcionRespuesta(Base):
    __tablename__ = 'Opciones_respuesta'
    id_opcion = Column(Integer, primary_key=True, autoincrement=True)
    id_pregunta = Column(Integer, ForeignKey('Preguntas.id_pregunta'))
    opcion = Column(CHAR(1), nullable=False)
    respuesta_texto = Column(String(255), nullable=False)
    pregunta = relationship("Pregunta", back_populates="opciones")


class RespuestaVark(Base):
    __tablename__ = 'Respuestas_vark'
    id_respuesta = Column(Integer, primary_key=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey('Perfil.id_perfil'))
    id_pregunta = Column(Integer, ForeignKey('Preguntas.id_pregunta'))
    respuesta = Column(CHAR(1), nullable=False)

class ResultadoVark(Base):
    __tablename__ = 'Resultado_vark'
    id_resultado = Column(Integer, primary_key=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey('Perfil.id_perfil'))
    V = Column(Integer, nullable=False)
    A = Column(Integer, nullable=False)
    R = Column(Integer, nullable=False)
    K = Column(Integer, nullable=False)
    
class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    matricula = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellidoPaterno = Column(String(100), nullable=False)
    apellidoMaterno = Column(String(100), nullable=False)
    contrasena = Column(String(255), nullable=False)
    usuario = Column(String(50), nullable=False)
    correo = Column(String(100), nullable=False)

# Setup database connection and create tables
def setup_database():
    db_instance = Database.get_instance()
    db_instance.Base.metadata.create_all(db_instance.engine)

if __name__ == '__main__':
    setup_database()
