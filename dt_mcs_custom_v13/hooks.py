from . import __version__ as app_version

app_name = "dt_mcs_custom_v13"
app_title = "DT-MCS-Custom-v13"
app_publisher = "Dipane Technologies Pvt Ltd"
app_description = "DT-MCS-Custom-v13"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev1@dipanetech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dt_mcs_custom_v13/css/dt_mcs_custom_v13.css"
# app_include_js = "/assets/dt_mcs_custom_v13/js/dt_mcs_custom_v13.js"

# include js, css files in header of web template
# web_include_css = "/assets/dt_mcs_custom_v13/css/dt_mcs_custom_v13.css"
# web_include_js = "/assets/dt_mcs_custom_v13/js/dt_mcs_custom_v13.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dt_mcs_custom_v13/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dt_mcs_custom_v13.install.before_install"
# after_install = "dt_mcs_custom_v13.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dt_mcs_custom_v13.uninstall.before_uninstall"
# after_uninstall = "dt_mcs_custom_v13.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dt_mcs_custom_v13.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"dt_mcs_custom_v13.tasks.all"
#	],
#	"daily": [
#		"dt_mcs_custom_v13.tasks.daily"
#	],
#	"hourly": [
#		"dt_mcs_custom_v13.tasks.hourly"
#	],
#	"weekly": [
#		"dt_mcs_custom_v13.tasks.weekly"
#	]
#	"monthly": [
#		"dt_mcs_custom_v13.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "dt_mcs_custom_v13.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "dt_mcs_custom_v13.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "dt_mcs_custom_v13.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"dt_mcs_custom_v13.auth.validate"
# ]

