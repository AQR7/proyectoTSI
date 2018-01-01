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
            'name':fields.char('Nombre', size = 15, required = True),
            'apellidos':fields.char('Apellidos', size = 60, required = True),
            'DNI':fields.char('DNI', size = 10, required = True),
            'numero_ventas':fields.integer('Numero de ventas', required = True),
            'salario':fields.float('Salario', required = True),
            'provincia':fields.char('Provincia', size = 20, required = True),
            'nacionalidad_id': fields.many2one('res.country','Nacionalidad',required=True),
            'direccion': fields.char('Direccion', required=True),
            'correo': fields.char('Direccion de correo', size = 40, required = True),
            'compras_ids': fields.one2many('compra','empleado_id','Compras realizadas',required=False),
            'state':fields.selection([('solicitante','Solicitante'),('contratado','Contratado'),('despedido','Despedido')],'Estados')
            }
    _defaults = {'state': 'solicitante'}
    
empleado()