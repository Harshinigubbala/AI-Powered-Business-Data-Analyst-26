# AI-Powered Business Data Analyst

A Streamlit dashboard and rule-based natural-language question interpreter for the UCI Online Retail transaction dataset.

## 1. Dataset Source and Description

- **Source:** [UCI Machine Learning Repository – Online Retail](https://archive.ics.uci.edu/dataset/352/online-retail)
- The dataset contains transactions from a UK-based online retailer between 1 December 2010 and 9 December 2011.
- Original dataset size: 541,909 transaction rows.
- It includes invoice number, product details, quantity, invoice date, unit price, customer ID, and country.
- Country is used as the geographic dimension.
- Sales are calculated as `Quantity × UnitPrice` in GBP.
- The dataset does not contain cost or profit information.

The dataset is available at:

`data/raw/Online Retail.xlsx`

## 2. Data Preparation and Assumptions

The data preparation process includes:

- Loading the Excel dataset using Pandas.
- Converting invoice numbers and stock codes into string values.
- Handling missing required fields.
- Converting transaction dates and numeric columns into appropriate data types.
- Removing cancellation invoices beginning with `C`.
- Excluding non-positive quantities and unit prices.
- Calculating sales using `Quantity × UnitPrice`.
- Extracting year, month, and year-month information.

The original dataset contains 541,909 rows, and 530,104 rows are retained after preparation.

The dashboard reports positive completed-sales transactions. It does not calculate net revenue after returns.

## 3. Project Features

- Interactive country and year filters.
- Business summary showing total sales, total quantity, invoice count, and country count.
- Sales analysis by country.
- Top-selling product analysis.
- Monthly sales trend analysis.
- Natural-language question answering.
- Highest and lowest sales analysis.
- Total sales and quantity calculations.
- Follow-up question handling.
- Clarification for ambiguous questions.
- Unsupported-topic detection.
- Protection against misleading profit-related answers.
- Supporting tables and calculation explanations.

## 4. Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL
- Microsoft Excel

## 5. Project Structure

```text
AI_Business_Data_Analyst_Updated/
│
├── data/
│   └── raw/
│       └── Online Retail.xlsx
│
├── docs/
│   ├── architecture.md
│   ├── data_flow.md
│   └── LLD.md
│
├── analysis.py
├── dashboard.py
├── first_analysis.py
├── qa_engine.py
├── requirements.txt
├── readme.md
├── validation_report.md
└── .gitignore
```

## 6. Installation and Setup

### Step 1: Install Python

Install Python on your system.

### Step 2: Install dependencies

Run this command from the project root directory:

```bash
python -m pip install -r requirements.txt
```

### Step 3: Check the dataset

Make sure the Excel dataset is available at:

`data/raw/Online Retail.xlsx`

### Step 4: Run the dashboard

Execute:

```bash
python -m streamlit run dashboard.py
```

The Streamlit application will open in your web browser.

## 7. Question Answering Workflow

The application follows these steps:

1. Receive a natural-language question from the user.
2. Identify the requested measure, such as sales, quantity, or invoice count.
3. Identify the grouping dimension, such as country, product, month, or year.
4. Identify the requested operation, such as total, highest, lowest, or breakdown.
5. Perform calculations using Pandas on the filtered dataset.
6. Generate a plain-language answer.
7. Display calculation steps and supporting results when applicable.
8. Ask for clarification when a question is ambiguous.
9. Reject unsupported topics and unavailable measures.

The question-answering engine uses predefined rules and keyword matching rather than a generative AI API.

## 8. Validation and Testing

The application was tested for:

- Total sales calculation.
- Total quantity calculation.
- Distinct invoice count.
- Country with highest sales.
- Country with highest quantity.
- Country with lowest sales.
- Sales breakdown by country.
- Follow-up question handling.
- Ambiguous question handling.
- Unsupported-topic handling.
- Profit-related misleading question handling.

Independent calculation checks and observed results are documented in `validation_report.md`.

The Streamlit dashboard was launched locally to verify its metrics, charts, and Q&A responses. Country and year filters were also checked for changes in displayed results.

## 9. Limitations and Misleading-Answer Prevention

- The dataset contains historical transactions from one retailer.
- Sales are calculated using quantity multiplied by unit price.
- The dataset does not contain cost, profit, or profit margin information.
- Cancellation invoices and non-positive quantity/price rows are excluded.
- Sales are not net revenue after returns.
- The question interpreter supports predefined measures and grouping dimensions.
- Ambiguous questions may require clarification.
- Results depend on the selected country and year filters.
- Product descriptions may contain inconsistencies or missing values.

To reduce misleading answers, the application explains its calculations, displays supporting results, and identifies unavailable information instead of estimating unsupported values.

## 10. AI Tool Usage

AI assistance was used for coding guidance, debugging, and documentation.

The application itself uses a deterministic, rule-based natural-language question interpreter and does not call an external generative AI service.

The developer should understand and be able to explain the implementation.

## 11. Future Improvements

- Add automated unit and integration tests.
- Improve natural-language question understanding.
- Add return and net-sales analysis.
- Introduce additional business insights.
- Improve dashboard performance.
- Deploy the application online.

## 12. Project Documentation

All technical documentation is available in the `docs/` folder:

1. `docs/architecture.md` – Explains the overall system architecture.
2. `docs/data_flow.md` – Explains how data moves through the application.
3. `docs/LLD.md` – Describes the project modules, processing workflow, data fields, and technologies.
4. `validation_report.md` – Describes validation tests and their results.

---

**Project Repository:** [AI-Powered Business Data Analyst on GitHub](https://github.com/Harshinigubbala/AI-Powered-Business-Data-Analyst-26)