#  -*- coding: utf-8 -*-
#  Part of Odoo. See LICENSE file for full copyright and licensing details.
#
from odoo import api, fields, models, _


class CustomProductReportWizard(models.TransientModel):
    _name = 'product.report.wizard'
    _description = 'Class to generate custom products reports'

    product_id = fields.Many2one('product.template', 'Product', check_company=True,
                                 domain="[('type', '!=', 'service')]")
    # product_state = fields.Selection(related='product_id.state', readonly=True)
    state = fields.Selection([
        ('prototype', 'Prototype'),
        ('in_use', 'En uso'),
        ('deprecated', 'Descartado')], 'State')

    report = fields.Selection([
        ('all', 'All Products'),
        ('group_state', 'Products Grouped by state'),
        ('state', 'Especific state')], 'State', default='all')

    # Switch between reports
    def action_print_report(self):
        self.ensure_one()
        if self.report == 'all':
            return self._action_print_report_all()
        elif self.report == 'group_state':
            return self._action_print_report_all()
        else:
            return self._action_print_report_filtered_state()

    # List all product and his states
    def _action_print_report_all(self):
        product_list_read = self.env['product.template'].search_read([])
        data = {
            # 'product_list': product_list_read
        }
        return self.env.ref('custom_products_report.action_report_product_state_list').report_action(self, data)

    # List all product filtering their states
    def _action_print_report_filtered_state(self):
        product_list_filtered = self.env['product.template'].search_read([('state', '=', self.read()[0]['state'])])
        data = {
            'product_list': product_list_filtered
        }
        return self.env.ref('custom_products_report.action_report_product_state_list').report_action(self, data)
