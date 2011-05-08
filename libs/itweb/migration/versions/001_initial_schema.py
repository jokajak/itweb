from sqlalchemy import *
from sqlalchemy.orm import relation, backref
from migrate import *
from migrate import migrate_engine

metadata = MetaData(migrate_engine)
componenttypes_table = Table("componenttypes", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("type", Unicode(255), nullable=False)
                      )

components_table = Table("components", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("type_id", Integer, ForeignKey('componenttypes.id')),
                       Column("type", ComponentType, backref=backref('components', order_by=id)),
                       Column("manufacturer", Unicode(255), nullable=False),
                       Column("description", Unicode(255), nullable=False),
                       Column("model", Unicode(255), nullable=False),
                       Column("sanitization", Unicode(255), nullable=False),
                       Column("media", Unicode(255), nullable=False),
                      )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind migrate_engine
    # to your metadata
    meta.create_all()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.drop_all()
