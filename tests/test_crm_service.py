import pytest
from app.services.crm_service import CRMService


@pytest.fixture
def crm():
    return CRMService()


def test_search_unique_customer(crm):
    result = crm.search_customers("Priya Verma")
    assert result.status == "found"
    assert len(result.matches) == 1
    assert result.matches[0].id == "C102"


def test_search_ambiguous_customer(crm):
    result = crm.search_customers("Rahul Sharma")
    assert result.status == "ambiguous"
    assert len(result.matches) == 2


def test_search_missing_customer(crm):
    result = crm.search_customers("Nonexistent Person")
    assert result.status == "not_found"
    assert result.matches == []


def test_get_customer_deals_and_total(crm):
    result = crm.get_customer_deals("C101")
    assert result.total_deals == 2
    assert result.total_value == 1_300_000


def test_filter_deals_by_month(crm):
    result = crm.get_customer_deals("C101", close_month="2026-11")
    assert result.total_deals == 1
    assert result.deals[0].id == "D201"


def test_invalid_month_format(crm):
    with pytest.raises(ValueError, match="YYYY-MM"):
        crm.get_customer_deals("C101", close_month="November")


def test_unknown_customer_id(crm):
    with pytest.raises(ValueError, match="Customer not found"):
        crm.get_customer_deals("C999")
