from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_terms_cond = fields.Text(string='Sale Terms & Condition')
    invoice_terms_cond = fields.Text(string='Invoice Terms & Condition')