CREATE DATABASE IF NOT EXISTS solarpulse;
USE solarpulse;

DROP TABLE IF EXISTS solar_energy;

CREATE TABLE solar_energy (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    panel_id VARCHAR(30),
    energy_produced_kwh DECIMAL(10,2),
    expected_energy_kwh DECIMAL(10,2),
    temperature_c DECIMAL(10,2),
    energy_loss_kwh DECIMAL(10,2),
    efficiency_percent DECIMAL(10,2),
    month_value VARCHAR(7),
    performance_status VARCHAR(30)
);

-- After creating the table, import solar_data_cleaned.csv
-- using MySQL Workbench's Table Data Import Wizard.

-- 1. Total energy produced
SELECT ROUND(SUM(energy_produced_kwh), 2) AS total_energy_produced
FROM solar_energy;

-- 2. Total energy loss
SELECT ROUND(SUM(energy_loss_kwh), 2) AS total_energy_loss
FROM solar_energy;

-- 3. Average efficiency by panel
SELECT
    panel_id,
    ROUND(AVG(efficiency_percent), 2) AS average_efficiency
FROM solar_energy
GROUP BY panel_id
ORDER BY average_efficiency DESC;

-- 4. Monthly energy production
SELECT
    month_value,
    ROUND(SUM(energy_produced_kwh), 2) AS monthly_energy_produced
FROM solar_energy
GROUP BY month_value
ORDER BY month_value;

-- 5. Panel performance ranking
SELECT
    panel_id,
    ROUND(SUM(energy_produced_kwh), 2) AS total_produced,
    ROUND(SUM(energy_loss_kwh), 2) AS total_loss,
    ROUND(AVG(efficiency_percent), 2) AS average_efficiency
FROM solar_energy
GROUP BY panel_id
ORDER BY average_efficiency DESC;

-- 6. Records needing attention
SELECT *
FROM solar_energy
WHERE performance_status = 'Needs Attention'
ORDER BY efficiency_percent ASC;

-- 7. Temperature and efficiency comparison
SELECT
    ROUND(temperature_c, 0) AS temperature_group,
    ROUND(AVG(efficiency_percent), 2) AS average_efficiency
FROM solar_energy
GROUP BY ROUND(temperature_c, 0)
ORDER BY temperature_group;
