# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'dgj_videoclub.pelicula'
    _description = 'Película'

    name = fields.Char('Título', required=True, help="Introduce el título de la película")
    precio_alquiler = fields.Float('Precio de alquiler', required=True, help="Introduce el precio de alquiler de la película")
    director = fields.Char('Director', help="Introduce el director de la película")
    fecha_lanzamiento = fields.Date('Fecha de lanzamiento', help="Introduce la fecha de lanzamiento de la película")

    
