"""Rule-based financial chatbot for Microsoft, Tesla, and Apple (FY2023-FY2025)."""
from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("financial_data.csv")

def load_data():
    return pd.read_csv(DATA_FILE)

def money(value):
    return f"${value:,.0f} million"

def answer_query(query, df=None):
    """Answer a supported financial question using predefined rule-based logic."""
    if df is None:
        df = load_data()
    q = query.lower().strip()
    companies = {"microsoft": "Microsoft", "tesla": "Tesla", "apple": "Apple"}
    company = next((name for key, name in companies.items() if key in q), None)
    years = [year for year in (2023, 2024, 2025) if str(year) in q]

    if not company:
        return "Please mention Microsoft, Tesla, or Apple in your question."
    company_df = df[df["Company"] == company].sort_values("Year")
    if company_df.empty:
        return "I couldn't find data for that company."

    if any(word in q for word in ("revenue", "sales")):
        metric = "Total Revenue"
        label = "revenue"
    elif "net income" in q or "profit" in q:
        metric = "Net Income"
        label = "net income"
    elif "asset" in q:
        metric = "Total Assets"
        label = "total assets"
    elif "liabilit" in q or "debt" in q:
        metric = "Total Liabilities"
        label = "total liabilities"
    elif "cash flow" in q or "operating cash" in q:
        metric = "Operating Cash Flow"
        label = "operating cash flow"
    else:
        return ("I can answer questions about total revenue, net income, total assets, "
                "total liabilities, and operating cash flow. Please include a metric and year.")

    if years:
        year = years[-1]
        row = company_df[company_df["Year"] == year]
        if row.empty:
            return f"No data is available for {company} in FY{year}."
        value = row.iloc[0][metric]
        return f"{company}'s {label} in FY{year} was {money(value)}."

    if any(word in q for word in ("change", "growth", "increased", "decreased", "over the last year", "year over year", "yoy")):
        last_two = company_df.tail(2)
        if len(last_two) < 2:
            return "Not enough yearly data to calculate a change."
        previous = float(last_two.iloc[0][metric])
        current = float(last_two.iloc[1][metric])
        difference = current - previous
        pct = (difference / previous * 100) if previous else 0
        direction = "increased" if difference > 0 else "decreased" if difference < 0 else "did not change"
        return (f"{company}'s {label} {direction} from FY{int(last_two.iloc[0]['Year'])} to "
                f"FY{int(last_two.iloc[1]['Year'])} by {money(abs(difference))} ({abs(pct):.2f}%).")

    latest = company_df.iloc[-1]
    return (f"{company}'s {label} in the latest available year, FY{int(latest['Year'])}, "
            f"was {money(latest[metric])}. Ask for a specific year or ask how it changed.")

def main():
    print("Financial Chatbot (FY2023-FY2025)")
    print("Ask about Microsoft, Tesla, or Apple: revenue, net income, assets, liabilities, or operating cash flow.")
    print("Type 'exit' to quit. Figures are in USD millions.")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", answer_query(query))

if __name__ == "__main__":
    main()
