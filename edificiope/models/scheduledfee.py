from odoo import fields, models

class ScheduledFee(models.Model):    
    _name = 'scheduledfee'
    _description = 'scheduledfee'

    name =fields.Char(string='Cuota', required=True  )
    month = fields.Char(string='Mont', required=True)
    year = fields.Char(string='Year', required=True)
    date_start = fields.Datetime(string='Date start', required=True)
    date_end = fields.Datetime(string='Date End', required=True)

    def setDefaultName(selft):
        return month  + year