
# System Architecture Diagram

## AI-Powered Business Data Analyst

```mermaid
flowchart TD
    A["Online Retail Dataset"] --> B["Data Preparation - analysis.py"]
    B --> C["Cleaned Data"]
    C --> D["Streamlit Dashboard - dashboard.py"]

    U["User"] --> E["Natural Language Question"]
    U --> F["Country and Year Filters"]

    E --> G["Q&A Engine - qa_engine.py"]
    C --> G
    G --> H["Data Analysis"]
    H --> I["Answer and Supporting Results"]
    I --> D

    F --> D
    D --> J["Charts, Metrics and Tables"]
```

## Explanation

1. Dataset: Uses the Online Retail Excel dataset.
2. Data Preparation: analysis.py loads and cleans the data.
3. Cleaned Data: Prepared data is used for analysis.
4. Dashboard: dashboard.py displays metrics, charts and filters.
5. Q&A Engine: qa_engine.py processes natural-language questions.
6. Data Analysis: Performs filtering, aggregation, comparison and ranking.
7. Results: Displays answers and supporting results.
