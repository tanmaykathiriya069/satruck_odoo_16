{
    'name': 'SA-Truck',
    'author': 'Entrivis Tech. PVT. LTD.',
    'description':'This App For Driver Activity and Expenses',
    'website': 'www.satruck.com',
    'version': '1.0',
    'depends': ['base','fleet','sale','report_xlsx'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/check.list.csv',
        'data/city.city.csv',
        'wizard/xlsx_report.xml',
        'wizard/pdf_report_wizard_view.xml',
        'wizard/pdf_report_using_quary_wizard.xml',
        'wizard/pdf_report_wizard_view_temp.xml',
        'report/sa_truck_report.xml',
        'report/invoice_report_inherit.xml',
        'report/sa_truck_xls_report.xml',
        'views/account_move.xml',
        'views/email_temp.xml',
        'views/sa_truck.xml',
        'views/actions_file.xml',
        'views/menu_file.xml',
        'views/configuration.xml',
        'views/res_partner_.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}