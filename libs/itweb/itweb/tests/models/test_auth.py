# -*- coding: utf-8 -*-
"""Test suite for the TG app's models"""
from nose.tools import eq_

from itweb import model
from itweb.tests.models import ModelTest

class TestGroup(ModelTest):
    """Unit test case for the ``Group`` model."""
    klass = model.Group
    attrs = dict(
        group_name = u"test_group",
        display_name = u"Test Group"
        )

    def test_obj_repr(self):
        """The obj has a proper string representation"""
        eq_(repr(self.obj), "<Group: name=test_group>")

    def test_obj_unicode(self):
        """The obj can be converted to a unicode string"""
        eq_(unicode(self.obj), u"test_group")

class TestUser(ModelTest):
    """Unit test case for the ``User`` model."""
    
    klass = model.User
    attrs = dict(
        user_name = u"ignucius",
        email_address = u"ignucius@example.org"
        )

    def test_obj_creation_username(self):
        """The obj constructor must set the user name right"""
        eq_(self.obj.user_name, u"ignucius")

    def test_obj_creation_email(self):
        """The obj constructor must set the email right"""
        eq_(self.obj.email_address, u"ignucius@example.org")

    def test_no_permissions_by_default(self):
        """User objects should have no permission by default."""
        eq_(len(self.obj.permissions), 0)

    def test_getting_by_email(self):
        """Users should be fetcheable by their email addresses"""
        him = model.User.by_email_address(u"ignucius@example.org")
        eq_(him, self.obj)

    def test_obj_repr(self):
        """The obj has a proper string representation"""
        eq_(repr(self.obj), "<User: name=u'ignucius', email=u'ignucius@example.org', display=None>")

    def test_obj_unicode(self):
        """The obj can be converted to a unicode string"""
        eq_(unicode(self.obj), u"ignucius")


class TestPermission(ModelTest):
    """Unit test case for the ``Permission`` model."""
    
    klass = model.Permission
    attrs = dict(
        permission_name = u"test_permission",
        description = u"This is a test Description"
        )
