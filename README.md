<img src="/static/images/cookio-logo.jpg" alt="logo-copy" class="center" />

# Cookio

### Collaborative Recipe Book

Cookio is a collaborative Recipe book with the possibility to Read-Only as a visitor or to create an account to be able to add, edit and delete recipes in a dynamic and interactive way.
The Admin will have additional tight to add, delete categories.

## Table of Contents

1. [**User Experience**](#user-experience)
2. [**UX**](#ux)
3. [**Using the website**](#using-the-website)
4. [**The Recipes**](#the-recipes)
5. [**The Memory Game**](#the-memory-game)
6. [**User Stories**](#user-stories)
7. [**As User**](#as-user)
8. [**As an Admin**](#as-an-admin)
9. [**Existing Features**](#existing-features)
10. [**Login**](#login)
10. [**register**](#register)
11. [**Technologies Used**](#technologies-used)
12. [**Testing**](#testing)
13. [**Bugs**](#bugs)
14. [**Deployment**](#deployment)
15. [**Wireframese**](#wireframes)
16. [**Credits**](#credits)
17. [**Acknowledgements**](#acknowledgements)

## User Experience

### UX

This website has been designed as a multi-page front end website with login possibility.

The website shows the logo in the nav bar and links to the different sections of the site.

The recipes are displayed in an accordion with collapsible field to show the preparation of them.

There is a User Profile to enter personal details and the possibility of edit the information.

While lohgging in, as an user it will show "Add Recipe" to create, delete and update recipes.


### Using the website

- The visitor will see the Landing Page with the logo on top and a tagline.
- A NavBar provides an easy way to select the desired section and sticks to the top when scrolling down.
- A first cartoon appears and gives a 3D effect (Parallax) when scrolling) giving way to text explaining who I am.
- A new cartoon appears and, again, a text section appears with an explanation of how I create my drawings.
- A third cartoon is revealed before reaching the footer.

## User Stories

### As User

- As a user I want to see recipes from other users.
- As a user, I want to have one place where to store all my recipes.
- As a user I want to be able to edit my own recipes.
- As a user I want to be able to remove my own recipes that I don't want to see and share anymore.
- As a user i want to easily see when a recipe is vegetarian.
- As a user I want to be able to search the recipes by key words.
- As a user who wants to select a specific type of meal (category) 
- As a non registered user I should not be able to add recipes.
- As a user I want to be able to contact Cookio.

### As an Admin

- As an Admin, I want to be able to Add categories in addition to other features.

### login

- The login page is an form where users can enter their username and password.

- **Flash message** If the username is not in the database or if the password has been incorrectly entered a Flash error message is displayed.

- New users who want to register can click on the link "Register here" to get redirected to the page.

### register

- New users can use the form in this page to start using Cookio.

- **Flash message** If the username entered is already in use a message will be displayed.

- To protect passwords in MongoDB, they have been hashed using the bcrypt function.

- Users already registered can directly click on "Login here" to enter credentials.

## Existing Features

- The navigation bar collapses with a burger button on smaller screens.
- Accordion with the recipes in an easy to use setup.
- Profile Section easy to update. In a future release we will enable use of the customer data (statistics, chat, etc)
- The Footer, with contact information and social media links.


## Features Left to Implement

- A future release will include upvoting to rate recipes and create a ranking.

## Technologies Used

#### Database:

- **[MongoDB](<[https://www.mongodb.com/](https://www.mongodb.com/)>)**

#### Mock-up tool:

- **[Pencil:](https://pencil.evolus.vn/'https://pencil.evolus.vn/)** I have used Pencil to create the mock-ups for the website.


#### Languages:

- **HTML5:** To create the structure of the website.
- **CSS3:** To add styles to the HTML.
- **[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** To add interactivity to the website. 
- **[Python:](<[https://www.python.org/](https://www.python.org/)>)** The main logic of the website has been created using Python.

- **[Flask:](<[https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/)>)** I have used the web Flask framework.

- **[Jinja:](<[http://jinja.pocoo.org/](http://jinja.pocoo.org/)>)** I have used Jinja templating engine in order to use template inheritance, add **for loops** and **if statements** in the html files and in order to pass information between back and frontend.

### Validation

- **HTML:** I have used https://validator.w3.org/ in order to validate the HTML code.

- **CSS:** I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

- **JavaScript:** I have used https://jshint.com/ in order to check the JavaScript code.

### testing

### Travis
#### How to set up Travis
- Went to Travis-ci.com and Sign up with GitHub.
- Accept the Authorization of Travis CI. You’ll be redirected to GitHub. F
- Click on profile picture in the top right of Travis Dashboard, click Settings and then the green Activate button, and select the repositories to use with Travis CI.

#### unittest

I have used unittest in order to test the **CRUD** operations.

My mentor Guido kinldy assisted setting up unittest for the project 

The tests are saved in the file **test_app.py** and this file is saved in the folder **tests**.
In order to run the tests I typed the following on the terminal:

`python -m tests.test_app`

### Results
- pymongo.errors.OperationFailure: user is not allowed to do action 
- [dropDatabase] on [test_recipe_manager.], 
- full error: {'ok': 0, 'errmsg': 'user is not allowed to do action 
- [dropDatabase] on [test_recipe_manager.]', 'code': 8000, 
- 'codeName': 'AtlasError'}
- self.mongo_client.drop_database('test_recipe_manager')

#### Dev Tools

I have used development tools in Google Chrome to inspect and try wothout compromising the code. I have also asked relatives and friends to check how the website would look on different devices (portrait and landscape mode). In addition to that testing I have also asked people to visit the website to ensure it works as wanted and if looks OK on their browsers and devices.

## Bugs

We have not found bugs to report

## Deployment

I used GitPod  to write all the code. My website is deployed on Heroku - To visit, click [Here](http://cookio.herokuapp.com/).

In order to do this is followed the below steps:

- Create a directory on the local file system.
- In GitHub “Repositories” I’ve clicked on the green “new” button and created a repository with the name of COOKIO.
- In GitHub “Repositories” I’ve clicked on the green GitPod button and used to write the code.
- Select Terminal Window.
- On GitHub, I’ve commmitted and changes are autimatically visible on Heroku hosted page.

## Live Page - Herokuapp

- Registered account in Herokuapp and logged with credentials.
- Click New on the top right corner and select “Create new app”.
- Gave the app a name (This will be included in the public URL for application) and click Create app.
- This step  takes to the dashboard of the app. Open Deploy tab and scroll to the “Deployment method” section.
- Selected GitHub as the method.
- Showed a “Connect to GitHub” option where I provided the GitHub repository.  Heroku asked permission to access my GitHub account.
- Here, I searched for the GitHub repository and click connect
- Once it found and connected to the GitHub repository, the Deployment section showed where to select - Automatic Deployment (as soon as the changes are pushed to GitHub, Heroku will pick them up and deploy) or Manual Deployment.
- Click Enable Automatic Deploys. 
- Selected Python from the available options and saved changes. 
- DONE. The site is hosted by Herokuapp and accessible.

## Wireframes

Wireframes created in Balsamiq:

You can find the wireframes [here](https://github.com/FabiBrachetta/mongocho/blob/master/wireframes/mongocho-mockup.png).

# Credits

## Content

- This website has been completely created by me and inspired by the miniproject of Code Institute.

## Acknowledgements

- A very special thanks to my mentor [@guidocecilio_mentor](https://github.com/guidocecilio) for his guidance and support.