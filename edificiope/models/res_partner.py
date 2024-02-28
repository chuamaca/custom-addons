from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def set_default_is_member(self):
        return False
    
    is_member = fields.Boolean(string="Is Member?", default=set_default_is_member)