
import frappe
from frappe.model.document import Document
from frappe.utils import flt


class ProductionMachine(Document):
    def validate(self):
        self.validate_machine()
        self.calculate_material_cost()

    def validate_machine(self):
        if flt(self.quantity) <= 0:
            frappe.throw("Quantity must be greater than zero")

        if flt(self.unit_cost) < 0:
            frappe.throw("Unit cost cannot be negative")

        if frappe.db.exists(
            "Production Machine",
            {
                "machine_code": self.machine_code,
                "name": ["!=", self.name],
            },
        ):
            frappe.throw("Machine Code already exists")

    def calculate_material_cost(self):
        total = 0
        used_materials = set()

        for row in self.get("materials") or []:
            if not row.material:
                frappe.throw(f"Material is required in row {row.idx}")

            if row.material in used_materials:
                frappe.throw(f"Duplicate material in row {row.idx}")

            used_materials.add(row.material)

            if flt(row.quantity) <= 0:
                frappe.throw(f"Invalid quantity in row {row.idx}")

            if flt(row.unit_price) < 0:
                frappe.throw(f"Invalid unit price in row {row.idx}")

            row.line_total = flt(
                flt(row.quantity) * flt(row.unit_price),
                2,
            )

            total += row.line_total

        self.total_material_cost = flt(total, 2)
