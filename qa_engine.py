

import pandas as pd


# Supported business measures
MEASURES = {
    "sales": "Sales",
    "revenue": "Sales",
    "quantity": "Quantity",
    "units": "Quantity",
    "invoices": "InvoiceNo",
    "invoice count": "InvoiceNo",
    "orders": "InvoiceNo",
}

# Supported grouping dimensions
GROUPS = {
    "country": "Country",
    "countries": "Country",
    "product": "Description",
    "products": "Description",
    "item": "Description",
    "items": "Description",
    "month": "Year-Month",
    "monthly": "Year-Month",
    "year": "Year",
}


def _response(answer, steps, data=None):
    """Return a consistent answer structure."""
    return {
        "answer": answer,
        "steps": steps,
        "data": data
    }


def _find_measure(question):
    """Identify the requested measure."""
    for keyword in sorted(MEASURES, key=len, reverse=True):
        if keyword in question:
            return keyword
    return None


def _find_group(question):
    """Identify the requested grouping dimension."""
    for keyword in sorted(GROUPS, key=len, reverse=True):
        if keyword in question:
            return keyword
    return None


def answer_question(df, question, previous_question=None):
    """Answer supported business questions using Pandas."""

    q = (question or "").lower().strip()
    prev = (previous_question or "").lower().strip()

    if not q:
        return _response(
            "Please enter a question about the retail data.",
            "No question was provided."
        )

    # Handle unavailable measures before other calculations
    if any(term in q for term in ("profit", "margin")):
        return _response(
            "Profit and profit margin cannot be calculated because "
            "the UCI Online Retail dataset does not contain cost or "
            "profit information. This dashboard calculates sales "
            "using Quantity × UnitPrice.",
            "The requested measure is not available in the dataset. "
            "No profit value was estimated."
        )

    # Handle unsupported topics
    if any(term in q for term in (
        "weather", "sports", "politics"
    )):
        return _response(
            "That topic is outside this retail dataset. Ask about "
            "sales, quantity, invoices, countries, products, or trends.",
            "The question is outside the supported business-data scope."
        )

    # Identify follow-up questions
    is_follow_up = any(
        phrase in q for phrase in (
            "what about",
            "and the",
            "how about",
            "and what about",
            "also"
        )
    )

    # Identify measure
    measure_key = _find_measure(q)

    if measure_key is None and is_follow_up:
        measure_key = _find_measure(prev)

    if measure_key is None:
        return _response(
            "Please specify sales, quantity, or invoice/order count.",
            "No supported measure was identified."
        )

    measure = MEASURES[measure_key]

    # Identify grouping
    group_key = _find_group(q)

    if group_key is None and is_follow_up:
        group_key = _find_group(prev)

    group_col = GROUPS.get(group_key) if group_key else None

    # Identify analysis intent
    highest = any(
        word in q for word in (
            "highest", "maximum", "top", "most", "largest"
        )
    )

    lowest = any(
        word in q for word in (
            "lowest", "minimum", "least", "smallest"
        )
    )

    compare = any(
        word in q for word in (
            "compare", "comparison", "breakdown", " by "
        )
    )

    # Preserve previous ranking intent for clear follow-ups
    if is_follow_up and not highest and not lowest:
        highest = any(
            word in prev for word in (
                "highest", "maximum", "top", "most", "largest"
            )
        )

        lowest = any(
            word in prev for word in (
                "lowest", "minimum", "least", "smallest"
            )
        )

        compare = compare or any(
            word in prev for word in (
                "compare", "comparison", "breakdown", " by "
            )
        )

    if highest and lowest:
        return _response(
            "Please ask for either the highest or the lowest result, "
            "not both.",
            "The requested ranking contains conflicting directions."
        )

    # Handle empty filtered datasets
    if df.empty:
        return _response(
            "No data is available for the selected filters. "
            "Please change your country or year filters.",
            "The filtered dataset contains no rows."
        )

    # Grouped analysis
    if group_col:

        if measure == "InvoiceNo":
            grouped = (
                df.groupby(group_col)[measure]
                .nunique()
                .rename("Value")
                .reset_index()
            )
            label = "distinct invoices"

        else:
            grouped = (
                df.groupby(group_col)[measure]
                .sum()
                .rename("Value")
                .reset_index()
            )
            label = (
                "sales"
                if measure == "Sales"
                else "quantity"
            )

        if grouped.empty:
            return _response(
                "No results were found for this analysis.",
                "The grouped dataset contains no results."
            )

        # Highest result
        if highest:
            result = grouped.sort_values(
                "Value", ascending=False
            )

            row = result.iloc[0]
            value = row["Value"]

            formatted_value = (
                f"£{value:,.2f}"
                if measure == "Sales"
                else f"{value:,.0f}"
            )

            return _response(
                f"{row[group_col]} has the highest {label}: "
                f"{formatted_value}.",
                f"Grouped data by {group_col}, calculated {label}, "
                "and sorted in descending order.",
                result.head(10)
            )

        # Lowest result
        if lowest:
            result = grouped.sort_values(
                "Value", ascending=True
            )

            row = result.iloc[0]
            value = row["Value"]

            formatted_value = (
                f"£{value:,.2f}"
                if measure == "Sales"
                else f"{value:,.0f}"
            )

            return _response(
                f"{row[group_col]} has the lowest {label}: "
                f"{formatted_value}.",
                f"Grouped data by {group_col}, calculated {label}, "
                "and sorted in ascending order.",
                result.head(10)
            )

        # Breakdown and comparison
        if compare or group_key in (
            "month", "monthly", "year"
        ):
            result = grouped.sort_values(
                "Value", ascending=False
            )

            return _response(
                f"Here is the {label} breakdown by {group_col}.",
                f"Grouped data by {group_col} and calculated {label}.",
                result.head(20)
            )

        return _response(
            f"Would you like the highest, lowest, or a comparison "
            f"of {label} by {group_col}?",
            "A grouping was identified, but the requested analysis "
            "was not clear."
        )

    # Overall total
    if any(word in q for word in (
        "total", "overall", "sum"
    )):
        if measure == "InvoiceNo":
            value = df["InvoiceNo"].nunique()
            label = "distinct invoices"

        elif measure == "Sales":
            value = df["Sales"].sum()
            label = "sales"

        else:
            value = df["Quantity"].sum()
            label = "quantity"

        formatted_value = (
            f"£{value:,.2f}"
            if measure == "Sales"
            else f"{value:,.0f}"
        )

        return _response(
            f"Total {label}: {formatted_value}.",
            f"Calculated the total of {label} in the filtered data.",
            pd.DataFrame({
                "Metric": [f"Total {label}"],
                "Value": [value]
            })
        )

    return _response(
        "Please ask for a total, highest/lowest result, or breakdown "
        "by country, product, month, or year.",
        "The question did not specify a supported calculation."
    )
