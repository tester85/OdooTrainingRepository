# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'
    _description = 'Change de sequence for the new Product lot created '

    name = fields.Char(
        'Lot/Serial Number', default=lambda self: self.env['ir.sequence'].next_by_code('stock.lot.serial'),
        required=True, help="Unique Lot/Serial Number")

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain=lambda self: self._domain_product_id(), required=True, check_company=True)

    @api.onchange('product_id')
    def _serial_lot(self):
        # formatting date to match 2 numbers 'month->[01] Year->[22]'
        date = datetime.now()
        month_year = date.strftime('%m%y')
        # Count amount of products who has a defined lot_prefix
        if self.product_id.lot_prefix:
            lot_quantity_sequence = self.env['stock.production.lot'].search([]).filtered(
                lambda x: x.product_id == self.product_id)
            # Asign new sequence to product lot
            new_name = str(self.product_id.lot_prefix) + '{:0>2}'.format(
                str(len(lot_quantity_sequence) + 1)) + month_year
            self.name = new_name
        elif self.product_id.lot_prefix is False:
            self.name
            # @ToDo - Practice exceptions control
            # return {
            #     'warning': {'title': "Warning",
            #           'message': "The product does not have a valid lot prefix.\n Define a new one by selecting "
            #                            "alongside the product."},
            # }
    # @api.depends('product_id')
