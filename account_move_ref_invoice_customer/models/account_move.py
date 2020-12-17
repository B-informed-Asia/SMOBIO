# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountMove(models.Model):
	_inherit = "account.move"

	def _get_invoice_reference_odoo_customer_invoice(self):
	    """ This computes the reference based on the Odoo format.
	        We simply return the number of the invoice, defined on the journal
	        sequence.
	    """
	    cust = self.partner_id.ref or str(self.partner_id.id)
	    invoice = self.name
	    return '%s / %s' % (cust, invoice)