import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(100))
#     street_number = Column(String(100))
#     post_code = Column(String(100), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False,)
    name = Column(String(100), )
    last_name = Column(String(100), )
    email = Column(String(100), nullable=False, unique=True)

class Peoples(Base):
    __tablename__ = 'Peoples'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False, unique=True)
    height = Column(Integer, nullable=False,)
    mass = Column(Integer, nullable=False,)
    hair_color = Column(String(100), nullable=False,)
    skin_color = Column(String(100), nullable=False,)
    eye_color = Column(String(100), nullable=False,)
    birth_year = Column(String(100), nullable=False,)
    gender = Column(String(100), nullable=False,)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False, unique=True)
    rotation_period = Column(Integer, nullable=False,)
    orbital_period = Column(Integer, nullable=False,)
    diameter = Column(Integer, nullable=False,)
    climate = Column(String(100), )
    gravity = Column(String(100), )
    terrain = Column(String(100), )
    surface_water = Column(Integer, nullable=False,)
    population = Column(Integer, nullable=False,)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    Vehicles_id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False, unique=True)
    model = Column(String(100), nullable=False, unique=True)
    manufacturer = Column(String(100), )
    cost_in_credits = Column(Integer, nullable=False,)
    length = Column(Integer, nullable=False,)
    max_atmosphering_speed = Column(Integer, nullable=False,)
    crew = Column(Integer, nullable=False,)
    passengers = Column(Integer, nullable=False,)
    cargo_capacity = Column(Integer, nullable=False,) 
    consumables = Column(String(100), )
    vehicle_class = Column(String(100), )

class Favorite_peoples(Base):
    __tablename__ = 'Favorite_peoples'
    id = Column(Integer, ForeignKey('Peoples.id'))
    user_id = Column(Integer, ForeignKey('Users.id'), primary_key=True,)

class Favorite_planets(Base):
    __tablename__ = 'Favorite_planets'
    id = Column(Integer, ForeignKey('Planets.id'))
    user_id = Column(Integer, ForeignKey('Users.id'), primary_key=True,)

class Favorite_vehicles(Base):
    __tablename__ = 'Favorite_vehicles'
    id = Column(Integer, ForeignKey('Vehicles.id'))
    user_id = Column(Integer, ForeignKey('Users.id'), primary_key=True,)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')