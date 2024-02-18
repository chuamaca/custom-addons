# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MyModel(models.Model):
    _name = "my.model"
    _description = 'My first model'

    name = fields.Char(string="Name", required=True)
    date_expected = fields.Datetime(string="Date Expected")
    people_id = fields.Many2one(comodel_name="res.partner", string="Responsible People")
    line_ids = fields.One2many(comodel_name="my.model.lines", inverse_name="mymodel_id", string="My Model lines")
    type = fields.Selection(string="Order type", 
                            selection=[('normal', 'Normal'),
                                        ('fast', 'Fast')],
                            default='normal')
    tag_ids = fields.Many2many("my.model.tags", "mymodel_tags_rel", "mymodel_id", "tag_id", string="Tags")
    lines_qty = fields.Integer(string="Lines qty", compute="_calc_lines_qty")

    @api.depends('line_ids')
    def _calc_lines_qty(self):
        for rec in self:
            rec.lines_qty = 0
            if len(rec.line_ids):
                rec.lines_qty = len(rec.line_ids)


class Lines(models.Model):
    _name = "my.model.lines"
    _description = 'My model lines'

    mymodel_id = fields.Many2one(string="My model", comodel_name="my.model")
    product_id = fields.Many2one(string="Product", comodel_name="product.product", required=True)
    qty = fields.Integer(string="Quantity", required=True)


class MyModelTags(models.Model):
    _name = "my.model.tags"
    _description = 'My model tags'

    name = fields.Char(string="Tag name", required=True)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    mi_nuevo_campo=fields.Char(string="Esto es un nuevo campo")