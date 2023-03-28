from odoo import api, fields, models, SUPERUSER_ID, _

import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import AccessError, UserError, ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name')
    p_o_ref = fields.Char(string='Purchase Order Ref')
    
    def action_confirm(self):
        if not self.p_o_ref:
            raise UserError(_('Kindly provide the Po Reference.'))
        res = super(SaleOrder,self).action_confirm()
        return res


    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['p_o_ref'] = self.p_o_ref
        return invoice_vals


