import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    favorite = relationship(Favorites)


class Planets(Base):
    __tablename__ = "planet"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    data_url = Column(String(250))


class Species(Base):
    __tablename__ = "specie"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    specie_name = Column(String(250))
    data_url = Column(String(250))


class Characters(Base):
    __tablename__ = "character"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    data_url = Column(String(250))


class Vehicles(Base):
    __tablename__ = "vehicle"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    data_url = Column(String(250))


class Starships(Base):
    __tablename__ = "starship"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    starship_name = Column(String(250))
    data_url = Column(String(250))


class Films(Base):
    __tablename__ = "film"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    section_name = Column(String(250))
    data_url = Column(String(250))
    starship_id = Column(Integer, ForeignKey("starship.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    specie_id = Column(Integer, ForeignKey("specie.id"))


class Sections(Base):
    __tablename__ = "section"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    section_name = Column(String(250))
    data_url = Column(String(250))
    favorite = relationship(Favorites)


class Favorites(Base):
    __tablename__ = "favorite"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("section.id"))
    uid = Column(Integer, nullable=False)
    user = relationship(Users)
    section = relationship(Sections)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, "diagram.png")
