import json

class DataWriter:

    def cleaned_data_to_csv(self, data, file_path='../results/tweets_dataset_cleaned.csv'):
        print("Writing data to CSV file...")
        try:
            data.to_csv(file_path, index=False)
            print(f"Data successfully written to {file_path}")
        except Exception as e:
            print(f"Error writing to CSV: {e}")


    def analysis_results_to_json(self, results, file_path='../results/results.json'):
        print("Writing analysis results to JSON file...")
        try:
            with open(file_path, 'w') as f:
                json.dump(results, f, indent=4, default=str)
            print(f"Results successfully written to {file_path}")
        except Exception as e:
            print(f"Error writing to JSON: {e}")
