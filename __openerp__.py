# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2014 OpenERP - Ozono informatica.
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
{
	'name':	 'Invoice internal number cleaner',
	'version':  '1.0',
	'author':   'Ozono informatica',
	'category': 'Argentina',
	'website':  'www.ozonoinformatica.com.ar',
	'license':  'AGPL-3',
	'description': """
Este modulo permite blanquear el numero interno de la factura una vez que ha sido asigndo al validar la factura.
Para esto la factura debe estar en borrador.
""",
	'depends': [
        'account',
	],
	'init_xml': [],
	'demo_xml': [],
	'test': [],
	'data': ['account_invoice_view.xml',],
	'update_xml': [],
	'active': False,
	'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
