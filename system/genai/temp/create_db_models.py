# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class User(Base):
    """description: Represents a user in the cannabis safety application."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Preference(Base):
    """description: Stores user-specific preferences regarding cannabis."""
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source_of_plant = Column(String)
    percentage_of_thc = Column(Float)
    preferred_branding = Column(String)

class Allergy(Base):
    """description: Represents any allergies to certain additives."""
    __tablename__ = 'allergies'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserAllergy(Base):
    """description: Link table to associate users with allergies."""
    __tablename__ = 'user_allergies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    allergy_id = Column(Integer, ForeignKey('allergies.id'))

class OutletStore(Base):
    """description: Represents an outlet store location."""
    __tablename__ = 'outlet_stores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

class Pricing(Base):
    """description: Stores pricing information for different users and outlet stores."""
    __tablename__ = 'pricings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    outlet_store_id = Column(Integer, ForeignKey('outlet_stores.id'))
    price = Column(Float)

class Branding(Base):
    """description: Represents a cannabis brand."""
    __tablename__ = 'brandings'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserBranding(Base):
    """description: Link table to associate users with their preferred branding."""
    __tablename__ = 'user_brandings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    branding_id = Column(Integer, ForeignKey('brandings.id'))

class SourceOfPlant(Base):
    """description: Represents different sources of cannabis plants."""
    __tablename__ = 'source_of_plants'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserSourceOfPlant(Base):
    """description: Link table to associate users with their preferred source of cannabis plants."""
    __tablename__ = 'user_source_of_plants'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source_of_plant_id = Column(Integer, ForeignKey('source_of_plants.id'))

class ThcPercentage(Base):
    """description: Represents allowed THC percentages."""
    __tablename__ = 'thc_percentages'
    id = Column(Integer, primary_key=True)
    value = Column(Float)

class UserThcPercentage(Base):
    """description: Link table to associate users with their preferred THC percentage."""
    __tablename__ = 'user_thc_percentages'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    thc_percentage_id = Column(Integer, ForeignKey('thc_percentages.id'))


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    user1 = User(id=1, name="Alice", email="alice@example.com")
    user2 = User(id=2, name="Bob", email="bob@example.com")
    user3 = User(id=3, name="Charlie", email="charlie@example.com")
    user4 = User(id=4, name="David", email="david@example.com")
    preference1 = Preference(id=1, user_id=1, source_of_plant="GreenHaven", percentage_of_thc=18.5, preferred_branding="EcoCanna")
    preference2 = Preference(id=2, user_id=2, source_of_plant="SunGrowers", percentage_of_thc=22.0, preferred_branding="Cannaluxe")
    preference3 = Preference(id=3, user_id=3, source_of_plant="GreenHaven", percentage_of_thc=20.0, preferred_branding="NaturalHigh")
    preference4 = Preference(id=4, user_id=4, source_of_plant="FarmFresh", percentage_of_thc=15.0, preferred_branding="PurePlant")
    allergy1 = Allergy(id=1, name="Nuts")
    allergy2 = Allergy(id=2, name="Gluten")
    allergy3 = Allergy(id=3, name="Sulfites")
    allergy4 = Allergy(id=4, name="Dairy")
    user_allergy1 = UserAllergy(id=1, user_id=1, allergy_id=1)
    user_allergy2 = UserAllergy(id=2, user_id=2, allergy_id=2)
    user_allergy3 = UserAllergy(id=3, user_id=3, allergy_id=3)
    user_allergy4 = UserAllergy(id=4, user_id=4, allergy_id=4)
    outlet_store1 = OutletStore(id=1, name="Downtown Dispensary", location="New York")
    outlet_store2 = OutletStore(id=2, name="Green Valley", location="Los Angeles")
    outlet_store3 = OutletStore(id=3, name="The Green House", location="Seattle")
    outlet_store4 = OutletStore(id=4, name="SunnyFields", location="San Francisco")
    pricing1 = Pricing(id=1, user_id=1, outlet_store_id=1, price=50.0)
    pricing2 = Pricing(id=2, user_id=2, outlet_store_id=2, price=45.0)
    pricing3 = Pricing(id=3, user_id=3, outlet_store_id=3, price=60.0)
    pricing4 = Pricing(id=4, user_id=4, outlet_store_id=4, price=55.0)
    branding1 = Branding(id=1, name="EcoCanna")
    branding2 = Branding(id=2, name="Cannaluxe")
    branding3 = Branding(id=3, name="NaturalHigh")
    branding4 = Branding(id=4, name="PurePlant")
    user_branding1 = UserBranding(id=1, user_id=1, branding_id=1)
    user_branding2 = UserBranding(id=2, user_id=2, branding_id=2)
    user_branding3 = UserBranding(id=3, user_id=3, branding_id=3)
    user_branding4 = UserBranding(id=4, user_id=4, branding_id=4)
    source_of_plant1 = SourceOfPlant(id=1, name="GreenHaven")
    source_of_plant2 = SourceOfPlant(id=2, name="SunGrowers")
    source_of_plant3 = SourceOfPlant(id=3, name="FarmFresh")
    source_of_plant4 = SourceOfPlant(id=4, name="UrbanFarm")
    user_source_of_plant1 = UserSourceOfPlant(id=1, user_id=1, source_of_plant_id=1)
    user_source_of_plant2 = UserSourceOfPlant(id=2, user_id=2, source_of_plant_id=2)
    user_source_of_plant3 = UserSourceOfPlant(id=3, user_id=3, source_of_plant_id=1)
    user_source_of_plant4 = UserSourceOfPlant(id=4, user_id=4, source_of_plant_id=3)
    thc_percentage1 = ThcPercentage(id=1, value=18.5)
    thc_percentage2 = ThcPercentage(id=2, value=22.0)
    thc_percentage3 = ThcPercentage(id=3, value=15.0)
    thc_percentage4 = ThcPercentage(id=4, value=10.0)
    user_thc_percentage1 = UserThcPercentage(id=1, user_id=1, thc_percentage_id=1)
    user_thc_percentage2 = UserThcPercentage(id=2, user_id=2, thc_percentage_id=2)
    user_thc_percentage3 = UserThcPercentage(id=3, user_id=3, thc_percentage_id=1)
    user_thc_percentage4 = UserThcPercentage(id=4, user_id=4, thc_percentage_id=3)
    
    
    
    session.add_all([user1, user2, user3, user4, preference1, preference2, preference3, preference4, allergy1, allergy2, allergy3, allergy4, user_allergy1, user_allergy2, user_allergy3, user_allergy4, outlet_store1, outlet_store2, outlet_store3, outlet_store4, pricing1, pricing2, pricing3, pricing4, branding1, branding2, branding3, branding4, user_branding1, user_branding2, user_branding3, user_branding4, source_of_plant1, source_of_plant2, source_of_plant3, source_of_plant4, user_source_of_plant1, user_source_of_plant2, user_source_of_plant3, user_source_of_plant4, thc_percentage1, thc_percentage2, thc_percentage3, thc_percentage4, user_thc_percentage1, user_thc_percentage2, user_thc_percentage3, user_thc_percentage4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
