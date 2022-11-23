from newspaper import Article
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser

def doSummarize(text):
    parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))
    summarizer_lsa = LsaSummarizer()
    summary_2 = summarizer_lsa(parser.document, 5)
    # dp = []
    summary=""
    for sentence in summary_2:
        # lp = str(sentence)
        summary+=str(sentence) + '\n';
    # dp.append(lp)
    return summary