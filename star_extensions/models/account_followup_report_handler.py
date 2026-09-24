# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.tools import SQL


class AccountFollowupReportHandler(models.AbstractModel):
    """ On-screen (Accounting) Follow-up report: add a 'Po Reference' column,
    fetched from the related sale order via the move's invoice origin. """
    _inherit = 'account.followup.report.handler'

    def _get_additional_column_aml_values(self):
        # Injected into the SELECT of both UNION branches of the partner-ledger
        # aml query, so it must end with a trailing comma. `account_move_line`
        # is the base table in both branches, so `move_id` is always available.
        return SQL(
            "%s%s",
            super()._get_additional_column_aml_values(),
            SQL(
                """(
                    SELECT so.p_o_ref
                      FROM sale_order so
                      JOIN account_move am ON am.id = account_move_line.move_id
                     WHERE so.name = am.invoice_origin
                     LIMIT 1
                ) AS p_o_ref, """
            ),
        )
