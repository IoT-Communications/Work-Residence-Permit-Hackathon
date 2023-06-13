# Copyright (c) 2023, IoT Communications (Pty) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from payments.utils.utils import get_payment_gateway_controller
from frappe.utils import flt, get_url, nowdate

class WorkPermitApplication(Document):

	def on_update(self):
		if self.workflow_state == "Ready for Payment":
			controller = get_payment_gateway_controller(self.payment_gateway)

			controller.validate_transaction_currency(self.currency)

			redirect_to = controller.get_payment_url(**{
				"amount": flt(self.application_fee),
				"title": "Credit and Debit Card Payment Gateway".encode("utf-8"),
				"description": ("Payment Request for Application " + self.name).encode("utf-8"),
				"reference_doctype": self.doctype,
				"reference_docname": self.name,
				"payer_email": "k.pule@iotcomms.co.bw".encode("utf-8"),
				"payer_name": self.full_name,
				"order_id": self.name,
				"currency": self.currency
			})

			self.payment_url = redirect_to

			self.db_set('payment_url', self.payment_url)

		

	def on_payment_authorized(self, status=None):
		
		if not status:
			return

		if status in ["Authorized", "Completed"]:
			frappe.flags.ignore_account_permission = True

			redirect_to = None

			doc = frappe.get_doc(self.doctype, self.name)

			if doc.workflow_state == "Pending Payment":
				doc.workflow_state = "Paid"
				doc.save(ignore_permissions=True)

				# redirect to application
				redirect_to = get_url("/app/residence-permit-application/" + self.name)

				# redirect_to = "https://work-residence.iotcomms.co.bw/app/work-permit-application/" + self.name

				# return redirect_to