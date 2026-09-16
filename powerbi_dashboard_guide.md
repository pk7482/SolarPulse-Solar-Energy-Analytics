# SolarPulse Power BI Dashboard Guide

## 1. Import the data
Open Power BI Desktop.

Choose **Home → Get Data → Text/CSV** and import:
- `data/solar_data_cleaned.csv`

Click **Transform Data** if you want to inspect the columns, then choose **Close & Apply**.

## 2. Create these measures

Go to **Modeling → New measure** and create the following measures:

```DAX
Total Energy Produced =
SUM(solar_data_cleaned[Energy_Produced_kWh])
```

```DAX
Total Expected Energy =
SUM(solar_data_cleaned[Expected_Energy_kWh])
```

```DAX
Total Energy Loss =
SUM(solar_data_cleaned[Energy_Loss_kWh])
```

```DAX
Average Efficiency =
AVERAGE(solar_data_cleaned[Efficiency_Percent])
```

```DAX
Total Records =
COUNTROWS(solar_data_cleaned)
```

## 3. Recommended dashboard layout

### KPI cards
Create five Card visuals:
1. Total Energy Produced
2. Total Expected Energy
3. Total Energy Loss
4. Average Efficiency
5. Total Records

### Visual 1: Monthly energy production
- Visual: Line chart
- X-axis: Month
- Y-axis: Energy_Produced_kWh
- Add Expected_Energy_kWh as another line if desired.

### Visual 2: Panel comparison
- Visual: Clustered column chart
- X-axis: Panel_ID
- Y-axis: Energy_Produced_kWh
- Add a filter or slicer for Month.

### Visual 3: Panel efficiency
- Visual: Bar chart
- Y-axis: Panel_ID
- X-axis: Efficiency_Percent
- Sort from highest to lowest.

### Visual 4: Energy loss
- Visual: Column chart
- X-axis: Month
- Y-axis: Energy_Loss_kWh

### Visual 5: Temperature versus efficiency
- Visual: Scatter chart
- X-axis: Temperature_C
- Y-axis: Efficiency_Percent
- Details: Panel_ID

### Slicers
Add slicers for:
- Date
- Panel_ID
- Performance_Status
- Month

## 4. Suggested dashboard title

SolarPulse – Solar Energy Production and Efficiency Dashboard

## 5. Business questions answered
- How much energy was produced?
- How much energy was expected?
- How much energy was lost?
- Which panel performed best?
- Which panel needs attention?
- Does temperature appear related to efficiency?
- Which month had the highest production?
