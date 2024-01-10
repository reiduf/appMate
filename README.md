# AppMate

## Overview
AppMate is a site meant to help organize your job search process. Instead of having massive spreadsheets tracking hundreds of applications, AppMate creates an environement where all that information can be stored and organized in a way that makes the job search process just a bit more bareable. It is designed to track and update you both on your job applications and proffessional connections. 


#### Technologies Used
> Django web framework
>
> Neon remote database
>
> Tailwind CSS framework and library


## App Walkthrough
Below are screenshots of AppMate, walking through some of the features. 


![Imgur](https://i.imgur.com/pF8x30a.png)


![Imgur](https://i.imgur.com/Vpa2pg2.png)
Once using Google's OAuth to login the user will be shown the homepage with the same feed but updated nav bar options. They can create a post, view their profile, find other user profiles, or logout. 

![Imgur](https://i.imgur.com/UbmWE2t.png)
![Imgur](https://i.imgur.com/Q5YBdHG.png)
When SEE DETAILS on a post is clicked a page showing the user, description, like/unlike buttons, comments, a form to add new comments and a delete button that appears when the post being viewed was created by the viewing user. A user can also view the poster's profile by clicking on their name at the top. 

![Imgur](https://i.imgur.com/foy82k8.png)
This shows a user's profile page which consists of their username and avatar at the top and a collection of pictures of their posts that once being clicked will bring you to the post's show page. 

![Imgur](https://i.imgur.com/Rairq9N.png)
This is the page a user is shown to create a post. It is pretty bare right now because the only data we need the user to enter is the image description, which will then be used to generate an image. 

![Imgur](https://i.imgur.com/IYNdpky.png)
This is the search page where a user can search for another user and any matching results will be shown. When clicked, the result will take the user to the searched profile page. 


## Getting Started
To view the site go here. 

Some notes:
- Generating images usually takes a few seconds so be patient when creating a post. 
- Images will be deleted after 2 hours (Open AI policy, trying to find work around).
- Must have a Google account (Gmail) to login.


## What's next?
Ontop of the future plans touched on in the overview, some features I would love to add are:
- Following or subscribing capabilities
- Feed algorithm based off followers and interest
- Post search based off hashtag type system
- Capability to share posts to other social media sites
- User image uploading functionality (obviously)
- and more...



