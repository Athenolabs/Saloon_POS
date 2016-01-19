# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "saloon"
app_title = "Saloon"
app_publisher = "Saloon"
app_description = "Saloon"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "pitambar.h@indictranstech.com"
app_version = "0.0.1"
app_license = "gpl"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/saloon/css/saloon.css"
# app_include_js = "/assets/saloon/js/saloon.js"
app_include_js = "assets/js/saloon.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/saloon/css/saloon.css"
# web_include_js = "/assets/saloon/js/saloon.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "saloon.install.before_install"
# after_install = "saloon.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "saloon.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"saloon.tasks.all"
# 	],
# 	"daily": [
# 		"saloon.tasks.daily"
# 	],
# 	"hourly": [
# 		"saloon.tasks.hourly"
# 	],
# 	"weekly": [
# 		"saloon.tasks.weekly"
# 	]
# 	"monthly": [
# 		"saloon.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "saloon.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "saloon.event.get_events"
# }

fixtures = ["Custom Field"]