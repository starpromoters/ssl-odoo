{
    'name': 'Star-Extensions',
    'version': '19.0.1.0.0',
    'category': '',
    'summary': 'Star-Extensions',
    
    'author': 'SSL',
    'website': '',
    'maintainer': '',

    'depends': ['base', 'sale', 'stock', 'account', 'account_followup', 'account_reports'],
    'data': [
        'security/delivery_security.xml',
        'views/res_company_view.xml',
        'views/product.xml',
        'views/sale_view.xml',
        'views/picking_view.xml',
        'views/invoice.xml',
        'views/res_partner_view.xml',
        'data/followup_report.xml',

    ],
    'installable': True,
    'auto_install': False,
    'price': 110.00,
    'currency': 'EUR',
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
}
