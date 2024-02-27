from odoo import models, fields, api
import logging

from odoo.exceptions import AccessError, UserError, ValidationError

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hs_code = fields.Char(string='HS Code',copy=False)
    company_id = fields.Many2one('res.company', 'Company', index=1, default=lambda self: self.env.company)
   
