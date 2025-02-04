# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'dgj_videoclub.cliente'
    _description = 'Cliente'

    name= fields.Char('Nombre y Apellidos', required=True, help="Introduzca el nombre y apellidos del cliente")
    telefono = fields.Integer('Teléfono', help="Introduzca el teléfono del cliente")
    correo_electronico = fields.Char('Correo electrónico', help="Introduzca el correo electrónico del cliente")
    direccion = fields.Char('Dirección', help="Introduzca la dirección del cliente")
    