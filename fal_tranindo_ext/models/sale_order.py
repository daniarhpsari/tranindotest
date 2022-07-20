from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.depends('picking_ids')
    def _fal_get_stock_picking(self):
        for sale_order in self:
            sale_order.fal_stock_picking_id = sale_order.picking_ids[0].id if sale_order.picking_ids else False

    fal_stock_picking_id = fields.Many2one("stock.picking", compute='_fal_get_stock_picking', string="Delivery")

    # _sql_constraints = [
    #     ('client_order_ref_contact_uniq', 'unique(client_order_ref)',
    #      "Duplicated Customer Reference detected. You probably encoded twice the same Quotation."),
    # ]

    @api.model
    def create(self, vals):
        if vals.get('client_order_ref') and vals.get('company_id'):
            self._check_duplicate_customer_reference(vals['client_order_ref'], vals['company_id'])
        res = super(SaleOrder, self).create(vals)
        return res

    def write(self, values):
        if values.get('client_order_ref'):
            self._check_duplicate_customer_reference(values.get('client_order_ref'), self.company_id.id)
        res = super(SaleOrder, self).write(values)
        return res
        
    def _check_duplicate_customer_reference(self, cust_ref, company):
        if self.search([('client_order_ref', '=', cust_ref), ('company_id', '=', company)]):
            raise UserError(_("Duplicated Customer Reference detected. You probably encoded twice the same Quotation."))
