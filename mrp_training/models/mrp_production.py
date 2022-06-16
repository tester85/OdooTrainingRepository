# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class MrpProduction(models.Model):
    _name = 'mrp.production'
    _inherit = [_name]

    lot_prefix = fields.Char(related="product_id.lot_prefix")
