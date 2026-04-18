# -*- coding: utf-8 -*-
{
    'name': "AU - UDF Multi Company",

    'summary': """
        Manage multi-company settings and UDF company configuration.
    """,

    'description': """
        This module helps manage company master data and multi-company setup in Odoo.
    """,

    'author': "Andy Utomo",
    'website': "https://andyut.blogspot.com/",
    'image': ['images/main_screenshot.png'],
    'category': 'External Integration',
    'version': '18.1',
    'application':True,
    'license': 'LGPL-3',
 
    'depends': ['base'],
 
    'data': [ 
        'init_models/inherit_res_company.xml' 
        
    ],
   
}