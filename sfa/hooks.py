# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sfa"
app_title = "Sales Force"
app_publisher = "bobzz.zone@gmail.com"
app_description = "Sales Force Application"
app_icon = "octicon-package"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sfa/css/sfa.css"
# app_include_js = "/assets/sfa/js/sfa.js"

# include js, css files in header of web template
# web_include_css = "/assets/sfa/css/sfa.css"
# web_include_js = "/assets/sfa/js/sfa.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sfa.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sfa.install.before_install"
# after_install = "sfa.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sfa.notifications.get_notification_config"

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

doc_events = {
	"Address": {
		"on_update": "sfa.custom_function.set_default_address",
#		"on_cancel": "method",
#		"on_trash": "method"
	},
	"Contact": {
		"on_update": "sfa.custom_function.set_default_contact",
#		"on_cancel": "method",
#		"on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sfa.tasks.all"
# 	],
# 	"daily": [
# 		"sfa.tasks.daily"
# 	],
# 	"hourly": [
# 		"sfa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sfa.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sfa.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sfa.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sfa.event.get_events"
# }

