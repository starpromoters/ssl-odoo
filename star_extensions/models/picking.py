from odoo import SUPERUSER_ID, _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class Picking(models.Model):
    _inherit = 'stock.picking'


    def _compute_is_hide_return(self):
        for record in self:
            record.is_hide_return = False
            if record.picking_type_id.code == 'outgoing' and self.env.user.has_group('star_extensions.group_main_domestic_user'):
                record.is_hide_return = True


    p_o_ref = fields.Char(string='Purchase Order Ref')
    is_hide_return = fields.Boolean(string="Is Hide Return",compute='_compute_is_hide_return')

    def _create_backorder_picking(self):
        """ Carry the Purchase Order Ref over to the backorder picking. """
        backorder_picking = super()._create_backorder_picking()
        backorder_picking.p_o_ref = self.p_o_ref
        return backorder_picking

class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()
        res.update({
            'p_o_ref': self.sale_line_id.order_id.p_o_ref if self.sale_line_id.order_id else False
            })
        return res

    
