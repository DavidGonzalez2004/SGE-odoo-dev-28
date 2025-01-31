# -*- coding: utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    name = fields.Char('Título',required=True, help="Introduce el título del libro")
    precio = fields.Float('Precio', help="Introduce el precio")
    ejemplares = fields.Integer('Ejemplares', help="Introduce el número de ejmplares en inventario")
    fecha_compra = fields.Date('Fecha de compra', help="Introduce fecha de compra")
    segmano = fields.Boolean('Segunda mano', help="Marca si es de segunda mano")
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado', default='0')