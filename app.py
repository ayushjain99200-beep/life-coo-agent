import datetime

def generate_digest():
    # Demo data (later we can connect your bank exports, UPI, etc.)
    transactions = [
        {"date": "2025-08-01", "category": "Rent", "amount": 12000},
        {"date": "2025-08-05", "category": "Groceries", "amount": 5200},
        {"date": "2025-08-10", "category": "Healthcare", "amount": 1800},
    ]

    total = sum(t["amount"] for t in transactions)
    today = datetime.date.today()

    digest = f"Finance Digest — {today.strftime('%B %Y')}\n"
    digest += f"Total spend: ₹{total}\n\nTop categories:\n"
    for t in transactions:
        digest += f" • {t['category']}: ₹{t['amount']}\n"

    digest += "\nSuggested actions:\n"
    digest += " • Shift +₹2,000 from food/groceries to SIP next month.\n"
    digest += " • Review subscriptions this weekend.\n"

    return digest

if __name__ == "__main__":
    print(generate_digest())
