from odoo import models, fields

class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor') #string es la etiqueta del campo 
    name = fields.Char(string='Session', required=True)
    date_start = fields.Datetime(string='Date start', required=True)
    #date_start = fields.Datetime('Date start', required=True)
    #date_start = fields.Datetime(required=True) # valor por defecto, en caso de no usar el string del campo: Date Start
    duration = fields.Float(string='Duration')
    course_id = fields.Many2one(comodel_name='course', string='Course')
    active = fields.Boolean('Active', default=True)

    #Definir un campo de relacion muchos a muchos: Many2many

    attendee_ids = fields.Many2many('res.partner', 'session_res_partner_rel', 'session_id', 'res_partner_id', string='Session attendees')

    #instructor_ids = fields.Many2many('res.partner', 'session_instructor_rel', 'session_id', 'instructor_id', string='Session instructors')


