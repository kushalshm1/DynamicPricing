# DynamicPricing: Presently for Movies Only

## Approach:
  1. Extracting tweets from twitter(extractTweet.py)
  2. Writing those tweets to DataFrame and then a CSV file(Tabular Format)
  3. Preprocessing Data(preprocess.py) basically it calculates the Frequencies and Relative Frequencies for unique words      in tweet and makes the data ready for training
  4. Applying Naive Bayes algorithm just to check that is there some possibility of classification of tweets based on hype
  5. Getting the Accuracy(Which is the worst for now atleast xD)

## Dataset:
Extracted dataset contains tweets classified into three classes
1. Low Hype:0
2. Medium Hype:1
3. High Hype:2

I took information from IMDB to get movie names and then tweets

## Further improvements
1. We can also add a feature No._Of_Tweets
2. Using RNN or LSTMs for classification which is basically Deep Learning approach so we need humongous amount of data, so 3. working on collecting and preprocessing that efficiently
