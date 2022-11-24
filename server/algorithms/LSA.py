from newspaper import Article
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer

def doSummarize(text):
    total = ""
    parser = PlaintextParser.from_string(text, Tokenizer('portuguese'))
    stemmer = Stemmer('portuguese')
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words('portuguese')
    for sentence in summarizer(parser.document, 5):
        total += str(sentence) + " "
    return total