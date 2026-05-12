# -*- coding: utf-8 -*-
{
    'name': 'POS Full Screen Button',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Add a full screen button to the POS navbar next to the search bar',
    'description': 'This module adds a button in the POS header to easily toggle full screen mode.',
    'author': 'Custom',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_full_screen/static/src/js/navbar_patch.js',
            'pos_full_screen/static/src/xml/navbar_patch.xml',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
