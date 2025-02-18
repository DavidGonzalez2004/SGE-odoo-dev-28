# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'dgj_videoclub.categoria'
    _description = 'Categoría'

    name = fields.Char('Nombre', required=True, help="Introduzca el nombre de la categoría")
    descripcion = fields.Char('Descripción', help="Introduzca la descripción de la categoría")

    pelicula_ids = fields.Many2many('dgj_videoclub.pelicula', relation="dgj_videoclub_categoria_pelicula_rel", string='Películas')