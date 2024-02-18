from odoo import models

class PurchaseOrder(models.Model):
    _inherit='purchase.order'
    
    def button_confirm(selft):
        #Invocar al Metodo Super
        res=super(PurchaseOrder,selft).button_confirm()
        print("Hello Word")
        return res
    