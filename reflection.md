# Reflection

Student Name:  Jack Kester
Student Email:  jwkester@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Ultimately, this project really chalanged me. I didn't want to showcase much data but rather utilize a lot of the tools you offered through this class. Doing this however, I ran into a lot of technical difficulties. Starting off with my scraper, playwright failed me, and as you learn in the about-project folder, I had to resort to other methods of scraping not taught in this class. I did however, learn the far superior and much more efficient selenium, beautifulsoup4, and webdriver mangager. These tools allowed me to scrape the tricky website the UFC website is and actually pull data from it. Going forward, I can use what I learned in this project to scrape other tricky websites such as ESPN. The whole idea of the scraper pretending to be human through the scroll function is what saved me and will help me in the future. The next big challenge I ran into was using the Open AI API. I kept running into 500 errors and had to resort chatgpt to manipulate my data. I would've liked a little more experience with the generate API and this project was the perfect opportunity. I am bummed that I couldn't use but on a time crunch I had to improvise. The code I tried to get working is actually in the code_pt2.py file but its commented out. When it came to the streamlit, I actually had a lot of fun making that. Although there isn't much, I'm proud of the different variations of plots and graphs a user can output. I'm happy with the histogram and barplots the user can make. The choropleth wasn't the hardest thing but everytime I make one of those things I need a refresher. I feel like I could have added more to the final streamlit but my goal was for the user to change the inputs of data and variables. I took heavy inspiriation from the last assignment but obviously changed a few things around such as having a different interactive map, and have interchangeable graphs. I really liked the 2 column system of showing graphs so I implemented that. In the end, I would say I was successful in displaying what I wanted to display from https://www.ufc.com/rankings but there definitely some things I wanted to do better. 

One last thing, my main function in scraping_code.py is only made for the ufc website and can't be interchanged. I didn't know if I needed a test or not but I included what I think it would br in the tests folder.


