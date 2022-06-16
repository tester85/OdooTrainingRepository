# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class MrpProductProduction(models.Model):
    _inherit = 'mrp.production'
    _description = 'Add new field lot prefix to product form template '

    # Introduce a prefix to the product to conform a new lot number
    # If not added we're going to use odoo default one.
    lot_prefix = fields.Char(related="product_id.lot_prefix")
