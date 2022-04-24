from newspaper import Article
import nltk
nltk.download('punkt')
url= 'https://www.miaminewtimes.com/news/meet-the-gen-z-tenants-displaced-from-coral-gables-and-priced-out-of-miami-14282338'
article = Article(url, language="en") # en for English 
article.download() 
article.parse() 
article.nlp()
print("Article Title:") 
print(article.title) #prints the title of the article
print("\n") 
print("Article Text:") 
print(article.text) #prints the entire text of the article
print("\n") 
print("Article Summary:") 
print(article.summary) #prints the summary of the article
print("\n") 
print("Article Keywords:")
print(article.keywords) #prints the keywords of the article