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


    def average_length_by_category(self):
        
        print("Calculating average tweet length by category...")
        self.data['word_count'] = self.data[self.text_column].apply(lambda x: len(x.split()))
        avg_by_category = self.data.groupby(self.biased_column)['word_count'].mean()
        antisemitic_avg = avg_by_category.get(1, 0)
        non_antisemitic_avg = avg_by_category.get(0, 0)
        overall_avg = self.data['word_count'].mean()

        return {
            "antisemitic": antisemitic_avg,
            "non_antisemitic": non_antisemitic_avg,
            "total": overall_avg
        }


    def top_10_words(self):
        print("Finding top 10 most common words in all tweets...")
        all_text = ' '.join(self.data[self.text_column])
        words = pd.Series(all_text.split())
        top_words = words.value_counts().head(10)
        return top_words.to_dict()


    def count_uppercase_words_by_category(self):
        print("Counting uppercase words by category...")
        def uppercase_word_count(text):
            return sum(1 for word in text.split() if word.isupper() and len(word) > 1)

        self.data['uppercase_count'] = self.data[self.text_column].apply(uppercase_word_count)
        grouped = self.data.groupby(self.biased_column)['uppercase_count'].sum()
        antisemitic = grouped.get(1, 0)
        non_antisemitic = grouped.get(0, 0)
        total = self.data['uppercase_count'].sum()

        return {
            "antisemitic": antisemitic,
            "non_antisemitic": non_antisemitic,
            "total": total
        }
        
    
    