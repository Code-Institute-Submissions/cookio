<img src="assets/images/mongocho-card-back.png" alt="logocopy" class="center" />

# Cookio

### Collaborative Recipe Book

Mongocho is a “Just for fun" website created to offer cartoon and illustration enthusiasts a gallery updated weekly with copyright free drawings and graphic gags.

The site is planned and built to showcase some of my work, to have fun and to connect with an audience that will appreciate my kind of humour to hopefully engage in a conversation.

The website is not intended to be an exhaustive portfolio of my work but a creative exercise to show a limited number of drawings and cartoons in the gallery which I am planning to update weekly with new material.

The main feature is a memory game where I show some of my characters in pairs to be matched in the least possible number of moves.

## Table of Contents

1. [**User Experience**](#user-experience)
2. [**UX**](#ux)
3. [**Using the website**](#using-the-website)
4. [**The Gallery**](#the-gallery)
5. [**The Memory Game**](#the-memory-game)
6. [**User Stories**](#user-stories)
7. [**As User**](#as-user)
8. [**As a Cartoonist**](#as-a-cartoonist)
9. [**Existing Features**](#existing-features)
10. [**Using the Contact Us form**](#using-the-contact-us-form)
11. [**Technologies Used**](#technologies-used)
12. [**Testing**](#testing)
13. [**Bugs**](#bugs)
14. [**Deployment**](#deployment)
15. [**Wireframese**](#wireframes)
16. [**Credits**](#credits)
17. [**Acknowledgements**](#acknowledgements)

## User Experience

### UX

This website has been designed as a multi-page front end website with parallax on scrolling.

The website shows at first the logo and a tagline, nav bar and sample of the drawings on parallax.
There is a section with a short introduction to what MOngocho is about and a footer with subscribe section and social media links.

There are several hover effects in the footer, over the titles and in social media icons.

The Contact Us section is a form with "required fields" and drop down menu to select style of painting desired.

### Using the website

- The visitor will see the Landing Page with the logo on top and a tagline.
- A NavBar provides an easy way to select the desired section and sticks to the top when scrolling down.
- A first cartoon appears and gives a 3D effect (Parallax) when scrolling) giving way to text explaining who I am.
- A new cartoon appears and, again, a text section appears with an explanation of how I create my drawings.
- A third cartoon is revealed before reaching the footer.

### The Gallery

- The next page is a gallery with a selection of cartoons and drawings. This gallery displays in a modal with easy navigation in carrousel or in group with easy browsing.

### The Memory Game

- The memory game is a 4 x 4 card grid with back logo and 8 pair of cartoons (4 Female and 4 Male).
- I got inspiration and guidance from Marina Ferreira (Credited) but I have modified the game with my own design with new styling, number of cards and functionality.
- I added a Restart Button and a counter to make it more engaging and fun to play.

## User Stories

### As User

- As user, I want to see cartoons.
- As user, I want to be able to look at the cartoons in detail.
- As user, I want to be able to contact Mongocho to ask for a particular design.
- As user, I want to play the memory game and get familiarised with the characters created by Mongocho.

### As a cartoonist

- As a cartoonist I want to show a selection of the cartoons that I create.
- As a cartoonist I want to be able to be contacted through the page.
- As a cartoonist I want to promote my work.
- As a cartoonist I want to connect with cartoons enthusiasts.

## Existing Features

- The navigation bar collapses with a burger button on smaller screens.
- The gallery displayed in a modal. This has been achieved using Fancybox.
- Memory game with functionality coded on JavaScript.
- Contact Us form.
- The Footer, with contact information and social media links.

## Using the Contact Us form

Go to "Contact Us"

- The contact fields are required and sending emssages without completing isn't allowed, showing a message to fill the form before sending.

## Features Left to Implement

- A future release will include add a shopping cart for customers to select, check out, pay and purchase cartoons.

## Technologies Used

### The project was build with:

- HTML5, to structure the website.
- CSS, to style the website.
- [jQuery](https://jquery.com/), for gallery.
- [Visual Studio Code](https://code.visualstudio.com/), for the development environment.
- [Github](https://github.com/), as the version control technology and GitHub Pages as the webserver technology to publish the website.
- [Bootstrap](https://getbootstrap.com/), to utilize responsive elements.
- [Font Awesome](https://fontawesome.com/), to utilize icons.
- [Google Fonts](https://fonts.google.com/), to utilize different fonts.

## Testing

- Manual testing was performed throughout the creation of this site.
- No testing has been automated.
- We have asked 8 people to act as potential users of the website.
- The site has been tested in Laptops and desktops in in Chrome, Safari, Firefox and IE to ensure it displays as desired.
- The site has been tested in iOS and Android phones in Safari, Chrome and Firefox.
- Throughout the build of this site, I used Chrome Develpers Tool.

- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)

In all screens tested the website looks exactly in the desired way and responded in expected way and achieving the goals of the site.
The memory game functions exactly as desired, with 3D effect and rotation appearance.

## Bugs

There was a bug when displaying the memory card in small screen. The cards animation did not work and the functionality of the game was not responding.

The problem is now fixed.
The css transform property is not fully supported by IOS browsers, to fully support it, I needed to add some css browser specific prefix to make it work on iOS (-webkit-transform:) . What I did was to copy the css file into https://autoprefixer.github.io/ to help format it and add the necessary css prefixes so it can be supported by most browsers.
Now is working very well.

There was a bug on displaying the parallax background images in landscape, as they were rendered out of proportion.
The parallax effect on mobile is not fully supported. The media query uses 600px to stop the parallax effect but when switched to landscape, the width becomes larger and the parallax effect tried to render in the mobile browser so I increased the width of the media query to 1200px to cover most phones and tabs. The parallax effects works fine on android even at the 600px.

## Deployment

I used Visual Studio Code to write all the code. My website is deployed on Github Pages - To visit, click [Here](https://fabibrachetta.github.io/mongocho/).

In order to do this is followed the below steps:

- Create a directory on the local file system.
- In GitHub “Repositories” I’ve clicked on the green “new” button and created a repository with the name of Mongocho.
- Select Clone "Clone or download" on Github, copy the link.
- In VSCode , select File -> Add Folder to Workspace -> Select the newly created directory.
- Select Terminal Window.
- In the terminal type:
git remote add origin https://github.com/FabiBrachetta/mongocho.git
git branch -M master
git push -u origin master
- In VSCode, I’ve created the site, committed and pushed onto repository.
- On GitHub, I’ve clicked on Mongocho repository.
- Under Mongocho repository name, click “Settings”.
- Under "GitHub Pages", use the Source drop-down menu and select Master Branch for live url.

## Wireframes

Wireframes created in Balsamiq:

You can find the wireframes [here](https://github.com/FabiBrachetta/mongocho/blob/master/wireframes/mongocho-mockup.png).

# Credits

## Content

- The full website has been completely created by me.
- The gallery was created using Fancybox from [Fancyapps](https://fancyapps.com/fancybox/3/).
- The memory game has been created inspired by the tutorial by Marina Ferreira - Software Engineer | Code Sketch Channel Tutorials [here](https://marina-ferreira.github.io/tutorials/js/memory-game/).
- I used modules of Bootstrap and styled to my taste.

## Media

- The images and logos used are all my creation. I own all rights to use and publish the images.
- I authorise free use of any image for non commercial use (credits would be appreciated).

## Acknowledgements

- Special thanks to my mentor [@guidocecilio_mentor](https://github.com/guidocecilio) for his guidance and support.