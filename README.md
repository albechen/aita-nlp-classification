# "Am I the Asshole" Reddit NLP Classification

**Creating CNN model and using NLP techniques to predict verdict of "Am I the Asshole?" posts on reddit.com/r/AITA**

**Language:** Python (tensorflow, sklearn, nltk, seaborn, gensim)

On Reddit there is a subreddit where people can post thier situation to ask the general public if they were the asshole in the situation they write about. The goal is to see from the post's body and title - if we can predict what verdict the comments will decide on.

The focus of the project was (1) to learn more about NLP techniques and how to apply them to real world data (2) to work with API's and pulling data for my own dataset.
Therefore, I was not focusing on the actual modeling or chasing better results.

- [1: data_collection](https://github.com/albechen/aita-nlp-classification/blob/main/aita-1-data_collection.ipynb) <br/>
Data pulls using Reddit's API to consistently grab chunks of posts and subsequent verdicts

- [1.5: recent_data_collection](https://github.com/albechen/aita-nlp-classification/blob/main/aita-1.5-recent_data_collection.ipynb) <br/>
Created shorter method to grab latest data to update dataset with new posts

- [2: inital_analysis](https://github.com/albechen/aita-nlp-classification/blob/main/aita-2-inital_analysis.ipynb) <br/>
Initial data exploration to see distribution of posts types and verdicts

- [3: tfidf_tokens_model](https://github.com/albechen/aita-nlp-classification/blob/main/aita-3-tfidf_tokens_model.ipynb) <br/>
Created simple models using word frequency and tokenizing to convert bodies to matrices and preformed simple regression and random forests models as baseline test

- [4: word2vec_cnn](https://github.com/albechen/aita-nlp-classification/blob/main/aita-4-word2vec_cnn.ipynb) <br/>
Created CNN model on word2vec vectorized bodies to garner main idea of posts to simple vectors

## Results

### Initial Data Exploration:

Definitions for the metrics compared:

    1) score - score of posts that users can upvote
    2) num_comments - number of comments to gauge engagement
    3) length_body - how long the post was
    4) upvote_ratio - how many upvotes to downvotes there were


Each post's verdicts are as follows:

    1) NTA "Not the asshole"
    2) YTA "Your the asshole"
    3) ESH "Everyone's the asshole"
    4) NAH "No assholes here"

Generally the main focus is on NTA and YTA posts. As generally thought, NTA posts are generally scored higher

![Alt text](/data/images/result_dist.jpg)

For each post there are two types

    1) AITA "Am I the ..."     - more common
    2) WIBTA "Would I be..."   - less common

It's observed that generally people are most interested in AITA posts which are more common and generally longer

![Alt text](/data/images/post_dist.jpg)

### Modeling Results:
| Model | Accuracy |
| ----------- | ----------- |
| Naive Model|50 %|
|Log Regression + TFIDF|53 %|
|Random Forest + TFIDF|51 %|
|CNN + word2vec|73 %|
