# Copyright 2026 AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    gross_weight = fields.Float(string="Gross Field", copy=False)

    # HT02687: portado del v14 (stock_move_qty_by_packaging): el peso bruto se
    # pone a mano y 'Hecho' (la cantidad) se calcula restando el peso de los
    # empaquetados (cajas) y el de los palets.
    @api.onchange("gross_weight")
    def _onchange_gross_weight(self):
        weight_categ = self.env.ref("uom.product_uom_categ_kgm")
        quantity = self.gross_weight
        if self.gross_weight and self.product_uom_id.category_id == weight_categ:
            if (
                self.product_packaging_id
                and self.product_packaging_id.weight
                and self.product_packaging_qty
            ):
                quantity -= (
                    self.product_packaging_id.weight * self.product_packaging_qty
                )
            if self.palet_id and self.palet_id.weight and self.palet_qty:
                quantity -= self.palet_id.weight * self.palet_qty
        self.quantity = quantity
