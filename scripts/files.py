import os

path = r"C:\project\data\raw"

for file in os.listdir(path):
    if file.endswith(".csv"):
        print(file)
import pandas as pd
import os

path = r"C:\project\data\raw"

for file in os.listdir(path):

    if file.endswith(".csv"):

        print("\n" + "=" * 80)
        print("FILE:", file)

        try:
            df = pd.read_csv(os.path.join(path, file))

            print("COLUMNS:")
            for col in df.columns:
                print("-", col)

            print(f"\nRows: {len(df)}")
            print(f"Columns: {len(df.columns)}")

        except Exception as e:
            print("ERROR:", e)