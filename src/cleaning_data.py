import pandas as pd

class DataCleaner:
    
    def __init__(self, data):
        self.data = data[['Text', 'Biased']].copy()
        self.text_column = 'Text'
        self.biased_column = 'Biased'

    def remove_missing_labels(self):
        self.data = self.data.dropna(subset=[self.biased_column])

    def remove_symbols(self):
        symbols = "[!\"$%&()*+-./:;<=>?@[\]^_`{|}~\n]"
        self.data[self.text_column] = self.data[self.text_column].str.replace(symbols, '')


    def convert_to_lowercase(self):
        self.data[self.text_column] = self.data[self.text_column].str.lower()

    def basic_clean(self):
        print("Starting basic cleaning...")
        self.remove_missing_labels()
        self.remove_symbols()
        self.convert_to_lowercase()
        print("Basic cleaning completed")


    