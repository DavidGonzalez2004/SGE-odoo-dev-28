# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoria'
    

    name = fields.Char('Nombre', required=True, help="Introduzca nombre de categoria")
    descripcion = fields.Char('Descripcion')

    libro_ids = fields.One2many('sge_libreria.libro', 'categoria_id', string='Libros')