from odoo import fields, models

class ScheduledFee(models.Model):    
    _name = 'scheduledfee'
    _description = 'scheduledfee'

    month = fields.Char(string='Mont', required=True)
    year = fields.Char(string='Year', required=True)
    date_start = fields.Datetime(string='Date start', required=True)