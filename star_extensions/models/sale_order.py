from odoo import api, fields, models, SUPERUSER_ID, _

import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import AccessError, UserError, ValidationError
from lxml import etree




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name')
    p_o_ref = fields.Char(string='Purchase Order Ref')

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(SaleOrder, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='p_o_ref']"):
                if self.env.company.id == 7:
                    node.set('string', 'AR')
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res
    
    def action_confirm(self):
        if not self.p_o_ref:
            raise UserError(_('Kindly provide the Po Reference.'))
        res = super(SaleOrder,self).action_confirm()
        return res


    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['p_o_ref'] = self.p_o_ref
        return invoice_vals




