# About My Project

Student Name:  Jack Kester
Student Email:  jwkester@syr.edu

### What it does
In this project, I scrape the UFC website for the top 15 fighters in each weight class, save them to individual dataframes with characteristics for each fighter, and load them into a streamlit to explore each weight class and understand the common characteristics that make them so great. 

My project goes the url https://www.ufc.com/rankings and scrapes all of the weight classes, and the top 15 fighters in each weight class. From there, it saves all the fighters to a csv depending on their weight class. After that, in code_pt2.py, these csvs are loaded in and set to pandas dataframes. Those dataframes are then cleaned putting the champion at the start of the list and taking away the last fighter so that it is a nice 15. 

Once the data is cleaned, a dataset is pulled in, created through chatgpt, that has each scraped fighter and some characteristics. These characteristics include Age, Height (cm), Reach (cm), Leg Reach (cm), Team, Fighting Style, Training Location, and Country. It will then merge every weight class dataset with the rows in the master chatgpt set that match on the name of the fighter. A new updated dataframe is created and saved to the cache as a csv. Additionally, a three new dataframes are made; one merged with all the scraped fighters, one with all the men, and one with all the men. 

These updated dataframes are then taken into the final file of code, streamlit_code.py. This file runs a streamlit through the Run and Debug Streamlit button and takes the user into their browser, opening a streamlit tab. Displayed in front of them is a dropdown with all of the weight classes scraped. The user can decide on which weight class to explore. Depending on their choice, the dataframe of all of the fighters in the weight class will appear. Below it, are two interactive graphs, a histogram with numerical characteristics, and a barplot with non-numerical. The user can decide what to graph for each one using a dropdown and it will update depending the input. Below everything is an interactive map that displays the world. Highlighted are the countries the fighters in the selected weight class are from and are on a gradient depending on the amount of fighters there are from each country. This will update live depending on the dataframe input of the user.

### How you run my project
First you need to do two commands in the terminal 
- pip install -r requirements.txt
- pip install selenium beatifulsoup4 webdriver-manager
- pip install plotly.express

Next, you want to run the scraping_code.py file
-This will scrape https://www.ufc.com/rankings grabbing the top 15 fighters from each weight class storing them into csv's.

Then you want to run the code_pt2.py file. 
-This file reads in the csv's of the weight classes, cleans them, merges with another dataset that has the characteristics of the fighters.

Lastly, you want to run streamlit_code.py through the run and debug streamlit button
-This will open your browswer and open the final streamlit. In here, you can choose the weight classes you want to explore and the different columns to graph. Additionally, there is a map at the bottom displaying how many fighters in that weight class came out of each country.

### Other things you need to know
The first thing you need to know is that the scraper in scraping_code is not at all the kind of scraper taught in class. I utilized selenium, beautifulsoup4, and webdriver-manager to build my scraper. The UFC website has upped its defense against scrapers and is a pain to scrape, just like the ESPN website. UFC is actually owned by ESPN so that might be why. I tried all of the techniques used in class such as playwright and codegen but nothing was working. Not even Chatgpt or Gemini could figure it out. This is when I went to a coding Discord server asking if anyone had experience web scraping and one guy spoke up. That guy gave me the guidance to build what is in the current file. Together, we prompt engineered chatgpt to give us a scraper for a website like the UFC rankings website and spent an hour or two working through trial and error to get the data. What is in my file is the final product we crafted. I understand that it is not the webscraper you were looking for but I really wanted to scrape for my data and that was how it got done. 

The second thing I really wanted to do was use the OpenAI Generate API to get those characteristic columns. I tried to test it out but was met with many 500 errors. If I remember correctly from class, a 500 error is a server issue and not my fault. From here I had to improvise. Hand typing the data would take too long. Instead I went to Chatgpt itself and gave it this prompt:"create a dataset using these fighters and add their age, height in cm, country, training location, fighting style, team, reach, and leg reach." With this prompt, I gave it a list fighters I had gathered from my scraping. Since the API was not working, I thought it was reasonable for me to through a similar prompt to what I would have used in my API into chatgpt and collect data that way, especially since its all from the same source anyway. At first, I was going to just use a dataset from online but there were none with the characteristics I wanted. Utilizing chatgpt allowed me to get the data I was looking for in the API and display what I wanted to display on my streamlit.

One last thing, my main function in scraping_code.py is only made for the ufc website and can't be interchanged. I didn't know if I needed a test or not but I included what I think it would br in the tests folder.
