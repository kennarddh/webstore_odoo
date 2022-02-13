import json

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_round
from odoo.tools.safe_eval import safe_eval


class DeliveryCarrier(models.Model):
    _name = "delivery.carrier"
    _inherit = ["delivery.carrier"]

    delivery_type = fields.Selection(
        selection_add=[("raja_ongkir", "raja_ongkir")],
        ondelete={'raja_ongkir': lambda recs: recs.write({
            'delivery_type': 'fixed', 'fixed_price': 0,
        })})


