# -*- coding: utf-8 -*-
{
    'name': "Sổ liên lạc điện tử",

    'summary': """Chia Nhân Sự và Phòng ban trong công ty""",

    'description': """
        Chia Nhân Sự và Phòng ban trong công ty
    """,

    'author': "BMSGROUP GLOBAL",
    'website': "http://www.bmsgroupglobal.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'BMS APP',
    'version': '1.1',

    # any module necessary for this one to work correctly
    # 'depends': ['crm','product','sale','sale_crm'],

    # always loaded
    'data': [
        'views/user_groups.xml',
        'security/ir.model.access.csv',
        'views/giaoanchinhsua.xml',
        'views/form.xml',
        'views/tree.xml',
        'views/baocao.xml',
    ],
}
