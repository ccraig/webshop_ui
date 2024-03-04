import frappe
from frappe.website.utils import (
	get_sidebar_items,
)

def website_context(context):
	a = 1
	web_forms_show_portal_menu = ['/address', '/update-profile']
	if context.show_sidebar and hasattr(frappe.local, "request") and frappe.local.request.environ:
		for web_form_url in web_forms_show_portal_menu:
			if web_form_url in frappe.local.request.environ['REQUEST_URI']:
					context.sidebar_items = get_sidebar_items("")
	#context.show_sidebar = True
	#print(context)
