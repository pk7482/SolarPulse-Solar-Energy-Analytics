# SolarPulse – Solar Energy Production and Efficiency Analytics

## Project overview
SolarPulse is an end-to-end beginner-friendly data analytics project. It uses Python, SQL, and Power BI to study solar panel energy production, expected production, energy loss, efficiency, temperature, and panel performance.

## Tools used
- Python
- pandas
- NumPy
- MySQL
- Power BI
- GitHub

## Project workflow
1. Load raw solar data using Python.
2. Clean missing values.
3. Create energy loss and efficiency columns.
4. Save the cleaned dataset.
5. Store the cleaned data in MySQL.
6. Run SQL analysis queries.
7. Build an interactive Power BI dashboard.
8. Upload the project to GitHub.

## Folder structure
```text
SolarPulse_Project/
│
├── data/
│   ├── solar_data_raw.csv
│   ├── solar_data_cleaned.csv
│   ├── project_summary.csv
│   ├── panel_summary.csv
│   └── monthly_summary.csv
│
├── python/
│   └── clean_and_analyze.py
│
├── sql/
│   └── analysis_queries.sql
│
├── powerbi/
│   └── powerbi_dashboard_guide.md
│
├── docs/
│   └── project_notes.md
│
└── README.md
```

## How to run the Python part
Open a terminal inside the `python` folder and run:

```bash
python clean_and_analyze.py
```

Install the required libraries first:

```bash
pip install pandas numpy
```

## GitHub upload commands
Run these commands inside the project folder:

```bash
git init
git add .
git commit -m "Created SolarPulse solar energy analytics project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your own GitHub repository URL.

## Important note
The Power BI file itself must be created in Power BI Desktop and saved as a `.pbix` file. The guide in the `powerbi` folder explains how to build it.
