{
    'name': "custom_products_report",

    'summary': """
        As developer we've been asked to develop customized reports involving the 
        the information about our products""",

    'description': """
        As developer we've been asked to develop customized reports involving the 
        the information about our products
    """,

    'author': "Freddy Ibargollin Gavilan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp_training'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        # 'views/views.xml',
        'report/custom_product_report.xml',
        'report/product_template_state_list_template.xml',
        'wizard/custom_product_report_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
# -*- coding: utf-8 -*-
