# -*- coding: utf-8 -*-

{
    'name': 'My First Module',
    'version': '1.0',
    'website': 'https://cesarhuamani.pe',
    'category': 'Contacts',
    'author': "Cesar Huamani",
    'sequence': 50,
    'summary': 'My First Module as example',
    'depends': [
        'base',
        'stock',
    ],
    'description': "My First Module as example. You can add HTML code in this section.",
    'data': [
        # Aqui van las rutas de las vistas del modulo
        #"data/data.xml"
    ],
    'qweb': [
        # Aqui van las rutas de las vistas qweb REPORTES
        
    ],
    "assets": {
        "web.assets_backend": [
            # Aqui van los assets como css, js del backend que son parte del modulo
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
