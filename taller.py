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

class taller(osv.Model):

    _name = 'taller'
    _description = 'Taller de reparaciones'
 
    _columns = {
            'name':fields.char('Nombre', size=30, required=True),
            'cif':fields.char('CIF',size=9,required=True),
            'provincia':fields.char('Provincia', size=30, required=False),
            'direccion':fields.char('Direccion', size=60, required=True),
            'especializado':fields.boolean('Taller especializado'), 
            'fechaApertura':fields.datetime('Fecha apertura',required=True, autodate = True),
            'reparaciones_ids': fields.many2many('reparacion','taller_reparacion_rel', 'taller_id', 'reparacion_id', 'Reparaciones del taller'),



        }
taller()