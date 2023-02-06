from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name')
    p_o_ref = fields.Char(string='Purchase Order Ref')

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['p_o_ref'] = self.p_o_ref
        return invoice_vals


