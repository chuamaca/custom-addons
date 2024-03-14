from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

class cuota(models.Model):
    _name = 'cuota'
    _description = 'cuota'

    partnerbuilding_id = fields.Many2one(comodel_name='res.partner', string='Usuario') #string es la etiqueta del campo
    department = fields.Char(string='Departamento', required=True)
    name = fields.Char(string='Recibo', default='New' ,readonly=True)
    paymentdate = fields.Datetime(string='Fecha de Pago', required=True)
    totalamount = fields.Float(digits=(2, 2), string='Total')
    pendingamount=fields.Float(digits=(2, 2), compute='_compute_campo_calculado_x_periodo', string='Pendiente') #compute='_compute_campo_calculado' ,
    amountpaid =fields.Float(digits=(2, 2),string='Pagado')
    scheduledfee_id=fields.Many2one(comodel_name='scheduledfee',string='Periodo')
    observation = fields.Char(string='Observacion')



    @api.onchange('scheduledfee_id','amountpaid')
    def _compute_campo_calculado_x_periodo(self):
        for record in self:
            scheduled_fee = record.scheduledfee_id
            if scheduled_fee:
                busqueda_cuota = self.env['scheduledfee'].search([('id','=',scheduled_fee.id)])
                if busqueda_cuota:
                    record.pendingamount=busqueda_cuota.amount - record.amountpaid
                    record.totalamount=busqueda_cuota.amount
                else:
                    record.pendingamount=0.0
                    record.totalamount=busqueda_cuota.amount
            else:
                record.pendingamount=0.0



    @api.onchange('amountpaid')
    def _compute_campo_calculado_segun_montopagado(self):
        for record in self:
            scheduled_fee = record.scheduledfee_id
            if scheduled_fee:
                busqueda_cuota = self.env['scheduledfee'].search([('id','=',scheduled_fee.id)])
                if busqueda_cuota:
                    record.pendingamount=busqueda_cuota.amount - record.amountpaid
                else:
                    record.pendingamount=0.0
           


    @api.depends('amountpaid')
    def _compute_campo_calculado(self):
        for record in self:
            scheduled_fee = record.scheduledfee_id
            if scheduled_fee:
                busqueda_cuota = self.env['scheduledfee'].search([('id','=',scheduled_fee.id)])
                if busqueda_cuota:
                    record.pendingamount=busqueda_cuota.amount - record.amountpaid
                else:
                    record.pendingamount=0.0
            else:
                record.pendingamount=0.0



    # @api.depends('amountpaid')
    # def _compute_campo_calculadoeee(self):
    #     for record in self:
    #        miid=record.scheduledfee_id
    #        busqueda_cuota = self.env['scheduledfee'].search([('id','=',miid)])
    #        print(str(busqueda_cuota))

                # Supongamos que quieres sumar el campo_a con el campo de un registro en ModeloB
                # modelo_b_record = self.env['scheduledfee'].search([('name', '=', record.scheduledfee_id)])
                # if modelo_b_record:
                #     record.pendingamount = modelo_b_record.amount - record.amountpaid
                # else:
                #     record.pendingamount = modelo_b_record.amount - record.amountpaid



    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('recibocuota') or 'New'
        result = super(cuota, self).create(vals)
        return result