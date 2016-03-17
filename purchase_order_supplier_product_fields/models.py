# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    supplier_product_code = fields.Char(
        compute="_supplier_product_code_compute",
        string='Supplier Product Code',
    )

    @api.depends('partner_id', 'product_id.seller_ids.product_code')
    @api.one
    def _supplier_product_code_compute(self):
        sellers = self.product_id.seller_ids.filtered(lambda seller: seller.name == self.partner_id)
        self.supplier_product_code = sellers and sellers[0].product_code
