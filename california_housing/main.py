import pandas as pd


path_to_train = "sample_data/california_housing_train.csv"

# task 40

df = pd.read_csv(path_to_train)

sub_df = df[df["population"] >= 0][df["population"] <= 500]

print(
    sub_df["median_house_value"].mean()
)

# task 42

sub_df = df[df["population"] == df["population"].min()]

print(
    sub_df["households"]
)