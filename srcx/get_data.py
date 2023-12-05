import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
from datetime import datetime
import seaborn as sns
import string
import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from collections import Counter
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
from datetime import datetime
import seaborn as sns
import string
from dateutil import parser

# 1.) Workflow: Search for "artifical intelligence", searching for ***posts***, sort by ***newest***, using selenium 

url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=386bfe8d-cafa-4df6-af02-ad551526afeb&sort=new"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    # Extracting the titles of threads 
    tag_list_1 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_1.append(tag.get_text())
else:
    raise Exception("Status code is not 200")
# This will just grab the titles and cut off the useless reddit threads at the end
newest_post_titles = tag_list_1[:246]
# This will just grab the titles and cut off the useless reddit threads at the end
newest_post_titles = tag_list_1[:246]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
newest_post_titles_word_counts_dict_final = dict(word_counts) 
sorted_newest_post_titles_word_counts_dict = sorted(newest_post_titles_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)

# Exporting number 1 to a csv:
with open('data/raw/dict1_newest_post_titles.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in newest_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
# 2.) Workflow: Search for "artifical intelligence", searching for ***comment***, sort by ***newest***, using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=comment&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=b84e0b3c-e204-44fd-b755-a09ef613f8c6&sort=new"
response = requests.get(url)
if response.status_code == 200:
    driver = webdriver.Safari()
    driver.get(url)
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) 
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_2 = []
# Iterating through comments dynamically
    for i in range(0, 295):
        content = soup.find("span", id=f"comment-content-{i}")
        if content:
            # Check if the element contains a link
            if content.find("a"):
                # Skip this iteration entirely
                continue
            tag_list_2.append(content.get_text())
all_text = ' '.join(tag_list_2)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
# Convert the sorted result to a dictionary
newest_comments_dict = dict(word_counts)
# And here is it sorted from highest to lowest
sorted_newest_comments_dict = sorted(newest_comments_dict.items(), key=lambda x: x[1], reverse=True)

