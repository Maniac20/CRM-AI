from schemas import CustomerDeals
data = {
    "customer_name": "Rahul Sharma",
    "total_deals": 2,
    "total_value": 1300000,
    "deals": [
        {
            "name": "Website Redesign",
            "amount": "five lakhs",
            "stage": "Negotiation"
        }
    ]
}

try:
    
    result = CustomerDeals(**data)
    print(result.model_dump())
    
except Exception as e:
    print(type(e).__name__)
    print(e)

