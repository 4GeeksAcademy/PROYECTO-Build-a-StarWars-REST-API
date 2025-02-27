
from flask_sqlalchemy import SQLAlchemy

baseDeDatos = SQLAlchemy()


class User(baseDeDatos.Model):
    __tablename__ = 'users'

    id = baseDeDatos.Column(baseDeDatos.Integer, primary_key=True)
    username = baseDeDatos.Column(baseDeDatos.String, unique=True, nullable=False)
    active = baseDeDatos.Column(baseDeDatos.Boolean())
    Favorito = baseDeDatos.relationship("Favorito", backref='user')

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            
        }
    
class Personaje(baseDeDatos.Model):
    __tablename__ ='personaje'
    id = baseDeDatos.Column(baseDeDatos.Integer, primary_key=True)
    name = baseDeDatos.Column(baseDeDatos.String(120), unique=True, nullable=False)
    specie = baseDeDatos.Column(baseDeDatos.String(200), nullable=False)
    height = baseDeDatos.Column(baseDeDatos.String, nullable=False)
    birth_year = baseDeDatos.Column(baseDeDatos.String, nullable=False)
    gender = baseDeDatos.Column(baseDeDatos.String, nullable=False)
    favoritos = baseDeDatos.relationship("Favorito", backref='personajes')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specie": self.specie,
            "height": self.height,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
    

    def save(self):
        baseDeDatos.session.add(self)
        baseDeDatos.session.commit()

    def update(self):
        baseDeDatos.session.commit()

    def delete(self):
        baseDeDatos.session.delete(self)
        baseDeDatos.session.commit()



class Planeta(baseDeDatos.Model):
    __tablename__ ='planetas'
    id = baseDeDatos.Column(baseDeDatos.Integer, primary_key=True)
    name = baseDeDatos.Column(baseDeDatos.String(120), unique=True, nullable=False)
    climate = baseDeDatos.Column(baseDeDatos.String(200), nullable=False)
    population = baseDeDatos.Column(baseDeDatos.String, nullable=False)
    terreno = baseDeDatos.Column(baseDeDatos.String, nullable=False)
    favoritos = baseDeDatos.relationship("Favorito", backref='planetas')
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terreno": self.terreno
        }
    
    def save(self):
        baseDeDatos.session.add(self)
        baseDeDatos.session.commit()

    def update(self):
        baseDeDatos.session.commit()

    def delete(self):
        baseDeDatos.session.delete(self)
        baseDeDatos.session.commit()


class Favorito(baseDeDatos.Model):
    __tablename__ ='favoritos'
    id = baseDeDatos.Column(baseDeDatos.Integer, baseDeDatos.ForeignKey('users.id'), primary_key=True)
    favorite_personajes = baseDeDatos.Column(baseDeDatos.Integer, baseDeDatos.ForeignKey('personajes.id'), primary_key=True)
    favs_planetas = baseDeDatos.Column(baseDeDatos.Integer, baseDeDatos.ForeignKey('planetas.id'), primary_key=True)

    def to_dict(self):
        return {
            "id": self.id,
            "favorite_personajes": self.favorite_personajes,
            "favs_planetas": self.favs_planetas,
            
        }
    def save(self):
        baseDeDatos.session.add(self)
        baseDeDatos.session.commit()

    def update(self):
        baseDeDatos.session.commit()

    def delete(self):
        baseDeDatos.session.delete(self)
        baseDeDatos.session.commit()
    
