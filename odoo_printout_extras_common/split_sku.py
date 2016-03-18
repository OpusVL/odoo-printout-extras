
"""Split SKU common code.


Example:

    class StockMove(models.Model, SplitSKUFieldsMixin):
        _inherit = 'stock.move'

"""

from openerp import fields, api

class SplitSKUFieldsMixin(object):
    """This is the mixin suitable for most models this functionality is applicable to
    """
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

