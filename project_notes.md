# Project Notes

## Dataset columns
- Date: date of the observation
- Panel_ID: solar panel identifier
- Energy_Produced_kWh: actual energy produced
- Expected_Energy_kWh: expected energy production
- Temperature_C: temperature during the observation

## Created columns
- Energy_Loss_kWh = Expected_Energy_kWh - Energy_Produced_kWh
- Efficiency_Percent = Energy_Produced_kWh / Expected_Energy_kWh × 100
- Month: year-month value
- Day: day of month
- Performance_Status:
  - Good: efficiency at least 90%
  - Average: efficiency from 75% to below 90%
  - Needs Attention: efficiency below 75%

## Interpretation
This is an educational analytics project. The dataset does not include panel capacity, sunlight irradiance, maintenance logs, or inverter data, so capacity factor and true technical downtime cannot be calculated reliably from this dataset alone.
