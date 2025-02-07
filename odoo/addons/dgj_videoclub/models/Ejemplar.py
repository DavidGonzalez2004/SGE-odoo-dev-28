# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ejemplar(models.Model):
    _name = 'dgj_videoclub.ejemplar'
    _description = 'Ejemplar'

    numero_ejemplar = fields.Integer('Número de ejemplar', required=True, help="Introduzca el número del ejemplar")
    formato = fields.Selection([
        ('0', 'VHS'),
        ('1', 'DVD'),
        ('2', 'BLURAY')
    ], string='Formato')
    