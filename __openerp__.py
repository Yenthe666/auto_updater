# -*- coding: utf-8 -*-
{
    'name': "auto_updater",

    'summary': """
        Automatic database updater""",

    'description': """
        Automaticly updates your Odoo database whenever you want it to.
        It first does a git fetch origin and then a git rebase --autostash
    """,

    'author': "Yenthe Van Ginneken",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'schedulers/auto_update_planner.xml',
    ],
}
