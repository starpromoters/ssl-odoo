from odoo import api, fields, models, SUPERUSER_ID, _

import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import AccessError, UserError, ValidationError




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name')
    p_o_ref = fields.Char(string='Purchase Order Ref')

    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id=view_id, view_type=view_type, **options)
        if view_type == 'form' and self.env.company.id == 7:
            for node in arch.xpath("//field[@name='p_o_ref']"):
                node.set('string', 'AR')
        return arch, view
    
    def action_confirm(self):
        if not self.p_o_ref:
            raise UserError(_('Kindly provide the Po Reference.'))
        res = super(SaleOrder,self).action_confirm()
        return res


    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['p_o_ref'] = self.p_o_ref
        return invoice_vals




