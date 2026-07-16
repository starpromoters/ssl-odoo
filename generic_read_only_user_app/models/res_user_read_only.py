# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools,_
from odoo.exceptions import ValidationError

class ResUser(models.Model):
    _inherit = 'res.users'

    read_only = fields.Boolean(string="Make Read Only")

    @api.onchange('read_only')
    def set_read_only_user(self):
        read_only_group = self.env.ref(
            'generic_read_only_user_app.group_read_only_user',
            raise_if_not_found=False
        )
        if not read_only_group:
            return

        for user in self:
            # Always create a plain Python list of IDs
            group_ids = list(user.group_ids.ids)
            if user.read_only:
                if read_only_group.id not in group_ids:
                    group_ids.append(read_only_group.id)
            else:
                group_ids = [
                    gid for gid in group_ids
                    if gid != read_only_group.id
                ]
            user.group_ids = [(6, 0, group_ids)]


class IrModelAccess(models.Model):
    _inherit = 'ir.model.access'

    @api.model
    @tools.ormcache('self._uid','model','mode','raise_exception','self.env.context.get("lang")',)
    # @tools.ormcache_context('self._uid', 'model', 'mode', 'raise_exception', keys=('lang',))
    def check(self, model, mode='read', raise_exception=True):
        result = super(IrModelAccess, self).check(model, mode, raise_exception=raise_exception)
        if self.env.user.has_group('generic_read_only_user_app.group_read_only_user'):
            if mode != 'read':
                return False
        return result

class IrRule(models.Model):
    _inherit = 'ir.rule'

    def _compute_domain(self, model_name, mode="read"):
        res = super(IrRule,self)._compute_domain(model_name, mode)
        obj_list=['res.users.log','res.users','mail.channel','mail.alias','bus.presence','res.lang']
        if model_name not in obj_list:
            if self.env.user.has_group('generic_read_only_user_app.group_read_only_user'):
                if mode != 'read':
                    raise ValidationError(_('Read only user can not done this operation..! (%s)') % self.env.user.name)
        return res