# Data Cleaning Project

A data cleaning and analysis pipeline for tweets dataset.

## Project Structure

```
Data-cleaning-project-04-08-2025/
├── main.py                          # Main entry point to run the project
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── data/
│   └── tweets_dataset.csv          # Raw tweets data
├── results/
│   ├── results.json                # Analysis results
│   └── tweets_dataset_cleaned.csv  # Cleaned data
└── src/
    ├── controller.py               # Main controller managing the pipeline
    ├── loading_data.py            # Data loading module
    ├── cleaning_data.py           # Data cleaning module
    ├── analysis_data.py           # Data analysis module
    └── writing_data.py            # Results writing module
```

## How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Project
```bash
python main.py
```

## What Happens During Execution?

1. **Loading** - Loads tweets data from `data/tweets_dataset.csv`
2. **Cleaning** - Cleans the data
3. **Analysis** - Performs statistical analysis on the data
4. **Saving** - Saves cleaned data and analysis results in the `results/` folder

## Output

After running, you'll find:
- `results/tweets_dataset_cleaned.csv` - Cleaned data
- `results/results.json` - Statistical analysis results" 
