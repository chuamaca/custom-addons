from odoo import fields, models

class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(string='Course', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one(comodel_name='res.users', string='Responsible', required=True)