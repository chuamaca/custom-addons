from odoo import models, fields

class Fose(models.Model):
    _name='fose'
    _descripcion='Fose'
    
    numerofose = fields.Char(string='Nro Fose', required=True)
    fechasolicitud = fields.Datetime(string='Fecha Solicitud')
    responsable_id = fields.Many2one(comodel_name='res.users', string='Responsible', required=True)
    cliente_id = fields.Many2one(comodel_name='res.company', string='Compania', required=True)

    