# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Inherit product to add new requested fields'

    #
    # def _get_default_elem_type(self):
    #     return self.env.ref('buc_budget_fabrication.fabrication_expense_element_type_1').id or False

    # Add field on product form to add lot prefix
    # Use odoo behavior by default.
    lot_prefix = fields.Char(string='Lot Prefix')

    # Add a status bar on the product form to manage its life cycle.
    # Set the values: ‘Prototype’, ‘In use’ and ‘Deprecated’. By default, the Kanban view must be grouped by status.
    state = fields.Selection([
        ('prototype', 'Prototype'),
        ('in_use', 'in Use'),
        ('deprecated', 'Deprecated')], string='State', default='prototype', copy=False, tracking=True)

    def action_set_in_use(self):
        return super(ProductTemplate, self).write({'state': 'in_use'})

    def action_set_deprecated(self):
        return super(ProductTemplate, self).write({'state': 'deprecated', 'standard_price': 0.0})

    # When a product goes from ‘In use’ to ‘Deprecate’, set its cost to 0.
    @api.onchange('state')
    def _onchange_partner(self):
        if self.state == 'deprecated':
            self.standard_price = 0.0
        else:
            self.standard_price

