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

class vehiculo(osv.Model):

    _name = 'vehiculo'
    _description = 'Modelo para vehiculos'
 
    _columns = {
            'name':fields.char('Matricula', size=9, required=True),
            'marca':fields.selection([
            ('bmw','BMW'),
            ('ford','FORD'),
            ('mercedes','MERCEDES'),
            ('audi','AUDI'),
            ('seat','SEAT'),
            ('toyota','TOYOTA'),
            ('peugeot','PEUGEOT'),],'Marca',required=True),
            'modelo':fields.char('Modelo', size=60, required=True),
            'tasacion':fields.float("Tasacion",required=True),
            'combustible':fields.selection([
            ('gasolina','Gasolina'),
            ('diesel','Diesel'),
            ('electrico','Electrico'),], 'Tipo de combustible'),
            'plazas':fields.integer("Numero de plazas")
        }
vehiculo()