from .analysis_data import DataAnalyzer
from .cleaning_data import DataCleaner
from .loading_data import DataLoader
from .writing_data import DataWriter
import pandas as pd

class Controller:

    def run(self):
        print("Starting data analysis pipeline...")
        
        loader = DataLoader("data/tweets_dataset.csv")
        data = loader.load_data()
        if data is None:
            print("Failed to load data")
            return
        
        cleaner = DataCleaner(data)
        cleaner.basic_clean()
        
        analyzer = DataAnalyzer(data)
        results = analyzer.summary_analiza()
        writer = DataWriter()
        writer.cleaned_data_to_csv(cleaner.data, "results/tweets_dataset_cleaned.csv")
        writer.analysis_results_to_json(results, "results/results.json")
        
        print("Pipeline completed successfully!")


if __name__ == "__main__":
    controller = Controller()
    controller.run()
    
        