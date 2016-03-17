# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    description_without_sku = fields.Char(
        compute="_description_without_sku_compute",
        readonly=True,
        string='Description without our product code',
    )

    product_sku = fields.Char(
        related=['product_id', 'default_code'],
        readonly=True,
        string='Our Product Code',
    )

    @api.depends('name', 'product_sku')
    @api.one
    def _description_without_sku_compute(self):
        if self.product_sku and self.name:
            sku_prefix = '[%s] ' % (self.product_sku,)
            self.description_without_sku = self.name.replace(sku_prefix, '')
        else:
            self.description_without_sku = self.name

