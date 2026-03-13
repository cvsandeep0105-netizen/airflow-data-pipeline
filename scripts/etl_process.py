import pandas as pd
# Extract
def extract_data():
    df = pd.read_csv("./data/raw_sales.csv", encoding="latin1")
    return df

# Transform
def transform_data(df):
    
    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Remove missing sales
    df = df.dropna(subset=["Sales"])

    # Create new column
    df["Profit_Margin"] = df["Profit"] / df["Sales"]

    return df

# Load
def load_data(df):
    df.to_csv("data/processed_sales.csv", index=False)

def run_etl():
    df = extract_data()
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_etl()