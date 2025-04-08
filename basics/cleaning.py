import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "Hello there! I’m learning NLP and it's amazing, isn't it?"

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize
tokens = word_tokenize(text)

# Remove stopwords
filtered = [word for word in tokens if word not in stopwords.words('english')]

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in filtered]

print("Final Cleaned Tokens:", stemmed)
