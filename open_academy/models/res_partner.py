from odoo import models,fields

class ResPartner(models.Model):
    _inherit='res.partner'
    
    
    def setDefaultIsInstructor(selft):
        return False
    #Alternativas de definir un default
    #is_instructor= fields.Boolean(string="Is Instructor?" default=false)
    #is_instructor= fields.Boolean(string="Is Instructor?" ,default=setDefaultIsInstructor)
    is_instructor= fields.Boolean(string="Is Instructor?", default=lambda selft:False)