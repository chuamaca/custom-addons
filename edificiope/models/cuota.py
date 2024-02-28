from odoo import fields, models

class cuota(models.Model):
    _name = 'cuota'
    _description = 'cuota'

    partnerbuilding_id = fields.Many2one(comodel_name='res.partner', string='') #string es la etiqueta del campo 
    name = fields.Char(string='Numero Cuota', required=True)
    date_start = fields.Datetime(string='Date start', required=True)
    date_end = fields.Datetime(string='Date End', required=True)
    #amount = fields.Monetary(string='Amount')
    amount = fields.Float(digits=(2, 2))

    scheduledfee_id=fields.Many2one(comodel_name='scheduledfee',string='Cuota Programada')


    def set_default_is_cero(self):
        return 0