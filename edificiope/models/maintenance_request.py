from odoo import fields, models

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'
    
    amount = fields.Float(digits=(2, 2) ,string="Costo Reparacion")
