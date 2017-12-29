# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class proveedor(osv.Model):
    _name = 'proveedor'
    _description = 'Proveedor de QUINTOCAR'
    
    _columns = {
            'name':fields.char('CIF', size = 15, required = True),
            'nombre':fields.char('Nombre', size = 20, required = True),
            'direccion': fields.text('Direccion'),
            'telefono':fields.char('Telefono', size = 10, required = True),
            'tipo': fields.char('Tipo', size=64, required=False, readonly=False),
            'sede': fields.char('Sede', size=64, required=False, readonly=False),
            'correo': fields.char('Direccion de correo', size = 40, required = True),
            'compras_ids': fields.one2many('compra','proveedor_id', 'Ventas realizadas', required=False)            
            }
proveedor()