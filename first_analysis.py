from analysis import load_data, get_business_summary, get_country_analysis, get_product_analysis, get_monthly_analysis

if __name__ == "__main__":
    df = load_data()
    print("PREPARED DATA SHAPE:", df.shape)
    print("\\nBUSINESS SUMMARY:")
    print(get_business_summary(df))
    print("\\nTOP 10 COUNTRIES BY SALES:")
    print(get_country_analysis(df).head(10).round(2).to_string(index=False))
    print("\\nTOP 10 PRODUCTS BY SALES:")
    print(get_product_analysis(df).head(10).round(2).to_string(index=False))
    print("\\nMONTHLY SALES:")
    print(get_monthly_analysis(df).round(2).to_string(index=False))
