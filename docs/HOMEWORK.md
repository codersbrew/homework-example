
# Ad-Juster Homework

  

## Description

  

A client wants you to retrieve data from a RESTful API and aggregate it for them. The HTTP API has two endpoints to gather data from. The relationship between the two types of data are that of a parent and child relationship, Campaign is the parent and the Creative is the child. The Creatives contain metric data that can be used to describe the overall performance of the parent Campaign item.

  

### API Endpoints


http://homework.ad-juster.com/api/campaigns GET 

http://homework.ad-juster.com/api/creatives GET

  

### Problem

 Write a HTTP Client, in language of choice, that pulls the client’s data from the API. The client wants the data presented in the following manner in a csv file.

  
campaign_id

 campaign_name

campaign_start

campaign_end

creative_name

impressions

clicks

  

Impressions and Clicks should be aggregated for the specific associated Campaign

* Extra Credit: Store the data in a database of choice. 


Please email a compressed copy of your source code to homework@ad-juster.com with the subject: HOMEWORK CODE Lastname_FirstName

  

Any questions? email homework@ad-juster.com
