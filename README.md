# Manufacturing Management — Frappe Framework

A custom manufacturing management application built with **Frappe Framework v15**, Python, JavaScript, and MariaDB.

This project is part of a hands-on Frappe/ERPNext development journey, focusing on manufacturing workflows, backend validations, document relationships, and business logic.

## Tech Stack

- Frappe Framework v15
- Python 3.11
- JavaScript
- MariaDB
- Redis
- Bench CLI
- Ubuntu 24.04 (WSL2) for local development

## Implemented Features

### Production Machine Management
- Create, view, update, and delete production machine records
- Manage machine code, name, quantity, unit cost, status, and remarks
- Backend validation for quantity and unit cost
- Duplicate machine code validation

### Raw Material Management
- Maintain a raw material master
- Store material code, name, unit, and default price
- Reference materials using Frappe Link fields

### Production Machine Materials
- Assign multiple raw materials to a production machine
- Manage material quantities and unit prices
- Automatically calculate line totals on document validation
- Calculate total material cost
- Reject invalid quantities, negative prices, and duplicate materials

## Data Model

```text
Production Machine
    |
    |-- Production Machine Material (Child Table)
            |
            |-- Raw Material (Link)
```

## Installation

### Requirements
- Frappe Framework v15
- Bench CLI
- MariaDB and Redis

### Install the App

From an existing Frappe Bench:

```bash
bench get-app https://github.com/YOUR_USERNAME/manufacturing_management.git
bench --site YOUR_SITE install-app manufacturing_management
bench --site YOUR_SITE migrate
```

### Start Development Server

```bash
bench start
```

## Project Structure

```text
manufacturing_management/
├── manufacturing_management/
│   ├── config/
│   ├── manufacturing_management/
│   │   └── doctype/
│   │       ├── production_machine/
│   │       ├── production_machine_material/
│   │       └── raw_material/
│   ├── hooks.py
│   └── modules.txt
├── pyproject.toml
└── README.md
```

## Roadmap

- [x] Custom Frappe application setup
- [x] Production Machine DocType
- [x] Raw Material DocType
- [x] Child Table and Link relationships
- [x] Backend validation
- [x] Material cost calculation
- [ ] Real-time Client Script calculations
- [ ] Automatic material price fetching
- [ ] Workflow and role-based permissions
- [ ] Material requisition
- [ ] Production order management
- [ ] Reports and dashboards
- [ ] Automated tests

## Development Status

**Active Learning & Development**

The current version demonstrates foundational Frappe concepts. It is not yet production-ready.

## License

MIT, if applicable to the license selected during app creation.
