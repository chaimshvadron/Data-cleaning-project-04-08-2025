import pandas as pd

class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            print(f"Loading data from: {self.file_path}")
            data = pd.read_csv(self.file_path).astype(str)
            print(f"Successfully loaded")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None