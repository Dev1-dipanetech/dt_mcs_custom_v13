// Copyright (c) 2023, Dipane Technologies Pvt Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Reco Report"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Company",
			"default": frappe.defaults.get_default("company")
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "item_group",
			"label": __("Item Group"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item Group"
		},
		{
			"fieldname": "item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item",
			"get_query": function() {
				return {
					query: "erpnext.controllers.queries.item_query",
				};
			}
		},
		{
			"fieldname": "warehouse",
			"label": __("Warehouse"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Warehouse",
			get_query: () => {
				let warehouse_type = frappe.query_report.get_filter_value("warehouse_type");
				let company = frappe.query_report.get_filter_value("company");

				return {
					filters: {
						...warehouse_type && {warehouse_type},
						...company && {company}
					}
				}
			}
		},
		{
			"fieldname": "warehouse_type",
			"label": __("Warehouse Type"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Warehouse Type"
		},
		{
			"fieldname":"include_uom",
			"label": __("Include UOM"),
			"fieldtype": "Link",
			"options": "UOM"
		},
		{
			"fieldname":"project",
			"label": __("Project"),
			"fieldtype": "Link",
			"options": "Project"
		},
		{
			"fieldname":"batch_no",
			"label": __("Batch No"),
			"fieldtype": "Link",
			"options": "Batch"
		},
		{
			"fieldname": "show_variant_attributes",
			"label": __("Show Variant Attributes"),
			"fieldtype": "Check"
		},
		{
			"fieldname": 'show_stock_ageing_data',
			"label": __('Show Stock Ageing Data'),
			"fieldtype": 'Check'
		},

	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);

		if (column.fieldname == "voucher_type" && data && data.voucher_type == "Reconciled") {
			// value = "<span style='color:green'>" + value + "</span>";
			let f_date = frappe.query_report.get_filter_value("to_date");
			
			const today = new Date(f_date);
			const sixMonthsAgo = new Date(today.getFullYear(), today.getMonth() - 6, today.getDate());
		

			var sixMonthsAgoFormatted = sixMonthsAgo.getFullYear() + '-' + 
  			(sixMonthsAgo.getMonth() + 1).toString().padStart(2, '0') + '-' + 
  			sixMonthsAgo.getDate().toString().padStart(2, '0');
			
			value = data["posting_date"]
			// value = sixMonthsAgoFormatted

			if (sixMonthsAgoFormatted > value ) {
				// value = "Old Reconciled";
				value = "<span style='color:yellow'>" + "Old Reconciled" + "</span>";
				// console.log("Today's date is after six months ago");
			} 
			else {
				// value = "Reconciled"
				value = "<span style='color:green'>" + "Reconciled" + "</span>";
			}
			
		}
		else if (column.fieldname == "voucher_type" && data && data.voucher_type == "Unreconciled") {
			value = "<span style='color:red'>" + value + "</span>";
		}

		if (column.fieldname == "out_qty" && data && data.out_qty > 0) {
			value = "<span style='color:red'>" + value + "</span>";
		}
		else if (column.fieldname == "in_qty" && data && data.in_qty > 0) {
			value = "<span style='color:green'>" + value + "</span>";
		}

		return value;
	}
};
