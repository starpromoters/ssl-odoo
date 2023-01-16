from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name')