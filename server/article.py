from newspaper import Article

def extractTextFromUrl(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
