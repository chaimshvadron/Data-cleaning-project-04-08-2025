import pandas as pd


class DataAnalyzer:

    def __init__(self, data):

        self.data = data
        self.text_column = 'Text'
        self.biased_column = 'Biased'
    
    def count_tweets_by_category(self):

        print("Analyzing tweet counts by category...")
        biased_counts = self.data[self.biased_column].value_counts()        
        antisemitic = biased_counts.get(1, 0)
        non_antisemitic = biased_counts.get(0, 0)       
        total_tweets = len(self.data)
        unspecified = total_tweets - antisemitic - non_antisemitic        
        result = {
            "antisemitic": antisemitic,
            "non_antisemitic": non_antisemitic,
            "total": total_tweets,
            "unspecified": unspecified
        }      
        return result
