# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MRP Training',
    'version': '1.0',
    'website': 'https://www.tester85.com',
    'category': 'Manufacturing/Manufacturing',
    'sequence': 56,
    'summary': 'Module for MRP Training',
    'depends': ['mrp', 'stock'],
    'description': """Module for MRP Training.""",
    'license': 'LGPL-3',
    'data': [
        'views/product_template_views.xml',
        'views/mrp_production_views.xml',
        'report/custom_production_order.xml',
        'report/custom_report_mrp_production_view.xml',
    ],
    'application': True,
}
