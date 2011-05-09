# -*- coding: utf-8 -*-
"""Network model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.orm import relation, backref

from itweb.model import DeclarativeBase, metadata, DBSession
from itweb.lib.history_meta import VersionedMeta, VersionedListener


class Network(DeclarativeBase):
    __metaclass__ = VersionedMeta
    __tablename__ = 'networks'

    #{ Columns

    id = Column(Integer, primary_key=True)

    netaddr = Column(String(100), nullable=False)

    prefix = Column(String(100), nullable=False)

    #}

class IPAddress(DeclarativeBase):
    __metaclass__ = VersionedMeta
    __tablename__ = 'ips'

    #{ Columns

    id = Column(Integer, primary_key=True)

    ipaddr = Column(String(100), nullable=False)

    mac = Column(String(100), nullable=True)

    network_id = Column(Integer, ForeignKey('networks.id'))

    network = relation(Network, backref=backref('ips', order_by=id))

    #}

class DNSEntry(DeclarativeBase):
    __metaclass__ = VersionedMeta
    __tablename__ = 'dnsentries'
    __table_args__ = (
            UniqueConstraint('ipaddr_id', 'entry', 'type'),
            None,
            {}
            )

    #{ Columns

    id = Column(Integer, primary_key=True)

    ipaddr_id = Column(Integer, ForeignKey('ips.id'))

    ipaddr    = relation(IPAddress, backref=backref('dnsentries', order_by=id))

    entry = Column(String(255), nullable=False)

    type = Column(Integer, nullable=False)

    #}
