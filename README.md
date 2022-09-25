# Project 1: What puts the "Hot" in Billboard Hot 100 Hits?

### Project Overview

This project seeks to analyze the trend in audio features in songs ranked #1 on the Billboard Hot 100 Chart for the last 20 years. The Billboard Hot 100 API, Spotify API, and iTunes API were used to consolidate a list of the #1 Hit Songs for each week of the last 20 years, and then to collect audio feature, genre, and explicitness data. Matplotlib and Seaborn were used to visualize the data and observe patterns.


### Some Conclusions from this analysis:
-  Looking at opur genre stacked chart, it is clear that Pop dominates the number one song spot over the last 20 years. In the early 2000's, R&B/Soul is a pretty big contributor, but falls off as we get closer to 2019. Hip-Hop/Rap becomes a more prominent genre as we get closer to modern day, and we see country and alternative become featured as well. 
- Looking at the bar charts for the breakdown of each audio feature, we can see that number one songs tend to have higher energy,danceability and tempo.
- We thought explicit songs would increase over the years, but it seemed pretty comparable when we borke it down, with exception sin 2002 and 2018. This, however, would probably show more explicitness if we had data for all songs on Top 100 charts.
- Most songs were written in key of G, C, C#/D which was surprising to see. 

### Limitations:
- We were only able to look at the number 1 song each week overt the last 20 years due to how many requests we could make to the billboard api. Would've been better to analyze trends with more data, perhaps if we could've looked at all the hits on the Top 100 Chart for each year.
- For the year 2000, we weren't able to get a good amount of the Song ID data that we needed to get audio features from the Spotify API. This led to us having almost 3 months worth of data missing and so our analysis was a little lacking that year. 
- Originally wanted to be able to look at trends according to geographical location, age, race, income level, etc but user data was not able to be accessed via the Spotify API. 

### Meet the Team
- Julie Demusz: Data Research, Visualizations 
- Julia O'Brien: Data Collection, Data Cleanup 
- Nathaniel Ross: Visualizations, Project Presentation 

### Acknowledgments / Inspiration
https://towardsdatascience.com/billboard-hot-100-analytics-using-data-to-understand-the-shift-in-popular-music-in-the-last-60-ac3919d39b49
