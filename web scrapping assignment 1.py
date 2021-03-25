#!/usr/bin/env python
# coding: utf-8

# # 1.Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")
soup 


# In[6]:



headers = soup.find_all(['h1','h2','h3','h4','h5','h6'])


# In[7]:


print('List all the header tags :',headers, sep='\n')


# # 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of Release

# In[8]:


page1 = requests.get("https://www.imdb.com/list/ls091520106/")


# In[9]:


bc = BeautifulSoup(page1.content, "html.parser")


# In[10]:


print(bc.prettify())


# In[11]:


Name =[]
IMDB_Rating = []
Year_of_Release = []


# In[12]:


movie_div = bc.find_all('div', class_='lister-item-content')


# In[13]:


for i in movie_div:
        name = i.h3.a.text
        Name.append(name) 
        
        
        year = i.h3.find('span', class_='lister-item-year').text
        Year_of_Release.append(year)


# In[14]:


rating = bc.find_all('div',class_="ipl-rating-star small")


# In[15]:


for j in rating:
    x = j.find('span',class_='ipl-rating-star__rating')
    IMDB_Rating.append(x)


# In[17]:


import pandas as pd
movie = pd.DataFrame({})
movie['Name'] = Name[:100]
movie['Rating'] = IMDB_Rating[:100]
movie['Release_Year'] = Year_of_Release[:100]


# In[18]:



movie.head()


# # 3)Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year of release)

# In[19]:


page2 = requests.get('https://www.imdb.com/list/ls009997493/?sort=user_rating,desc&st_dt=&mode=detail&page=1')


# In[20]:


soup1 = BeautifulSoup(page2.content, "html.parser")


# In[21]:


Name =[]
IMDB_Rating = []
Year_of_Release = []


# In[22]:


movie_div = soup1.find_all('div', class_='lister-item-content')


# In[23]:


for x in movie_div:
        name = x.h3.a.text
        Name.append(name) 
        
        
        year = x.h3.find('span', class_='lister-item-year').text
        Year_of_Release.append(year)


# In[24]:


rating = soup1.find_all('div',class_="ipl-rating-star small")


# In[25]:



for j in rating:
    r = j.find('span',class_='ipl-rating-star__rating')
    IMDB_Rating.append(r)


# In[27]:




Hindi_movie = pd.DataFrame({})
Hindi_movie['Name'] = Name[:100]
Hindi_movie['Rating'] = IMDB_Rating[:100]
Hindi_movie['Release_Year'] = Year_of_Release[:100]


# In[28]:


Hindi_movie.head()


# # 4) Write a python program to scrap book name, author name, genre and book review of any 5 books

# In[29]:


book1 = requests.get('https://bookpage.com/reviews/25867-dantiel-w-moniz-milk-blood-heat-fiction#.YBjXbugzY2w')


# In[30]:


soup = BeautifulSoup(book1.content, "html.parser")


# In[31]:



Book_Name = soup.find_all('h1',class_="italic")
for i in Book_Name:
    Book_Name = i.get_text()
    print("BOOK NAME: ",Book_Name)
Author_Name = soup.find_all('h4',class_="sans")
for i in Author_Name:
    Author_Name = i.get_text()
    print("AUTHOR NAME: ",Author_Name)
Book_Review = soup.find_all('div',class_="article-body")
for i in Book_Review:
    Book_Review = i.get_text()
    print("REVIEW : ",Book_Review)
Genre = soup.find_all('p',class_="genre-links")
for i in Genre:
    Genre = i.a.text
    print("GENRE: ", Genre)


# In[32]:


book2 = requests.get('https://bookpage.com/reviews/25833-lauren-oyler-fake-accounts-fiction#.YBje4-gzY2w')


# In[33]:


soup1 = BeautifulSoup(book2.content, "html.parser")


# In[34]:


Book2_Name = soup1.find_all('h1',class_="italic")
for i in Book2_Name:
    Book2_Name = i.get_text()
    print("BOOK NAME: ",Book2_Name)
Author2_Name = soup1.find_all('h4',class_="sans")
for i in Author2_Name:
    Author2_Name = i.get_text()
    print("AUTHOR NAME: ",Author2_Name)
Book2_Review = soup1.find_all('div',class_="article-body")
for i in Book2_Review:
    Book2_Review = i.get_text()
    print("REVIEW: ",Book2_Review)
Genre2 = soup1.find_all('p',class_="genre-links")
for i in Genre2:
    Genre2 = i.a.text
    print("GENRE: ",Genre2)


# In[35]:


book3 = requests.get('https://bookpage.com/reviews/25934-joanna-schaffhausen-every-waking-hour-mystery-suspense#.YBjk9ugzY2w')


# In[36]:



soup2 = BeautifulSoup(book3.content, "html.parser")


# In[37]:


