# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Module Sales',
    'version': '1.1',
    'category': 'Sales/Sales',
    'summary': 'Add New Origin Country Sales',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['sale_management'],
    'data': [
        #'security/sale_security.xml',
        #'security/ir.model.access.csv',
        'report/custom_sales_template.xml',
        'views/custom_sale_order.xml',
    ],
    'demo': [
        'data/product_product_demo.xml',
        'data/sale_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
