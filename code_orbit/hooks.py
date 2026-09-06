app_name = "code_orbit"
app_title = "CodeOrbit"
app_publisher = "Dhanaa Lakshmi"
app_description = "AI-Powered Software Engineering Operations Platform"
app_email = "dhanaalakshminarayanan@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "code_orbit",
# 		"logo": "/assets/code_orbit/logo.png",
# 		"title": "CodeOrbit",
# 		"route": "/code_orbit",
# 		"has_permission": "code_orbit.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/code_orbit/css/code_orbit.css"
# app_include_js = "/assets/code_orbit/js/code_orbit.js"

# include js, css files in header of web template
# web_include_css = "/assets/code_orbit/css/code_orbit.css"
# web_include_js = "/assets/code_orbit/js/code_orbit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "code_orbit/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "code_orbit/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "code_orbit.utils.jinja_methods",
# 	"filters": "code_orbit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "code_orbit.install.before_install"
# after_install = "code_orbit.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "code_orbit.uninstall.before_uninstall"
# after_uninstall = "code_orbit.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "code_orbit.utils.before_app_install"
# after_app_install = "code_orbit.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "code_orbit.utils.before_app_uninstall"
# after_app_uninstall = "code_orbit.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "code_orbit.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "code_orbit.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"code_orbit.tasks.all"
# 	],
# 	"daily": [
# 		"code_orbit.tasks.daily"
# 	],
# 	"hourly": [
# 		"code_orbit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"code_orbit.tasks.weekly"
# 	],
# 	"monthly": [
# 		"code_orbit.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "code_orbit.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "code_orbit.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "code_orbit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "code_orbit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["code_orbit.utils.before_request"]
# after_request = ["code_orbit.utils.after_request"]

# Job Events
# ----------
# before_job = ["code_orbit.utils.before_job"]
# after_job = ["code_orbit.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"code_orbit.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

