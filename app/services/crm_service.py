from app.crm.mock_data import CUSTOMERS, DEALS
from app.schemas.crm import Customer, Deal, CustomerLookupResult, DealLookupResult


class CRMService:
    """Mock CRM adapter. Replace this implementation with a real CRM adapter later."""

    def search_customers(self, name: str) -> CustomerLookupResult:
        query = name.strip().casefold()
        matches = [
            Customer(**customer)
            for customer in CUSTOMERS
            if query in customer["name"].casefold()
            or query in customer["company"].casefold()
        ]
        if not matches:
            return CustomerLookupResult(
                status="not_found",
                message="No matching customer found.",
            )
        if len(matches) > 1:
            return CustomerLookupResult(
                status="ambiguous",
                message="Multiple customers match. Ask the user to identify the correct company.",
                matches=matches,
            )
        return CustomerLookupResult(
            status="found",
            message="Customer found.",
            matches=matches,
        )

    def get_customer_deals(
        self,
        customer_id: str,
        close_month: str | None = None,
    ) -> DealLookupResult:
        customer_data = next(
            (customer for customer in CUSTOMERS if customer["id"] == customer_id),
            None,
        )
        if customer_data is None:
            raise ValueError("Customer not found.")

        deals_data = [
            deal for deal in DEALS if deal["customer_id"] == customer_id
        ]
        if close_month:
            if (
                len(close_month) != 7
                or close_month[4] != "-"
                or not close_month[:4].isdigit()
                or not close_month[5:].isdigit()
                or not 1 <= int(close_month[5:]) <= 12
            ):
                raise ValueError("close_month must use YYYY-MM format.")
            deals_data = [
                deal for deal in deals_data
                if deal["close_date"].startswith(close_month)
            ]

        deals = [Deal(**deal) for deal in deals_data]
        # Compute money totals in deterministic backend code, not with the LLM.
        total_value = sum(deal.amount for deal in deals)
        return DealLookupResult(
            customer=Customer(**customer_data),
            deals=deals,
            total_deals=len(deals),
            total_value=total_value,
        )
