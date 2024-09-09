import csv
import pandas as pd

def main():
    asi_sku_regex = "^(?:\d{4}-|\d{3}-)?[A-Z]-\d{6}$"
    # Import ASI Data CSV using pandas
    df = pd.read_csv("./data.csv")

    print(df)


if __name__ == "__main__":
    main()