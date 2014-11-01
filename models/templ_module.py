# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api, _
from openerp.osv import osv
from openerp.osv import fields
from operator import itemgetter
import logging

_logger = logging.getLogger(__name__)

class module_model(osv.osv):
    _inherit = 'module.model'
    _columns = {
        'campo': fields.char('nombre', size=64, help="Website of Partner or Company", select=True),
   }

module_model()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
