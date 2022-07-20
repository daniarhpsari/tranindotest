from odoo import fields, models, api
from odoo import _
from odoo.exceptions import UserError, ValidationError
import odoo.addons.decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)


class product_product(models.Model):
    _inherit = 'product.template'

    @api.constrains('name')
    def _check_name(self):
        if self.name:
            product_rec = self.env['product.template'].search(
                [('name', '=', self.name)])
            if len(product_rec) > 1:
                raise ValidationError(_('Theres already product with the same name!!!'))


