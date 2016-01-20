from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_currency_domination(currency):
	return frappe.db.sql("""select label,image,value from `tabCurrency Denomination` where parent=%s""",currency, as_dict=1)
	