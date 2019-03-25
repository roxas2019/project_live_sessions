# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomModel(models.Model):
    _name = 'custom.module'
    _rec_name = 'name'
    _description = 'Custom Module'

    name = fields.Char(string="Name", required=False, )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=False, )
