import pandas as pd
import numpy as np

# 1. Load the raw dataset
data = pd.read_csv("../data/solar_data_raw.csv")

# 2. Convert the Date column into a date format
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

# 3. Check missing values
print("Missing values before cleaning:")
print(data.isnull().sum())

# 4. Fill missing numeric values with the median
data["Energy_Produced_kWh"] = data["Energy_Produced_kWh"].fillna(
    data["Energy_Produced_kWh"].median()
)

data["Temperature_C"] = data["Temperature_C"].fillna(
    data["Temperature_C"].median()
)

# 5. Create useful analysis columns
data["Energy_Loss_kWh"] = (
    data["Expected_Energy_kWh"] - data["Energy_Produced_kWh"]
)

data["Efficiency_Percent"] = (
    data["Energy_Produced_kWh"] / data["Expected_Energy_kWh"] * 100
)

data["Month"] = data["Date"].dt.strftime("%Y-%m")
data["Day"] = data["Date"].dt.day

data["Performance_Status"] = np.where(
    data["Efficiency_Percent"] >= 90,
    "Good",
    np.where(data["Efficiency_Percent"] >= 75, "Average", "Needs Attention")
)

# 6. Save the cleaned dataset
data.to_csv("../data/solar_data_cleaned.csv", index=False)

# 7. Create panel-level summary
panel_summary = data.groupby("Panel_ID", as_index=False).agg(
    Total_Energy_Produced_kWh=("Energy_Produced_kWh", "sum"),
    Total_Expected_Energy_kWh=("Expected_Energy_kWh", "sum"),
    Total_Energy_Loss_kWh=("Energy_Loss_kWh", "sum"),
    Average_Efficiency_Percent=("Efficiency_Percent", "mean"),
    Average_Temperature_C=("Temperature_C", "mean"),
    Records=("Panel_ID", "count")
)

panel_summary.to_csv("../data/panel_summary.csv", index=False)

# 8. Create monthly summary
monthly_summary = data.groupby("Month", as_index=False).agg(
    Total_Energy_Produced_kWh=("Energy_Produced_kWh", "sum"),
    Total_Expected_Energy_kWh=("Expected_Energy_kWh", "sum"),
    Total_Energy_Loss_kWh=("Energy_Loss_kWh", "sum"),
    Average_Efficiency_Percent=("Efficiency_Percent", "mean")
)

monthly_summary.to_csv("../data/monthly_summary.csv", index=False)

print("Cleaning and analysis completed successfully.")
print("Cleaned file saved as ../data/solar_data_cleaned.csv")
