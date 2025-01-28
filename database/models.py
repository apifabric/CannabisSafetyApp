# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 28, 2025 15:43:17
# Database: sqlite:////tmp/tmp.elRSiWazN1-01JJPS81EM1MHMDFTE6BYHQEJ1/CannabisSafetyApp/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Allergy(Base):  # type: ignore
    """
    description: Represents any allergies to certain additives.
    """
    __tablename__ = 'allergies'
    _s_collection_name = 'Allergy'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    UserAllergyList : Mapped[List["UserAllergy"]] = relationship(back_populates="allergy")



class Branding(Base):  # type: ignore
    """
    description: Represents a cannabis brand.
    """
    __tablename__ = 'brandings'
    _s_collection_name = 'Branding'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    UserBrandingList : Mapped[List["UserBranding"]] = relationship(back_populates="branding")



class OutletStore(Base):  # type: ignore
    """
    description: Represents an outlet store location.
    """
    __tablename__ = 'outlet_stores'
    _s_collection_name = 'OutletStore'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PricingList : Mapped[List["Pricing"]] = relationship(back_populates="outlet_store")



class SourceOfPlant(Base):  # type: ignore
    """
    description: Represents different sources of cannabis plants.
    """
    __tablename__ = 'source_of_plants'
    _s_collection_name = 'SourceOfPlant'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    UserSourceOfPlantList : Mapped[List["UserSourceOfPlant"]] = relationship(back_populates="source_of_plant")



class ThcPercentage(Base):  # type: ignore
    """
    description: Represents allowed THC percentages.
    """
    __tablename__ = 'thc_percentages'
    _s_collection_name = 'ThcPercentage'  # type: ignore

    id = Column(Integer, primary_key=True)
    value = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    UserThcPercentageList : Mapped[List["UserThcPercentage"]] = relationship(back_populates="thc_percentage")



class User(Base):  # type: ignore
    """
    description: Represents a user in the cannabis safety application.
    """
    __tablename__ = 'users'
    _s_collection_name = 'User'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PreferenceList : Mapped[List["Preference"]] = relationship(back_populates="user")
    PricingList : Mapped[List["Pricing"]] = relationship(back_populates="user")
    UserAllergyList : Mapped[List["UserAllergy"]] = relationship(back_populates="user")
    UserBrandingList : Mapped[List["UserBranding"]] = relationship(back_populates="user")
    UserSourceOfPlantList : Mapped[List["UserSourceOfPlant"]] = relationship(back_populates="user")
    UserThcPercentageList : Mapped[List["UserThcPercentage"]] = relationship(back_populates="user")



class Preference(Base):  # type: ignore
    """
    description: Stores user-specific preferences regarding cannabis.
    """
    __tablename__ = 'preferences'
    _s_collection_name = 'Preference'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    source_of_plant = Column(String)
    percentage_of_thc = Column(Float)
    preferred_branding = Column(String)

    # parent relationships (access parent)
    user : Mapped["User"] = relationship(back_populates=("PreferenceList"))

    # child relationships (access children)



class Pricing(Base):  # type: ignore
    """
    description: Stores pricing information for different users and outlet stores.
    """
    __tablename__ = 'pricings'
    _s_collection_name = 'Pricing'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    outlet_store_id = Column(ForeignKey('outlet_stores.id'))
    price = Column(Float)

    # parent relationships (access parent)
    outlet_store : Mapped["OutletStore"] = relationship(back_populates=("PricingList"))
    user : Mapped["User"] = relationship(back_populates=("PricingList"))

    # child relationships (access children)



class UserAllergy(Base):  # type: ignore
    """
    description: Link table to associate users with allergies.
    """
    __tablename__ = 'user_allergies'
    _s_collection_name = 'UserAllergy'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    allergy_id = Column(ForeignKey('allergies.id'))

    # parent relationships (access parent)
    allergy : Mapped["Allergy"] = relationship(back_populates=("UserAllergyList"))
    user : Mapped["User"] = relationship(back_populates=("UserAllergyList"))

    # child relationships (access children)



class UserBranding(Base):  # type: ignore
    """
    description: Link table to associate users with their preferred branding.
    """
    __tablename__ = 'user_brandings'
    _s_collection_name = 'UserBranding'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    branding_id = Column(ForeignKey('brandings.id'))

    # parent relationships (access parent)
    branding : Mapped["Branding"] = relationship(back_populates=("UserBrandingList"))
    user : Mapped["User"] = relationship(back_populates=("UserBrandingList"))

    # child relationships (access children)



class UserSourceOfPlant(Base):  # type: ignore
    """
    description: Link table to associate users with their preferred source of cannabis plants.
    """
    __tablename__ = 'user_source_of_plants'
    _s_collection_name = 'UserSourceOfPlant'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    source_of_plant_id = Column(ForeignKey('source_of_plants.id'))

    # parent relationships (access parent)
    source_of_plant : Mapped["SourceOfPlant"] = relationship(back_populates=("UserSourceOfPlantList"))
    user : Mapped["User"] = relationship(back_populates=("UserSourceOfPlantList"))

    # child relationships (access children)



class UserThcPercentage(Base):  # type: ignore
    """
    description: Link table to associate users with their preferred THC percentage.
    """
    __tablename__ = 'user_thc_percentages'
    _s_collection_name = 'UserThcPercentage'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    thc_percentage_id = Column(ForeignKey('thc_percentages.id'))

    # parent relationships (access parent)
    thc_percentage : Mapped["ThcPercentage"] = relationship(back_populates=("UserThcPercentageList"))
    user : Mapped["User"] = relationship(back_populates=("UserThcPercentageList"))

    # child relationships (access children)
