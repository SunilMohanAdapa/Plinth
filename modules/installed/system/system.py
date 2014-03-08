import os
import cherrypy
try:
    import simplejson as json
except ImportError:
    import json
from gettext import gettext as _
from filedict import FileDict
from auth import require
from plugin_mount import PagePlugin, FormPlugin
import cfg
from forms import Form
from model import User
from util import *

sys_dir = "modules/installed/sys"


class Sys(PagePlugin):
    order = 10
    def __init__(self, *args, **kwargs):
        PagePlugin.__init__(self, *args, **kwargs)
        self.register_page("sys")
        self.menu = cfg.main_menu.add_item(_("System"), "icon-cog", "/sys", 100)
	self.menu.add_item(_("Configure"), "icon-cog", "/sys/config", 10)
	self.menu.add_item(_("Users and Groups"), "icon-user", "/sys/users", 15)

    @cherrypy.expose
    def index(self):
        return self.fill_template(title=_("System Configuration"), main=_("""
        <p>In this section, you can control the %(product)s's
        underlying system, as opposed to its various applications and
        services.  These options affect the %(product)s at its most
        general level.  This is where you add/remove users, install
        applications, reboot, etc.</p>
        """ % {'product':cfg.product_name}))
