{
    'name': 'Edificio Pe',
    'version': '16.1.0',
    'website': 'https://dcodepe.pe',
    'category': 'Administracion',
    'author': "Cesar Huamani Dcode",
    'sequence': 60,
    'summary': 'Module for Building & Department',
    'depends': [
        'base',
        'contacts',
    ],
    'description': "",
    'data': [
        # Aqui van las rutas de las vistas del modulo
        "views/cuota_views.xml",
          "views/member_view.xml",
        #"views/session_views.xml",
        #"views/res_partner_views.xml",
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
