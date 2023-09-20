# %%
#Webscraping reviews and sentiment analysis 
#Use BeautifulSoup to webscrape reviews and TextBlob to perform sentiment analysis. 
#All packages used have been already installed using %pip install

# %%
#Write a Python function that takes the parameter url and returns a list of reviews. URL is the input.

#Used the following URLs to test the function:
#https://www.rottentomatoes.com/m/spider_man_across_the_spider_verse/reviews
#https://www.rottentomatoes.com/m/the_little_mermaid_2023/reviews
#https://www.rottentomatoes.com/m/barbie/reviews

# %%
def rev():
    import requests
    from bs4 import BeautifulSoup

    URLstr = input("enter URL:")
    mURL = requests.get(URLstr)
    html = mURL.text

    soup = BeautifulSoup(html, 'html.parser')
    reviews = soup.findAll('p',{'class':'review-text'})

    for review in reviews:
        print(review.text.strip()+"\n\n")

print(rev())

# %%
#Get Barbie reviews
#https://www.rottentomatoes.com/m/barbie/reviews
print(rev())

# %%
#Get Little Mermaid Reviews
#https://www.rottentomatoes.com/m/the_little_mermaid_2023/reviews
print(rev())

# %%
# Get Spiderman: Across the Spiderverse Reviews
#https://www.rottentomatoes.com/m/spider_man_across_the_spider_verse/reviews

print(rev())

# %%
#Append reviews to a list for sentiment analysis

# %%
#Create empty list for Barbie and append reviews
barbiereviews = []


import requests
from bs4 import BeautifulSoup

URLstr = "https://www.rottentomatoes.com/m/barbie/reviews"
mURL = requests.get(URLstr)
html = mURL.text

soup = BeautifulSoup(html, 'html.parser')
reviews = soup.findAll('p',{'class':'review-text'})

for review in reviews:
    barbtext = review.text.strip()+"\n\n"
    barbiereviews.append(barbtext)

print("Barbie Reviews:", barbiereviews)

# %%
#Create empty list for Little Mermaid and append reviews
mermaidreviews = []

import requests
from bs4 import BeautifulSoup

URLstr = "https://www.rottentomatoes.com/m/the_little_mermaid_2023/reviews"
mURL = requests.get(URLstr)
html = mURL.text

soup = BeautifulSoup(html, 'html.parser')
reviews = soup.findAll('p',{'class':'review-text'})

for review in reviews:
    mertext = review.text.strip()+"\n\n"
    mermaidreviews.append(mertext)

print("Little Mermaid Reviews:", mermaidreviews)

# %%
#Create empty list for Spiderman and append reviews
spidermanreviews = []

import requests
from bs4 import BeautifulSoup

URLstr = "https://www.rottentomatoes.com/m/spider_man_across_the_spider_verse/reviews"
mURL = requests.get(URLstr)
html = mURL.text

soup = BeautifulSoup(html, 'html.parser')
reviews = soup.findAll('p',{'class':'review-text'})

for review in reviews:
    spidertext = review.text.strip()+"\n\n"
    spidermanreviews.append(spidertext)

print("Spiderman Reviews:", spidermanreviews)

# %%
#Sentiment Analysis

# %%
from textblob import TextBlob

# %%
#Barbie Reviews
barbiereviewtext = barbiereviews

for text in barbiereviewtext:
    barbieblob = TextBlob(text)
    polarity = barbieblob.sentiment.polarity
    subjectivity = barbieblob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print()

# %%
#The Little Mermaid Reviews

lilmermaidtext = mermaidreviews

for text in lilmermaidtext:
    mermaidblob = TextBlob(text)
    polarity = mermaidblob.sentiment.polarity
    subjectivity = mermaidblob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print()


# %%
#Spiderman: Across the Spiderverse
spidermantext = spidermanreviews

for text in spidermantext:
    spiderblob = TextBlob(text)
    polarity = spiderblob.sentiment.polarity
    subjectivity = spiderblob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print()

# %%
#Find the movie with the highest (most postive) sentiment using polarity scores.
#First create a list for each movie of only polarity scores. Then calculate the averages and compare them. 

# %%
#Barbie
barbiepolarity = []

for text in barbiereviewtext:
    barbieblob = TextBlob(text)
    polarity = barbieblob.sentiment.polarity
    barbiepolarity.append(polarity)

barbiepolarity

# %%
#The Little Mermaid 
mermaidpolarity = []

for text in lilmermaidtext:
    mermaidblob = TextBlob(text)
    polarity = mermaidblob.sentiment.polarity
    mermaidpolarity.append(polarity)

mermaidpolarity

# %%
#Spiderman: Across the Spiderverse
spidermanpolarity = []

for text in spidermantext:
    spiderblob = TextBlob(text)
    polarity = spiderblob.sentiment.polarity
    spidermanpolarity.append(polarity)

spidermanpolarity

# %%
#Save the averages as variables

Barb_avg = sum(barbiepolarity)/len(barbiepolarity)

LM_avg = sum(mermaidpolarity)/len(mermaidpolarity)

Spider_avg = sum(spidermanpolarity)/len(spidermanpolarity)

# %%
#Compare averages between movies to determine the movie with the highest poplarity (most positive sentiment).

a = [Barb_avg, LM_avg, Spider_avg]
b = max(a)

if Barb_avg >= b:
  print("The movie with the highest average polarity (most positive sentiment) is Barbie")
elif LM_avg >= b:
  print("The movie with the highest average polarity (most positive sentiment) is The Little Mermaid")
elif Spider_avg >= b:
  print("The movie with the highest average polarity (most positive sentiment) is the Spiderman: Across the Spiderverse")
else:
  print ("All the movies' polarities are equal")