Book3_Name = soup2.find_all('h1',class_="italic")
for i in Book3_Name:
    Book3_Name = i.get_text()
    print("BOOK NAME: ",Book3_Name)
Author3_Name = soup2.find_all('h4',class_="sans")
for i in Author3_Name:
    Author3_Name = i.get_text()
    print("AUTHOR NAME: ",Author3_Name)
Book3_Review = soup2.find_all('div',class_="article-body")
for i in Book3_Review:
    Book3_Review = i.get_text()
    print("REVIEW: ",Book3_Review)
Genre3 = soup2.find_all('p',class_="genre-links")
for i in Genre3:
    Genre3 = i.a.text
    print("GENRE: ",Genre3)


# In[38]:


book4 = requests.get('https://bookpage.com/reviews/25932-harper-st-george-heiress-gets-duke-romance#.YBjmZ-gzY2w')


# In[39]:


soup3 = BeautifulSoup(book4.content,'html.parser')


# In[40]:


Book4_Name = soup3.find_all('h1',class_="italic")
for i in Book4_Name:
    Book4_Name = i.get_text()
    print("BOOK NAME: ",Book4_Name)
Author4_Name = soup3.find_all('h4',class_="sans")
for i in Author4_Name:
    Author4_Name = i.get_text()
    print("AUTHOR NAME: ",Author4_Name)
Book4_Review = soup3.find_all('div',class_="article-body")
for i in Book4_Review:
    Book4_Review = i.get_text()
    print("REVIEW: ",Book4_Review)
Genre4 = soup3.find_all('p',class_="genre-links")
for i in Genre4:
    Genre4 = i.a.text
    print("GENRE: ",Genre4)


# In[41]:


book5 = requests.get('https://bookpage.com/reviews/25893-rajani-larocca-red-white-whole-childrens#.YBjnjegzY2w')


# In[42]:


soup4 = BeautifulSoup(book5.content,'html.parser')


# In[43]:


Book5_Name = soup4.find_all('h1',class_="italic")
for i in Book5_Name:
    Book5_Name = i.get_text()
    print("BOOK NAME: ",Book5_Name)
Author5_Name = soup4.find_all('h4',class_="sans")
for i in Author5_Name:
    Author5_Name = i.get_text()
    print("AUTHOR NAME: ",Author5_Name)
Book5_Review = soup4.find_all('div',class_="article-body")
for i in Book5_Review:
    Book5_Review = i.get_text()
    print("REVIEW: ",Book5_Review)
Genre5 = soup4.find_all('p',class_="genre-links")
for i in Genre5:
    Genre5 = i.a.text
    print("GENRE: ",Genre5)


# # 5 &6)Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:\ i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating. \ ii) Top 10 ODI Batsmen in men along with the records of their team and rating. \ iii) Top 10 ODI bowlers along with the records of their team and rating.

# In[44]:


url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
r = requests.get(url)
r.content
soup = BeautifulSoup(r.content, "html.parser")

maindiv = soup.find_all("div", {"class": "rankings-block__container full rankings-table"})
for div in maindiv:
    print(div.text[:450])


# In[45]:


url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting"
r = requests.get(url)
r.content
soup = BeautifulSoup(r.content, "html.parser")

maindiv = soup.find_all("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})
for div in maindiv:
    print(div.text)


# In[46]:


url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling"
r = requests.get(url)
r.content
soup = BeautifulSoup(r.content, "html.parser")

maindiv = soup.find_all("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})
for div in maindiv:
    print(div.text)


# In[47]:


r = requests.get(url)
r.content
soup = BeautifulSoup(r.content, "html.parser")

maindiv = soup.find_all("div", {"class":"cb-col cb-col-100 cb-font-14 cb-lst-itm text-center"})
for div in maindiv:
    print(div.text)


# # 8) Write a python program to extract information about the local weather from the National Weather Service website of USA, https://www.weather.gov/ for the city, San Francisco.

# In[49]:


site = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(site.content, 'html.parser')
result = soup.find(id="seven-day-forecast")
forecast = result.find_all(class_="tombstone-container")
today = forecast[0]
print(today.prettify())


# In[50]:


period = today.find(class_='period-name').get_text()
description = today.find(class_='short-desc').get_text()
temperature = today.find(class_='temp').get_text()
print(period)
print(description)
print(temperature)


# In[51]:



days_tags = result.select(".tombstone-container .period-name")
days = [pt.get_text() for pt in days_tags]
days


# In[53]:


short_descs = [sd.get_text() for sd in result.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in result.select(".tombstone-container .temp")]
descs = [d["title"] for d in result.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


# In[54]:


weather = pd.DataFrame({
        "period": days,
         "short_desc": short_descs,
         "temp": temps,
         "desc":descs
    })
weather


# In[ ]:




