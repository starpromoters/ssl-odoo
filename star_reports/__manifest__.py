{
    'name': 'Star-Reports',
    'version': '15.0.1',
    'category': '',
    'summary': 'Star-Reports',
    
    'author': 'SSL',
    'website': '',
    'maintainer': '',

    'depends': ['sale','star_extensions','stock','account'],
    'data': [
    'reports/sale_report.xml',
    'reports/delivery_slip.xml',
    'reports/account_report.xml',
    'reports/sale_report_templates.xml',
    'reports/report_deliveryslip.xml',
    'reports/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
    'price': 110.00,
    'currency': 'EUR',
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
}
