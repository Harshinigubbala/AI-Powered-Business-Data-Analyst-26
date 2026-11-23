
# Validation Report — UCI Online Retail

**Dataset used:** UCI Machine Learning Repository, Online Retail (`Online Retail.xlsx`).

**Data preparation:** 541,909 source rows; 530,104 retained rows after removing rows with missing required fields, cancellation invoices (invoice number starts with `C`), non-positive quantity, and non-positive unit price.

**Sales calculation:** Sales = Quantity × UnitPrice.

## 1. Independent Calculation Checks

Expected values were calculated independently from the original Excel data using Pandas, then compared with the prepared-data functions and Q&A outputs.

| Test | Input | Independently calculated expected result | Application result | Status |
|---|---|---|---|---|
| 1 | Total sales | £10,666,684.544 | £10,666,684.54 | Pass |
| 2 | Total quantity | 5,588,376 | 5,588,376 | Pass |
| 3 | Total distinct invoices | 19,960 | 19,960 | Pass |
| 4 | Country with highest sales | United Kingdom — £9,025,222.084 | United Kingdom — £9,025,222.08 | Pass |
| 5 | Country with highest quantity | United Kingdom — 4,662,390 | United Kingdom — 4,662,390 | Pass |

## 2. Question Handling Tests

| Input | Expected behavior | Observed behavior | Status |
|---|---|---|---|
| Which country has highest sales? | Return top country, value, method, and supporting table | United Kingdom; supporting country totals returned | Pass |
| Which country has highest sales? → What about quantity? | Keep country/highest intent and change measure to quantity | United Kingdom, highest quantity 4,662,390 | Pass |
| Show sales by country | Return country breakdown | Country sales breakdown returned | Pass |
| What is the weather in Hyderabad? | Decline unsupported topic and state supported scope | Unsupported-topic response returned | Pass |
| Tell me about sales. | Ask the user to clarify the type of sales analysis required | Clarification response returned | Pass |
| What is the total sales? | Return total sales | £10,666,684.54 | Pass |
| What is the total quantity? | Return total quantity | 5,588,376 | Pass |
| Which country has the lowest sales? | Return country with lowest sales | Saudi Arabia — £145.92 | Pass |

## 3. Filter Check

The data loader and dashboard filter expressions were checked for country and year fields.

The Streamlit dashboard was launched locally. The dashboard displayed summary metrics, country sales charts, product charts, monthly sales trends, and filtered transaction data.

Interactive testing of all possible country and year filter combinations remains to be completed.

## 4. Misleading-Answer Scenario and Mitigation

**Test question:** Which country has the highest profit?

**Expected behavior:** The application should explain that profit cannot be calculated because the dataset does not contain cost or profit information.

**Observed behavior:** The application correctly responded:

"Profit and profit margin cannot be calculated because the UCI Online Retail dataset does not contain cost or profit information. This dashboard calculates sales using Quantity × UnitPrice."

**Status:** Pass

**Mitigation:** The application detects profit-related questions and prevents unsupported calculations. Sales are calculated using Quantity × UnitPrice and are not treated as profit. Cancellation invoices and non-positive quantity/price rows are excluded.

The application also documents that its sales figures are not net of returns.

## 5. Test Limitations

Python syntax, data calculations, Q&A responses, and the Streamlit dashboard were tested locally.

The dashboard displayed the expected metrics, charts, and profit-unavailable response. Further interactive testing of all filters and dashboard features may be performed.

