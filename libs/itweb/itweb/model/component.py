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

    type = Column(Unicode(100), nullable=False)

    #}

class Component(DeclarativeBase):
    __tablename__ = 'components'
    __table_args__ = (
            UniqueConstraint('manufacturer', 'model'),
            None,
            {}
            )

    #{ Columns

    id = Column(Integer, primary_key=True)

    type_id = Column(Integer, ForeignKey('componenttypes.id'))

    type = relation(ComponentType, backref=backref('components', order_by=id))

    manufacturer = Column(Unicode(100), nullable=False)

    description = Column(Unicode(255), nullable=False)

    model = Column(Unicode(100), nullable=False)

    sanitization = Column(Unicode(255), nullable=False)

    media = Column(Unicode(255), nullable=False)

    #}
