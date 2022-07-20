from odoo import _, exceptions, fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta, MO, SU
from odoo.exceptions import UserError, ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.move"


    fal_stock_picking_id = fields.Many2one("stock.picking", string="Delivery", compute='_fal_get_stock_picking')
    date_invoice = fields.Date(string='Date Invoices')
    
    @api.depends('invoice_line_ids')
    def _fal_get_stock_picking(self):
        for invoice in self:
            sale_order_ids = invoice.invoice_line_ids.mapped('sale_line_ids').mapped('order_id')
            if sale_order_ids:
                invoice.fal_stock_picking_id = sale_order_ids[0].fal_stock_picking_id.id if sale_order_ids[0].fal_stock_picking_id else False
            else:
                invoice.fal_stock_picking_id = ''

    fal_paid_date = fields.Date(string='Paid Date')
    fal_payment_method = fields.Many2one('account.journal', string='Payment Method')
    

