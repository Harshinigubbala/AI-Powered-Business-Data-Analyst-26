
# Data Flow Diagram (DFD)

## AI-Powered Business Data Analyst

```mermaid
flowchart TD
    A["Online Retail Excel Dataset"] --> B["Load Dataset"]
    B --> C["Clean and Prepare Data"]
    C --> D["Prepared Data"]

    U["User"] --> E["Enter Business Question"]
    U --> F["Select Dashboard Filters"]

    D --> G["Question Answering Engine"]
    E --> G
    G --> H["Analyze Data"]
    H --> I["Generate Answer"]
    I --> J["Display Answer and Results"]

    D --> K["Streamlit Dashboard"]
    F --> K
    K --> L["Display Charts, Metrics and Tables"]
```

## Explanation

1. Dataset: Provides original retail transaction data.
2. Load Dataset: Reads the Excel file.
3. Clean and Prepare Data: Removes invalid records and prepares sales values.
4. Prepared Data: Stores cleaned information for analysis.
5. User Input: Accepts natural-language questions and dashboard filters.
6. Question Answering Engine: Processes the user's question.
7. Analyze Data: Performs the required calculations.
8. Results: Displays answers and supporting information.
