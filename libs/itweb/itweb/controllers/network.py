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
from itweb.model import DBSession, metadata, Network

class NetworkController(CrudRestController):
    # The predicate that must be met for all the actions in this controller:
    allow_only = has_permission('manage',
                                msg=l_('Only for people with the "manage" permission'))
    model = Network

    class new_form_type(AddRecordForm):
        __model__ = Network
        __omit_fields__ = ['id', 'version', 'timestamp', 'user_id', 'ips']

    class edit_form_type(EditableForm):
        __model__ = Network
        __omit_fields__ = ['id', 'version', 'timestamp', 'user_id', 'ips']

    class edit_filler_type(EditFormFiller):
        __model__ = Network

    class table_type(TableBase):
        __model__ = Network
        __omit_fields__ = ['id', 'version', 'timestamp', 'user_id', 'ips']

    class table_filler_type(TableFiller):
        __model__ = Network
