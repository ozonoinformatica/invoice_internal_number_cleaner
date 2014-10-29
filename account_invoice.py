# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2014 Ozono informatica
# http://github.com/organizations/ozonoinformatica/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import osv
import logging

_logger = logging.getLogger(__name__)

class account_invoice(osv.osv):
    _inherit = "account.invoice"

    def clear_internal_number(self, cr, uid, ids, context={}):
        return_id = {}
        for invoice in self.browse(cr, uid, ids):
            if (invoice.internal_number):
                vals = {'internal_number': "",}
                return_id = self.write(cr, uid, invoice.id, vals)

        return return_id

account_invoice()