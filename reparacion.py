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

class reparacion(osv.Model):
 
    _name = 'reparacion'
    _description = 'Modelo de reparacion de vehiculos'
    _columns = {
            'name':fields.char('Nombre', size=30 , required=True),
            'vehiculo_id':fields.many2one('vehiculo', 'Vehiculo', required=True), 
            'descripcion': fields.text('Descripcion'), 
            'coste':fields.float("Importe",required=True),
            'fecharep': fields.datetime('Fecha reparación',required=True, autodate = True),
            'talleres_ids': fields.many2many('taller','taller_reparacion_rel', 'reparacion_id', 'taller_id', 'Talleres reparacion'),
            
         }
reparacion()