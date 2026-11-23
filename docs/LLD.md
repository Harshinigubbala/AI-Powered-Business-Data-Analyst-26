
# Low-Level Design (LLD)

## AI-Powered Business Data Analyst

### 1. Project Modules

The application consists of the following Python modules:

**analysis.py**
- Loads the Online Retail Excel dataset.
- Cleans missing and invalid records.
- Prepares transaction data.
- Calculates sales and other business metrics.
- Performs basic business analysis.

**dashboard.py**
- Creates the Streamlit user interface.
- Displays business summary metrics.
- Provides country and year filters.
- Displays charts and tables.
- Connects user interaction with the analysis functionality.

**qa_engine.py**
- Accepts natural-language questions.
- Identifies supported business questions.
- Performs filtering, aggregation, ranking and comparison.
- Generates answers based on available data.
- Handles ambiguous and unsupported questions.

**first_analysis.py**
- Supports initial dataset exploration and analysis.

### 2. Processing Workflow

1. Load the Excel dataset.
2. Clean and prepare the transaction records.
3. Calculate sales using Quantity multiplied by UnitPrice.
4. Make prepared data available for analysis.
5. Accept user questions and dashboard filters.
6. Process questions using the Q&A engine.
7. Calculate the requested business results.
8. Display answers, metrics, charts and tables.

### 3. Data Fields

| Field | Description |
|---|---|
| InvoiceNo | Transaction invoice number |
| StockCode | Product code |
| Description | Product description |
| Quantity | Number of products |
| InvoiceDate | Transaction date |
| UnitPrice | Price per unit |
| CustomerID | Customer identifier |
| Country | Customer country |
| Sales | Quantity multiplied by UnitPrice |

### 4. Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL

### 5. Output

The application provides:
- Total sales and quantity.
- Country-wise business analysis.
- Product-wise analysis.
- Monthly and yearly sales analysis.
- Natural-language question answering.
- Interactive dashboard visualizations.
