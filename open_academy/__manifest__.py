{
    'name': 'Open academy',
    'version': '16.1.0',
    'website': 'https://recursostecnologicos.pe',
    'category': 'Education',
    'author': "Josue Rodriguez - Recursos Tecnologicos",
    'sequence': 50,
    'summary': 'Module for learn Odoo and Python',
    'depends': [
        'base',
        'contacts',
        'purchase'
    ],
    'description': "",
    'data': [
        # Aqui van las rutas de las vistas del modulo
        "views/course_views.xml",
        "views/session_views.xml",
        "views/res_partner_views.xml",
        "security/ir.model.access.csv",
    ],
    'qweb': [
        # Aqui van las rutas de las vistas qweb

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
