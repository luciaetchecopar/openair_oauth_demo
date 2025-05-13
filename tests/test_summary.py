from openair_api.summary import summarize_billable_hours

def test_summarize_billable_hours():
    entries = [
        {"userId": 1, "decimalHours": 2.5},
        {"userId": 2, "decimalHours": 1.0},
        {"userId": 1, "decimalHours": 1.5},
    ]
    result = summarize_billable_hours(entries)
    assert result == {1: 4.0, 2: 1.0}
