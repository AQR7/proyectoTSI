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
from openerp.osv.fields import many2one


class compra(osv.Model):

    _name = 'compra'
    _description = 'Modelo para compra'
 
    _columns = {
            'importe': fields.float('Importe'),
            'fecha': fields.datetime('Fecha',required=True, autodate = True), 
            'comentarios': fields.text('Comentarios'),
            'image': fields.binary('Contrato', help = 'Seleccionar imagen'),
            'proveedor_id': many2one('proveedor','Proveedor',required=True),
            'empleado_id': many2one('empleado','Empleado',required=True),
            'vehiculo_id': many2one('vehiculo','Vehiculo',required=True),#Al no existir relacion one2one en esta version usaremos many2one
            'state': fields.selection([('en_proceso','En proceso'),('finalizada','Finalizada')],'Estados')      
        }
    _defaults = {'state' : 'en_proceso'}
     
compra()