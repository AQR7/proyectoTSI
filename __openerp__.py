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

{
    "name": "QuintoCar",
    "version": "1.0",
    "depends": ["base"],
    "author": "Grupo 6",
    "category": "QuintoCar",
    "description": """
    Compra-venta de vehiculos de segunda mano.
    """,
    "init_xml": [],
    'data': ['vehiculo_view.xml','empleado_view.xml','cliente_view.xml','reparacion_view.xml','taller_view.xml','compra_view.xml','proveedor_view.xml','empleado_workflow.xml','compra_workflow.xml','venta_view.xml','venta_workflow.xml','extras_view.xml'],
    'demo_xml': ["QUINTOCAR_demo.xml"],
    'installable': True,
    'active': False
}
