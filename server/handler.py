from algorithms.LSA import doSummarize as lsa_summarize
from algorithms.spacy import doSummarize as spacy_summarize
from algorithms.transformer import doSummarize as transformer_summarize

def handleRequest(text, algorithm):
    if algorithm == "LSA":
            return lsa_summarize(text)
    elif algorithm == 'Spacy':
        return spacy_summarize(text)
    elif algorithm == 'AutoTokenizer' or algorithm == 'T5':
        return transformer_summarize(text, algorithm)
    else:
        return "Algoritmo não encontrado"