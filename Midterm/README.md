# Midterm Exam - Spring 2017
# Question 1
- **Question 1 - Analysis 1**

Analysis 1: Analysis on sent mail by Enron employees

For this analysis, we get the content from the Sent mail folder files using email parser. Used Freq. Distance to get the top email senders for Enron. 
The top email senders in descending order are : kay mann, vince kaminski, chris germany, eric bass, kate symes, drew fossum, sally beck, susan scott, phillip love and benjamin rogers. 
Created a csv file to view the range of mails sent.

![ScreenShot](https://github.com/vegashetty/midterm/blob/master/Question%201/Analysis_1/Enron.png?raw=true)

Above graph shows us very few outliers. Thereby bringing us to the conclusion that very few employees have sent a large amount of emails above 1000. The content of the top mail senders can be further investigated.

- **Question 1 - Analysis 2**

Analysis 2 : Content analysis based on the top email sender Mann,K from Analysis 1

Collected content from sent mail folder and performed data cleaning
Found frequency for the words used in sent mail

Prove Zipfs Law

![ScreenShot](https://github.com/vegashetty/midterm/blob/master/Question%201/Analysis_2/ZipfsLaw.png?raw=true)


Based on the content for Mann,K emails, we have proven the Zipf's Law.

- **Question 1 - Analysis 3**

Analysis 3 - Analysis of communications for Chairman Kenneth Lay

Collect data for the sent and received mails of Kenneth Lay
Further found the top recipients and senders of mails to/from Chairman.

Chairman Kenneth Lay has sent the most emails to :
lizard_ar,
jeffrey garten,
katherine brown,
expense report,
sally keepers.

Chairman Kenneth Lay has received the most emails from :
svarga@kudlow.com,
announcements.enron@enron.com,
dbrock@howard.edu,
mschopper@houston.org,
jharwood@mindspring.com.

Conclusion
The top mail receipents/Senders for Kenneth Lay can be further used for investigation into the Enron scandal.

# Question 2

- **Question 2 - Analysis 1**

Analysis 1 : Found the most discussed topics in 2016

Dataset used : Archive API NYT

Based on the data collected for the year 2016, following were the analysis:
There were 340303 keywords for the year 2016.
The top 10 common keywords were: 
'Presidential Election of 2016', 'Trump, Donald J', 'Clinton, Hillary Rodham', 'Books and Literature', 'Movies', 'New York City', 'Television', 'United States Politics and Government', 'Music', 'Republican Party'.

Following is the graph depicting the occurrence of keyword:

![ScreenShot](https://github.com/vegashetty/midterm/blob/master/Question%202/Analysis_1/ques2analysis1.png?raw=true)

Based on the above analysis, we can conclude that the most discussed topic for 2016 was Presidential Election of 2016 followed by Donald Trump Jr and Hillary Clinton.

- **Question 2 - Analysis 2**

Analysis 2 : Distribution of news coverage from July - Nov 2016 based on section names

Dataset used : Article search API NYT

For every month, collected the sorted list of section names and the number of times they appear in the articles.

Based on the data collected for the months July- Dec 2016, following were the analysis:

![ScreenShot](https://github.com/vegashetty/midterm/blob/master/Question%202/Analysis_2/ques2analysis2_barchart.png?raw=true)


Based on the attached Excel bar chart, we can see that the distribution for news coverage from July - Nov 2016 based on section names covers more percent of Sports, World and U.S. news.


- **Question 2 - Analysis 3**

Analysis 3: Analysis on positive and negative headlines for New York Times

Number of positive and negative headlines based on the positive and negative words list downloaded from the reseach papers "Mining and Summarizing Customer Reviews" by Minqing Hu and Bing Liu and "Opinion Observer: Analyzing and Comparing Opinions on the Web." by Bing Liu, Minqing Hu and Junsheng Cheng.

Dataset used : Article search API NYT

Collected all the headlines between the month July- November 2016 to get the sentiment analysis around that period.
There were 7650 headlines for the months July - Nov 2016.
While comparing the headlines with the positive and negative word list attached, we can conclude that for the headlines between July - November 2016 , there were 330 positive headlines and 596 negative headlines. Thereby giving an overall negative sentiment on the total headlines.
