TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_customers",
            "description": (
                "Search CRM customers by customer name or company. "
                "Use this first when the user identifies a customer by name."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Customer name or company name",
                    }
                },
                "required": ["name"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_customer_deals",
            "description": (
                "Retrieve deals for a uniquely identified customer. "
                "Only call after search_customers returns exactly one match. "
                "Optionally filter by close month in YYYY-MM format."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string"},
                    "close_month": {
                        "type": ["string", "null"],
                        "description": "Optional close month, e.g. 2026-11",
                    },
                },
                "required": ["customer_id", "close_month"],
                "additionalProperties": False,
            },
        },
    },
]
