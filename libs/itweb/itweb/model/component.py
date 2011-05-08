# -*- coding: utf-8 -*-
"""Component module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
from sqlalchemy.orm import relation, backref

from itweb.model import DeclarativeBase, metadata, DBSession

class ComponentType(DeclarativeBase):
    __tablename__ = 'componenttypes'

    #{ Columns

    id = Column(Integer, primary_key=True)

    ctype = Column(Unicode(255), nullable=False)

    #}

class Component(DeclarativeBase):
    __tablename__ = 'components'

    #{ Columns

    id = Column(Integer, primary_key=True)

    ctype_id = Column(Integer, ForeignKey('componenttypes.id'))

    ctype = relation(ComponentType, backref=backref('components', order_by=id))

    manufacturer = Column(Unicode(255), nullable=False)

    description = Column(Unicode(255), nullable=False)

    model = Column(Unicode(255), nullable=False)

    sanitization = Column(Unicode(255), nullable=False)

    media = Column(Unicode(255), nullable=False)

    #}
