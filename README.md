# Rule-Based Financial Chatbot

## Purpose
A small Python prototype that answers predefined questions about Microsoft, Tesla, and Apple for FY2023-FY2025.

## Files
- `chatbot.py` — rule-based chatbot using simple text matching and `if`-style logic.
- `financial_data.csv` — financial metrics used by the chatbot (USD millions).
- `test_results.txt` — sample test cases and expected responses.

## Requirements
- Python 3.9 or newer
- pandas

Install pandas:
```bash
python -m pip install pandas
```

## Run
Keep all files in the same folder, then run:
```bash
python chatbot.py
```

Example questions:
- What was Microsoft's total revenue in 2025?
- How did Tesla net income change over the last year?
- What are Apple's total assets in 2024?
- What was Apple's operating cash flow in 2025?

Type `exit` to stop the chatbot.

## How it works
The program reads the CSV file with pandas, identifies the company and metric from the question, and returns the matching year value or calculates the change between the latest two years when requested.

## Limitations
- Supports only Microsoft, Tesla, and Apple and the metrics included in the CSV.
- Uses simple keyword matching; it does not use a trained NLP model.
- Uses a fixed dataset and does not fetch live information.
- Financial values should be checked against original annual reports before professional use. This prototype is for learning and is not investment advice.
