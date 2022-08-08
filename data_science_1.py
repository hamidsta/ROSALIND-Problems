import pandas as pd
import matplotlib.pyplot as plt
from imblearn.under_sampling import  RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier




rus = RandomUnderSampler(random_state=0)
df_review_bal, df_review_bal['sentiment']=rus.fit_resample(df_review_imb[['review']],
                                                           df_review_imb['sentiment'])
df_review_bal



df_review = pd.read_csv('IMDB Dataset.csv')

# subset
df_positive=df_review[df_review['sentiment']=='positive'][:9000]
df_negative=df_review[df_review['sentiment']=='negative'][:1000]

df_review_imb = pd.concat([df_positive, df_negative])

# dealing with  Imbalanced Classes , need to reorganise
length_negative = len(df_review_imb[df_review_imb['sentiment']=='negative'])
df_review_positive = df_review_imb[df_review_imb['sentiment']=='positive'].sample(n=length_negative)
df_review_non_positive = df_review_imb[~(df_review_imb['sentiment']=='positive')]

df_review_bal = pd.concat([
    df_review_positive, df_review_non_positive
])
df_review_bal.reset_index(drop=True, inplace=True)
df_review_bal['sentiment'].value_counts()

#The df_review_bal dataframe should have now 1000 positive and negative reviews as shown above.

# Splitting data into train and test set
# We’ll use sklearn’s train_test_split to do the job. In this case, we set 33% to the test data.

train, test = train_test_split(df_review_bal, test_size=0.33, random_state=42)

train_x, train_y = train['review'], train['sentiment']

test_x, test_y = test['review'], test['sentiment']

# Turning our text data into numerical vectors
#  we want to identify unique/representative words for positive reviews and negative reviews, so we’ll choose the TF-IDF.

tfidf = TfidfVectorizer(stop_words='english')
train_x_vector = tfidf.fit_transform(train_x)
# display as a matrix
matrix=pd.DataFrame.sparse.from_spmatrix(train_x_vector,
                                  index=train_x.index,
                                  columns=tfidf.get_feature_names())

test_x_vector = tfidf.transform(test_x)
# now we have numerical data
# notes: better to use tokenization and removing extra words considering
# as irrelevent

# Supervised vs Unsupervised learning
# we have labeled input and output data , therefore, we’re dealing with supervised learning
#Two common types of supervised learning algorithms are Regression and Classification.
#Regression: They’re used to predict continuous values such as price, salary, age, etc
#Classification: They’re used to predict discrete values such as male/female, spam/not spam, positive/negative, etc.


# four classification models.
 # 1) support Vector Machines (SVM)
  # To fit an SVM model, we need to introduce the input (text reviews as numerical vectors) and output (sentiment)
svc = SVC(kernel='linear')
svc.fit(train_x_vector, train_y)

# Decision Tree
# To fit a decision tree model, we need to introduce the input (text reviews as numerical vectors)
# and output (sentiment)
dec_tree = DecisionTreeClassifier()
dec_tree.fit(train_x_vector, train_y)
print(svc.predict(tfidf.transform(['A good movie'])))
print(svc.predict(tfidf.transform(['An excellent movie'])))
print(svc.predict(tfidf.transform(['I did not like this movie at all'])))



