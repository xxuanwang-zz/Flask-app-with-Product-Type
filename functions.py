import nltk
import re
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# set english stopwords
stop_words = set(stopwords.words('english'))

# Apply basic NLP for one piece of text
def clean_text(text):
    # Remove \n\w\s, all lower case
    text = re.sub(r'[^\w\s]', ' ', str(text).lower().strip())
    text = text.replace('\n', ' ')
    lst_text = text.split()
    
    # Remove stopwords
    lst_text = [word for word in lst_text if word not in stop_words]
    
    # Stemming (remove -ing, -ly, ...)
    ps = nltk.stem.porter.PorterStemmer()
    lst_text = [ps.stem(word) for word in lst_text]
    
    # Lemmatisation (convert the word into root word)
    lem = nltk.stem.wordnet.WordNetLemmatizer()
    lst_text = [lem.lemmatize(word) for word in lst_text]
    text = " ".join(lst_text)
    
    return text
    
# transfer mlb result from (a, b, c) to "a, b, c"
def mlb2string(mlbresult):
    theresult = []
    for i in range(len(mlbresult)):
        t = ""
        for j in range(len(mlbresult[i])):
            t = t + mlbresult[i][j] + ", "
        t = t.rstrip(", ")
        theresult.append(t)
    
    return theresult