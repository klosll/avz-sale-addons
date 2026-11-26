# Copyright 2023 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Order Line Gross Weight",
    "version": "18.0.1.1.0",
    "category": "Hidden",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/sale-addons",
    "depends": [
        "stock_move_qty_by_packaging",
        # HT02687: para insertar 'Peso bruto' después de 'Cantidad palet'
        "product_packaging_palet",
    ],
    "data": [
        "views/sale_order_view.xml",
        "views/stock_move_line_view.xml",
    ],
    "installable": True,
}
