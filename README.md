odoo-printout-extras
====================

# Data Modules

The following modules provide data fields that are useful in rendering customised
reports.  They do not alter the base reports themselves.

## `purchase_order_split_sku_fields`

Adds two new computed fields to `purchase.order.line`:

* `product_sku` - the default code from the chosen product
* `description_without_sku` - the `name` field with the string `[product_sku]` stripped off

## `purchase_order_supplier_product_code_field`

Adds a `supplier_product_code` field to `purchase.order.line`, computed based upon
entries in the `product_id.seller_ids` field.

This will start with a very naive algorithm, and as requirements or R&D find better ways
this will be refined.

# Copyright and License

Copyright (C) 2016 OpusVL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

If you require assistance, support, or further development of this
software, please contact OpusVL using the details below:

* Telephone: +44 (0)1788 298 410
* Email: community@opusvl.com
* Web: http://opusvl.com
