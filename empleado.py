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

class empleado(osv.Model):
    _name = 'empleado'
    _description = 'Empleado de QUINTOCAR'
    
    _columns = {
            'name':fields.char('nombre del empleado', size = 15, required = True),
            'apellidos':fields.char('apellidos del empleado', size = 60, required = True),
            'DNI':fields.char('dni empleado', size = 10, required = True),
            'numero ventas':fields.integer('numero de ventas del empleado', required = True),
            'salario':fields.float('salario del empleado', required = True)  
            }
empleado()