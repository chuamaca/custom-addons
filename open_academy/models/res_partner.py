from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def set_default_is_instructor(self):
        return False
    
    is_instructor = fields.Boolean(string="Is Instructor?", default=set_default_is_instructor)