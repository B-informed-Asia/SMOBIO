# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class AccountJournal(models.Model):
    _inherit = "account.journal"

    invoice_reference_type = fields.Selection(selection_add=[('customer_invoice', 'Customer Reference with Invoice number')]) 