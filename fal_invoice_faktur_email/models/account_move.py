import base64
from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    faktur_file = fields.Binary(string='Faktur Pajak')
    po_file = fields.Binary(string='Purchase Order')
    invoice_file = fields.Binary(string='Invoice')
    surat_jalan_file = fields.Binary(string='Surat Jalan')

    customer_reference = fields.Char(string='Customer Reference', compute='_get_customer_reference')

    agreement_file = fields.Many2many(
        'ir.attachment',
        'class_ir_attachments_rel',
        'class_id',
        'attachment_id',
        string="Agreement files",
        required=False)


    @api.depends('invoice_line_ids')
    def _get_customer_reference(self):
        for record in self:
            # record.customer_reference = ''
            for line in record.invoice_line_ids:
                for test in line.sale_Line_ids:
                    for result in test.order_id:
                        if result.client_order_ref:
                            record.customer_reference = result.client_order_ref
                        else:
                            record.customer_reference = ''

    def action_send_mail(self):
        template_id = self.env.ref('fal_invoice_faktur_email.email_template_invoice')

        faktur = {
            'name': "Faktur Report",
            'type': 'binary',
            'datas': self.faktur_file,
            # 'datas_fname': 'Faktur Report',
            'res_model': 'account.move',
        }

        purchase = {
            'name': "Purchase Report",
            'type': 'binary',
            'datas': self.po_file,
            # 'datas_fname': 'Purchase Report',
            'res_model': 'account.move',
        }

        invoice = {
            'name': "Invoice Report",
            'type': 'binary',
            'datas': self.invoice_file,
            # 'datas_fname': 'Invoice Report',
            'res_model': 'account.move',
        }

        surat_jalan = {
            'name': "Surat Jalan Report",
            'type': 'binary',
            'datas': self.surat_jalan_file,
            # 'datas_fname': 'Surat Jalan',
            'res_model': 'account.move',
        }

        faktur_id = self.env['ir.attachment'].create(faktur)
        purchase_id = self.env['ir.attachment'].create(purchase)
        invoice_id = self.env['ir.attachment'].create(invoice)
        surat_jalan_id = self.env['ir.attachment'].create(surat_jalan)

        template_id.attachment_ids = [
            (4, faktur_id.id), (4, purchase_id.id),
            (4, invoice_id.id), (4, surat_jalan_id.id)
            ]

        template_id.send_mail(self.id, raise_exception=False,  force_send=True)
        # template_id.attachment_ids = [
        #     (3, faktur_id.id), (3, purchase_id.id),
        #     (3, invoice_id.id), (3, surat_jalan_id.id)
        #     ]

        return True