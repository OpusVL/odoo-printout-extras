# -*- coding: utf-8 -*-

from openerp import models
from ..odoo_printout_extras_common.split_sku import SplitSKUFieldsMixin

class StockMove(models.Model, SplitSKUFieldsMixin):
    _inherit = 'stock.move'
