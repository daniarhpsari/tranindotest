# -*- coding: utf-8 -*-
# Part of Odoo Falinwa Edition. See LICENSE file for full copyright and licensing details.
{
    'name': 'Falinwa Tranindo Extention',
    'version': '15.0.1.0.0',
    'author': 'Falinwa Limited',
    'summary': 'Module to handle tranindo extention from falinwa',
    'category': 'Falinwa Tranindo Extention',
    'website': "https://falinwa.com",
    'description':
    '''
        Module to handle tranindo extention from falinwa
    ''',
    'depends': [
        'sale',
        'sale_stock',
        'account',
        'stock',
    ],
    'data': [
        # Form File
        'views/account_move_views.xml',
        'views/sale_order_views.xml',
        'views/res_company_views.xml',
        # Report File
        'report/tranindo_report_footer_header.xml',
        'report/tranindo_report_sj_letter_header_footer.xml',
        'report/tranindo_voucher_footer_header.xml',
        'report/layouts.xml',
        'report/sj_transfers_c5.xml',
        'report/sj_letters_c5.xml',
        'report/voucher_c5.xml',
        'report/voucher_a4.xml',
        # 'report/c5_report.xml',
        # 'e_faktur/e_faktur_account_move_view.xml',
        # 'e_faktur/e_faktur_res_partner_view.xml',
    ],
    'css': [],
    'js': [],
    'installable': True,
    'active': False,
    'application': False,
}
