# -*- coding: utf-8 -*-
{
    'name': "Librería",

    'summary': "Módulo de ejemplo SGE",

    'description': """
Módulo de ejemplo SGE<br/>
Gestión de una librería
    """,

    'author': "IES El Cañaveral",
    'website': "https://site.educa.madrid.org/ies.elcanaveral.mostoles/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/categoria.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

