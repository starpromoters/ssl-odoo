# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.tools.translate import _


class AccountFollowupReport(models.AbstractModel):
    _inherit = 'account.followup.report'

    def get_po_ref(self, value):
        order = self.env['sale.order'].search([('name', '=', value)], limit=1)
        return order.p_o_ref or ''

    def _get_followup_report_columns_name(self):
        """ Add a 'Po Reference' column right before the 'Total Due' column. """
        columns = super()._get_followup_report_columns_name()
        columns.insert(len(columns) - 1, {
            'name': _('Po Reference'),
            'style': 'text-align:center; white-space:nowrap;',
        })
        return columns

    def _get_followup_report_lines(self, options):
        """ Inject a 'Po Reference' cell (fetched from the related sale order via
        the move's invoice origin) into every line, keeping cell/header alignment. """
        lines = super()._get_followup_report_lines(options)
        for line in lines:
            columns = line.get('columns')
            if not columns:
                continue
            po_ref = ''
            move_id = line.get('move_id')
            if move_id:
                move = self.env['account.move'].browse(move_id)
                if move.invoice_origin:
                    po_ref = self.get_po_ref(move.invoice_origin)
            po_cell = {
                'name': po_ref,
                'style': 'text-align:center; white-space:normal;',
                'template': 'account_followup.line_template',
            }
            # Insert before the last cell (the amount / Total Due column)
            columns.insert(len(columns) - 1, po_cell)
        return lines
