# -*- coding: utf-8 -*-
"""Component controller module"""

# turbogears imports
from tgext.crud import CrudRestController
from tg import expose, tmpl_context
#from tg import redirect, validate, flash

# third party imports
from sprox.formbase import AddRecordForm, EditableForm
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller, EditFormFiller
from tw.forms.fields import TextField
from formencode.validators import NotEmpty
#from pylons.i18n import ugettext as _
#from repoze.what import predicates
from repoze.what.predicates import has_permission
from pylons.i18n import ugettext as _, lazy_ugettext as l_

# project specific imports
from itweb.lib.base import BaseController
from itweb.model import DBSession, metadata, ComponentType, Component

class ComponentTypeController(CrudRestController):
    # The predicate that must be met for all the actions in this controller:
    allow_only = has_permission('manage',
                                msg=l_('Only for people with the "manage" permission'))
    model = ComponentType

    class new_form_type(AddRecordForm):
        __model__ = ComponentType
        __omit_fields__ = ['components']

    class edit_form_type(EditableForm):
        __model__ = ComponentType
        __omit_fields__ = ['id', 'components']

    class edit_filler_type(EditFormFiller):
        __model__ = ComponentType

    class table_type(TableBase):
        __model__ = ComponentType
        __omit_fields__ = ['id', 'components']

    class table_filler_type(TableFiller):
        __model__ = ComponentType

class ComponentController(CrudRestController):
    # The predicate that must be met for all the actions in this controller:
    allow_only = has_permission('manage',
                                msg=l_('Only for people with the "manage" permission'))
    model = Component

    class new_form_type(AddRecordForm):
        __model__ = Component
        __omit_fields__ = ['id']
        __field_attrs__ = {'description':{'rows':'2'}}
        __field_order__ = ['type', 'manufacturer', 'model', 'description', 'sanitization', 'media']
        __required_fields__ = ['type', 'manufacturer', 'description']
        description = TextField
        sanitization = TextField
        media = TextField
        type = NotEmpty()

    class edit_form_type(EditableForm):
        __model__ = Component
        __omit_fields__ = ['id']
        __field_attrs__ = {'description':{'rows':'2'}}
        __field_order__ = ['type', 'manufacturer', 'model', 'description', 'sanitization', 'media']
        __required_fields__ = ['type', 'manufacturer', 'description']
        description = TextField
        sanitization = TextField
        media = TextField
        type = NotEmpty()

    class edit_filler_type(EditFormFiller):
        __model__ = Component

    class table_type(TableBase):
        __model__ = Component
        __omit_fields__ = ['id', 'type_id']

    class table_filler_type(TableFiller):
        __model__ = Component