with open('data/raw/dict2_newest_comments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in newest_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
# 3.) Workflow: Search for "artifical intelligence", searching for ***post***, sort by ***most comments***, using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=1e881230-3c5d-4f22-b9ec-f7caa041cc7c&sort=comments"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    # Extracting the titles of threads 
    tag_list_3 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_3.append(tag.get_text())
else:
    raise Exception("Status code is not 200")
# This will just grab the titles and cut off the useless reddit threads at the end
newest_post_titles_3 = tag_list_3[:243]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_3)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
most_comment_post_titles_word_counts_dict_final = dict(word_counts) 
sorted_most_comment_post_titles_word_counts_dict_final = sorted(most_comment_post_titles_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting #3 to a csv:
with open('data/raw/dict3_most_comment_post_titles_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in newest_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
# 4.) Workflow: Search for "artifical intelligence", searching for ***comment***, sort by ***relevance***, using selenium
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=comment&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=44a60ee4-76ac-47e0-8051-a495f3c21a93&sort=relevance"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_4 = []
    # Iterating through comments dynamically
    for i in range(0, 295):
        content = soup.find("span", id=f"comment-content-{i}")
        if content:
            # Check if the element contains a link
            if content.find("a"):
                # Skip this iteration entirely
                continue
            tag_list_4.append(content.get_text())
all_text = ' '.join(tag_list_4)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
relevance_comments_word_counts_dict_final = dict(word_counts)
# And here is it sorted from highest to lowest
sorted_relevance_comments_word_counts_dict_final = sorted(relevance_comments_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting fourth to a csv:

with open('data/raw/dict4_relevance_comments_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in newest_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
# 5.) Workflow: Search for "artifical intelligence", searching for ***comments***, sort by ***TOP***, using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=comment&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=e0e3857f-f489-4088-960e-04f77053f59e&sort=top"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_5 = []
    # Iterating through comments dynamically
    for i in range(0, 200):
        content = soup.find("span", id=f"comment-content-{i}")
        if content:
            # Check if the element contains a link
            if content.find("a"):
                # Skip this iteration entirely
                continue
            tag_list_5.append(content.get_text())
all_text = ' '.join(tag_list_5)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
# Final dictionary containing the count of each word in  Search for "artifical intelligence", searching for comments, sort by newest
top_comments_word_counts_dict = dict(word_counts)
sorted_top_comments_word_counts_dict = sorted(top_comments_word_counts_dict.items(), key=lambda x: x[1], reverse=True)
# Exporting fifth to a csv:

with open('data/raw/dict5_top_comment_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in newest_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
#6.) Workflow: Search for "artifical intelligence", searching for ***posts***, sort by ***TOP***, using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=a067c5d1-726a-4799-b2eb-ab5b44e4b6f5&sort=top"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_6 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_6.append(tag.get_text())
newest_post_titles_6 = tag_list_6[:247]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_6)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
top_post_titles_word_counts_dict_final = dict(word_counts) 
sorted_top_post_titles_word_counts_dict_final = sorted(top_post_titles_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting sixth to a csv:
with open('data/raw/dict6_top_post_titles_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in top_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
#7.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***HOT***, using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=f5c7c150-40e2-4794-a147-6132abe91bd0&sort=hot"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_7 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_7.append(tag.get_text())
newest_post_titles_7 = tag_list_7[:246]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_7)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
hot_post_titles_word_counts_dict_final = dict(word_counts) 
sorted_hot_post_titles_word_counts_dict_final = sorted(hot_post_titles_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting seventh to a csv:
with open('data/raw/dict7_hot_post_titles_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in hot_post_titles_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
#8.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***HOT***, within the ***past year*** using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=f4eb9063-ba8d-416b-970f-8c7834152541&t=year&sort=top"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_8 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_8.append(tag.get_text())
newest_post_titles_8 = tag_list_8[:246]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_8)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
hot_post_titles_past_year_word_counts_dict_final = dict(word_counts) 
sorted_hot_post_titles_past_year_word_counts_dict_final = sorted(hot_post_titles_past_year_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting eighth to a csv:
with open('data/raw/dict8_hot_post_titles_past_year_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in hot_post_titles_past_year_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
# 9.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***Relevance***, within the ***past year*** using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=90a75a27-d6fb-4f06-9899-4a3da653f393&t=year&sort=relevance"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_9 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_9.append(tag.get_text())
newest_post_titles_9 = tag_list_9[:246]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_9)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
relevance_post_titles_past_year_word_counts_dict_final = dict(word_counts) 
sorted_relevance_post_titles_past_year_word_counts_dict_final = sorted(relevance_post_titles_past_year_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting ninth to a csv:
with open('data/raw/dict9_relevance_post_titles_past_year_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in relevance_post_titles_past_year_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
#10.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***Most Comments***, within the ***past year*** using selenium
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=09ea418e-5aa8-4a99-8a28-950362ff385e&t=year&sort=comments"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    tag_list_10 = []
    invisible_tags = soup.find_all("span", class_="invisible")
    for tag in invisible_tags:
        tag_list_10.append(tag.get_text())
newest_post_titles_10 = tag_list_10[:246]
# Combine all text into a single string
all_text = ' '.join(newest_post_titles_10)
# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = all_text.translate(translator).lower()
# Tokenize the cleaned text
tokens = cleaned_text.split()
# Count the occurrences of each word
word_counts = Counter(tokens)
most_comments_post_titles_past_year_word_counts_dict_final = dict(word_counts) 
sorted_most_comments_post_titles_past_year_word_counts_dict_final = sorted(most_comments_post_titles_past_year_word_counts_dict_final.items(), key=lambda x: x[1], reverse=True)
# Exporting tenth to a csv:
with open('data/raw/dict10_most_comments_post_titles_past_year_word_counts_dict_final.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in most_comments_post_titles_past_year_word_counts_dict_final.items():
        w.writerow([key, value])
# ----------------------------------------------------------------------------------------------------------------------------------------
#11.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***TOP***, ***all time***, and gathering the date posted, and amount of interactions using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=a68725fb-6ca9-4487-bd00-7b02cc9f1e3a&t=all&sort=top"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    final_top_date_time_vote_comment_dict = []
    invisible_tags = soup.find_all("time")
    invisible_tags_titles = soup.find_all("span", class_="invisible")
    vote_comment_divs = soup.find_all('div', class_='text-neutral-content-weak text-12')
    name_tags = soup.find_all("a", class_= "flex items-center text-neutral-content-weak font-semibold")
# Iterate over both lists simultaneously using zip
for time_tag, title_tag, div, name_tag in zip(invisible_tags, invisible_tags_titles, vote_comment_divs, name_tags):
    # Extract date information from the <time> tag
    date_value = time_tag['title']
    # Extract post title from the <span> tag
    title = title_tag.get_text(strip=True)
    # Extract votes
    votes_tag = div.find('faceplate-number', {'pretty': ''})
    votes = votes_tag['number']
    # Extract comments
    comments_tag = div.find('span', string='comments')
    comments = comments_tag.find_previous('faceplate-number')['number']
    subreddit = name_tag["href"]
    # Print both date, title, votes, and comments
    #print(f"Date: {date_value}, Title: {title}, Votes = {votes}, Comments = {comments}, Subreddit= {subreddit}")
    final_top_date_time_vote_comment_dict.append({
        "Title": title,
        "Subreddit": subreddit,
        "Date": date_value,
        "Votes": int(votes),
        "Comments": int(comments),  
    })
#12.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***most comments***, ***all time***, and gathering the date posted, and amount of interactions using selenium 
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=fc7a51aa-31c1-4df4-8e8d-f632f66fcbb3&t=all&sort=comments"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    final_most_coments_date_time_vote_comment_dict = []
    invisible_tags = soup.find_all("time")
    invisible_tags_titles = soup.find_all("span", class_="invisible")
    vote_comment_divs = soup.find_all('div', class_='text-neutral-content-weak text-12')
    name_tags = soup.find_all("a", class_= "flex items-center text-neutral-content-weak font-semibold")
# Iterate over both lists simultaneously using zip
for time_tag, title_tag, div, name_tag in zip(invisible_tags, invisible_tags_titles, vote_comment_divs, name_tags):
    # Extract date information from the <time> tag
    date_value = time_tag['title']
    # Extract post title from the <span> tag
    title = title_tag.get_text(strip=True)

    # Extract votes
    votes_tag = div.find('faceplate-number', {'pretty': ''})
    votes = votes_tag['number']

    # Extract comments
    comments_tag = div.find('span', string='comments')
    comments = comments_tag.find_previous('faceplate-number')['number']
    subreddit = name_tag["href"]
    # Print both date, title, votes, and comments
    #print(f"Date: {date_value}, Title: {title}, Votes = {votes}, Comments = {comments}, Subreddit= {subreddit}")
    final_most_coments_date_time_vote_comment_dict.append({
        "Title": title,
        "Subreddit": subreddit,
        "Date": date_value,
        "Votes": int(votes),
        "Comments": int(comments),  
    })
#13.) Workflow: Search for "artificial intelligence", searching for ***posts***, sort by ***Relevance***, ***all time***, and gathering the date posted, and amount of interactions using selenium
url = "https://www.reddit.com/search/?q=artificial+intelligence&type=link&cId=daed8c04-82aa-4737-8bf2-cf9e69e933fc&iId=02b2cbc7-61a7-40dc-952f-34bbb143a748&sort=relevance"
response = requests.get(url)
if response.status_code == 200:
    # Using the safari driver
    driver = webdriver.Safari()
    # Opening the URL
    driver.get(url)
    # Scroll down to load more content, here I went to ten because that is the maximum amount of times it can scroll
    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #: I will need a longer sleep time if I'm trying to load more titles
    # Getting the updated HTML content
    html_content = driver.page_source
    # Closing the browser
    driver.quit()
    # Parsing the html content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    final_relevance_date_time_vote_comment_dict = []
    invisible_tags = soup.find_all("time")
    invisible_tags_titles = soup.find_all("span", class_="invisible")
    vote_comment_divs = soup.find_all('div', class_='text-neutral-content-weak text-12')
    name_tags = soup.find_all("a", class_= "flex items-center text-neutral-content-weak font-semibold")
# Iterate over both lists simultaneously using zip
for time_tag, title_tag, div, name_tag in zip(invisible_tags, invisible_tags_titles, vote_comment_divs, name_tags):
    # Extract date information from the <time> tag
    date_value = time_tag['title']
    # Extract post title from the <span> tag
    title = title_tag.get_text(strip=True)

    # Extract votes
    votes_tag = div.find('faceplate-number', {'pretty': ''})
    votes = votes_tag['number']

    # Extract comments
    comments_tag = div.find('span', string='comments')
    if comments_tag:
        # Find the previous 'faceplate-number' tag
        comments_number_tag = comments_tag.find_previous('faceplate-number')
        if comments_number_tag:
            comments = int(comments_number_tag['number'])
        else:
            comments = -1 
    else:
        comments = -1  
    #comments = comments_tag.find_previous('faceplate-number')['number']
    subreddit = name_tag["href"]
    # Print both date, title, votes, and comments
    #print(f"Date: {date_value}, Title: {title}, Votes = {votes}, Comments = {comments}, Subreddit= {subreddit}")
    final_relevance_date_time_vote_comment_dict.append({
        "Title": title,
        "Subreddit": subreddit,
        "Date": date_value,
        "Votes": int(votes),
        "Comments": int(comments),  
    })

combined_list = []
combined_list.extend(final_top_date_time_vote_comment_dict)
combined_list.extend(final_most_coments_date_time_vote_comment_dict)
combined_list.extend(final_relevance_date_time_vote_comment_dict)

with open('data/raw/post_data_from_all_time_top_relevance_most-comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = combined_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in combined_list:
        writer.writerow(row)