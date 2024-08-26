# Milestone Project 3 - Concert Connect

![Responsive Website Mockup](./static/images/documentation/responsive_image.png)

## Live Site

The live site for this project can be found at this link: <https://concert-connect-802cf2f5a70f.herokuapp.com>

## GitHub Repository

The GitHub Repository for this project can be found at this link: <https://github.com/99bjacko/milestone-project-3>

## Objective

In this project, I intend to create an engaging and responsive website. The goal of this website is to illustrate my passion for going to concerts, and to allow other users to do the same thing by sharing their experiences. The main objective is to demonstrate my capabilities using HTML, CSS, Python, Flask and MongoDB, creating an enjoyable experience for users of the website.

The target audience for this website is people who are similar to myself - people who love going to concerts and watching live music.

## UX

### User Stories

- As a visitor to the website, I want the navigation between pages and/or areas to be easy and intuitive, not having to rely on browser buttons.
- As a visitor to the website, I want the website to be responsive on a number of different devices.
- As a first time visitor to the website, I would like to easily view other users' posts.
- As a first time visitor to the website, I would like to be able to view all posts in a specific category.
- As a first time visitor to the website, I would like the home page to be visually appealing.
- As a first time visitor to the website, I would like to easily register for my own account, allowing me to contribute to the website.
- As a first time visitor to the website, I would like to add my own posts, allowing me to share my experience with other like-minded individuals.
- As a returning visitor to the website, I would like to be able to log in easily.
- As a returning visitor to the website, I would like to be able to log out easily.
- As a returning visitor to the website, I would like to be able to edit my existing posts.
- As a returning visitor to the website, I would like to be able to delete my existing posts.
- As a returning visitor to the website, I would like to be able to view the most recent posts, allowing me to catch up on other people's activity.
- As an administrator, I would like to be able to manage existing categories, including updating and deleting.
- As an administrator, I would like to be able to add new categories, which will become available to users adding new posts.
- As an administrator, I would like to be able to edit or delete any post on the website, reducing the risk of bad actors.

### Opportunities

Derived from user stories
| Opportunities | Importance | Viability / Feasibility |
| ------------- | ---------- | ----------------------- |
|Easy and intuitive navigation between pages and/or areas | 5 | 5 |
|Responsive and visually appealing site suitable for mobile, tablet, and desktop screen sizes | 5 | 5 |
|Allow any user, whether they are logged in or not, to view other users' posts | 5 | 5 |
|Allow any user, whether they are logged in or not, to view posts in a specific category | 4 | 4 |
|Allow users to view the most recent posts, useful for those returning to the website | 4 | 4 |
|Allow new users to easily register for their own account | 5 | 5 |
|Allow existing users to easily log in to their account | 5 | 5 |
|Allow logged in users to easily log out of their account | 5 | 5 |
|Allow users, when logged in, to add their own posts | 5 | 5 |
|Allow logged in users to edit their existing posts | 5 | 5 |
|Allow logged in users to delete their existing posts | 5 | 5 |
|Allow administrator users to manage existing categories | 5 | 5 |
|Allow administrator users to add new categories | 5 | 5 |
|Allow administrator users to edit and delete posts created by other users | 5 | 5 |

### Initial Concept

The concept for this website was very much functionality first, focusing on a good, functional user experience, whilst keeping the design visually appealing but simplistic, maintaining appropriate contrast throughout the website. The design should be kept distraction-free, focusing on the content created by the users, rather than the website itself. 

#### Wireframes

For initially designing the project, I utilised Balsamiq to produce wireframes. This step allows for planning layouts and page structures, allowing to focus more on the website looking like the designs, instead of trying to simultaneously code and design.

- [Home Page Wireframe](./static/images/documentation/home_page_wireframe.png)
- [Home Page Logged In Wireframe](./static/images/documentation/home_page_logged_in_wireframe.png)
- [Registration Page Wireframe](./static/images/documentation/registration_page_wireframe.png)
- [Login Page Wireframe](./static/images/documentation/login_page_wireframe.png)
- [All Posts Page Wireframe](./static/images/documentation/all_posts_page_wireframe.png)
- [Post Page Wireframe](./static/images/documentation/post_page_wireframe.png)
- [Add Post Page Wireframe](./static/images/documentation/add_post_page_wireframe.png)
- [Categories Page Wireframe](./static/images/documentation/categories_page_wireframe.png)
- [Categories Page Administrator View Wireframe](./static/images/documentation/categories_page_administrator_wireframe.png)
- [Add Category Page Wireframe](./static/images/documentation/add_category_page_wireframe.png)

#### Colour Scheme

The colour scheme for this project involved a lot of trial and error. I was interested in potentially using a background image for the home page, but I did not have a clear vision on what it would have been, so I decided against it. I experimented with different colour combinations, using Coolors for inspiration.

The colours used throughout this website are:
- Navigation Bar: Red `#CC2936`
- Cards: Grey `#333138`
- Background: Black `#000103`
- Buttons: Styled using Bootstrap's primary (blue), secondary (grey), info (turquoise), and danger (red) classes
- Text: White `#fff`

#### Typography

The typography for this project was picked using Google Fonts.
- Main Brand / Logo: Poetsen One
- Other Text: IBM Plex Sans

## Features

### Current Features

#### Navigation bar
    
- The design of the navigation bar is kept consistent across all pages of the website, following convention with the logo / brand text on the left hand side and navigation links on the right.
- The Navbar is the main method for navigation around the different pages of the website. The links change depending on whether a user is logged in or not.
- When logged out, the navigation bar includes links to Home, Categories, All Posts, Log In, and Register.
- When logged in , the navigation bar includes links to Home, Categories, Add Post, All Posts, and Log Out.
- The navigation bar is fully responsive with smaller screens having a collapsed menu with a navigation toggler button and larger screens having a fully expanded navigation bar.
- The navigation bar satisfies the first user story as it is easy and intuitive.
- The navigation bar satisfies the second user story as it is responsive on a number of different devices and it is visually appealing.

##### Logged Out

![Navbar Logged Out](./static/images/documentation/navbar_logged_out_screenshot.png)

##### Logged In
    
![Navbar Logged In](./static/images/documentation/navbar_logged_in_screenshot.png)

##### Mobile

![Navbar Mobile Screenshot](./static/images/documentation/navbar_collapsible_screenshot.png)

#### Logo

- The Navbar also contains the main brand logo, which is also a form of navigation, acting as a home button.

![Logo](./static/images/documentation/logo_screenshot.png)

#### Home Page

##### Logged Out

![Home Page Logged Out](./static/images/documentation/home_page_logged_out_screenshot.png)

##### Logged In

![Home Page Logged In](./static/images/documentation/home_page_logged_in_screenshot.png)

##### Administrator View

![Home Page Logged In Admin](./static/images/documentation/home_page_logged_in_admin_screenshot.png)

- The Home Page features two main sections:
    - The first section is a card displaying the main brand image along with a comment, introducing users to the concept of the website.
        - If the user is logged in, a button for adding a post will be displayed.
    - The second section displays the most recent posts added by users, view post buttons are displayed for each post.
        - If the user is logged in and one of the recent posts was created by that specific user, buttons for editing and deleting that post will be displayed.
        - If the user logged in is an admin, buttons for editing and deleting the posts will be displayed.

- The Home Page targets the third, fifth, and twelfth user stories.

#### Categories Page

#### Logged Out / Logged in as a regular user

![Categories Page](./static/images/documentation/categories_page_screenshot.png)

##### Administrator View

![Categories Page Admin](./static/images/documentation/categories_page_logged_in_admin_screenshot.png)

- The Categories Page features categories separated onto individual cards.
- Through this page, users can view posts under specific categories.
- If an administrator is logged in, buttons for editing and deleting the categories will be displayed.
- The Categories Page targets the fourth user story.

#### View Posts By Category Page

![View Posts By Category Page](./static/images/documentation/view_posts_by_category_page_screenshot.png)

##### Page when there are no posts found with that category name

![View Posts By Category Page When No Posts Are Found](./static/images/documentation/view_posts_by_category_page_no_posts_found_screenshot.png)

- The View Posts By Category Page displays all of the posts in a specific category.
- The category name is displayed as a heading.
- If a user is logged in and one of the displayed posts was created by that specific user, buttons for editing and deleting that post will be displayed.
- If the user logged in is an admin, buttons for editing and deleting the posts will be displayed.
- If no posts are found, a message is displayed.
- This page targets the third and fourth user stories.

#### Add Category Page

![Add Category Page](./static/images/documentation/add_category_page_screenshot.png)

- The Add Category Page is accessed through the Categories Page via a button, which is hidden to non-administrators.
- The Add Category Page is only accessible by an administrator.
- The page features a form with an input field and two buttons:
    - The input field is for the category name.
    - The add category button submits the category to the database.
    - The cancel button redirects the user back to the categories page.
- This page targets the fourteenth user story.

#### Edit Category Page

![Edit Category Page](./static/images/documentation/edit_category_page_screenshot.png)

- The Edit Category Page is accessed through the Categories Page via a button, which is hidden to non-administrators.
- The Edit Category Page is only accessible by an administrator.
- The page features a form with an input field and two buttons:
    - The input field is for the category name and is filled by default with the current category name.
    - The edit category button updates the category in the database.
    - The cancel button redirects the user back to the categories page.
- This page targets the thirteenth user story.

#### All Posts Page

##### Logged Out

![All Posts Page Logged Out](./static/images/documentation/all_posts_page_logged_out_screenshot.png)

##### Logged In

![All Posts Page Logged In](./static/images/documentation/all_posts_page_logged_in_screenshot.png)

##### Administrator View

![All Posts Page Logged In Admin](./static/images/documentation/all_posts_page_logged_in_admin_screenshot.png)

- The All Posts Page can be accessed by all users
- All posts are displayed on individual cards, with view post buttons which link to the individual posts.
- If the user is logged in, a button for adding a post will be displayed underneath the heading.
- If the user is logged in and one of the posts was created by that specific user, buttons for editing and deleting that post will be displayed.
- If the user logged in is an admin, buttons for editing and deleting the posts will be displayed.
- This page targets the third user story

#### View Post Page

##### Logged In as the same user that created the post or logged in as admin

![View Post Page Logged In](./static/images/documentation/display_post_page_logged_in_screenshot.png)

##### Logged Out or logged in as a user that didn't create the post

![View Post Page Logged Out](./static/images/documentation/display_post_page_logged_out_screenshot.png)

- The View Post Page can be accessed by all users via the "View Post" button displayed on the post cards.
- The Page displays all the necessary information related to the post:
    - The page heading is the post title.
    - The image is displayed beneath the heading.
    - The rest of the details are displayed on a card beneath the image.
- If the user is logged in and created that specific post, or if the user logged in is an administrator, buttons for editing and deleting the post will be displayed.
- This page targets the third user story.

#### Registration Page

![Registration Page](./static/images/documentation/registration_page_screenshot.png)

- The registration page is accessed through the navigation bar, the link only displays to users not logged in.
- The page consists of a form with fields for username and password and a submit button to submit the data to the database.
- The form checks if the username does not already exist and also validates the username and password to ensure requirements are met.
- After registering successfully, the password is saved as a hashed password in the database.
- After registering successfully, the user is automatically logged in.
- After registering successfully, the user is redirected to the all posts page and a flash message is displayed, welcoming the user.
- This page targets the sixth user story.

#### Log In Page

![Log In Page](./static/images/documentation/login_page_screenshot.png)

- The log in page is accessed through the navigation bar, the link only displays to users not logged in.
- The page consists of a form with fields for username and password and a submit button.
- Upon clicking the button, the username and password are checked against the data stored in the database.
- After logging in successfully, the user is redirected to the home page and a flash message is displayed, welcoming the user.
- This page targets the eighth user story.

#### Log Out Function

![Log Out Link](./static/images/documentation/logout_link_screenshot.png)

- The log out link is only displayed to logged in users in the navigation bar.
- Upon clicking the link, the user is logged out.
- This function targets the ninth user story.

#### Add Post Page

![Add Post Page](./static/images/documentation/add_post_page_screenshot.png)

- The Add Post page is either accessed through the buttons on the home and all posts pages or through the link in the navigation bar.
    - The buttons and link in the navigation bar are only displayed to logged in users.
- The page consists of a form with fields for all of the relevant data related to a post along with a submit button to submit the data to the database.
- The form also contains a cancel button, which redirects the user to the all posts page.
- This page targets the seventh user story.

#### Edit Post Page

![Edit Post Page](./static/images/documentation/edit_post_page_screenshot.png)

- The Edit Post page is accessed through the buttons displayed on a post card.
    - These buttons are only displayed to the correct users and all administrators
- The page consists of a form with the same fields and buttons as the Add Post page, the form has been filled in by default with the pre-existing data.
- This page targets the tenth user story.

#### Error 404 Page

![Error 404 Page](./static/images/documentation/error_404_page_screenshot.png)

#### Missing Permissions Page

![Missing Permissions Page](./static/images/documentation/missing_permissions_page_screenshot.png)

### Future Features

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used to create the website
- [CSS3](https://en.wikipedia.org/wiki/CSS) was used to style the website
- [JavaScript (through Bootstrap)](https://en.wikipedia.org/wiki/JavaScript) was used for the functionality of the website
- [Python](https://www.python.org/) was used as the back-end programming language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) was used as the Python framework, along with [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating.
- [Bootstrap 5.3.3](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used to aid with responsive design and styling of the website
- [Gitpod](https://gitpod.io/): used to create the site (IDE)
- [Google Fonts](https://fonts.google.com/): used to import the fonts used for this website into the style.css file
- [Coolors](https://coolors.co/): used for picking a colour scheme
- [Google Developer Tools](https://developer.chrome.com/docs/devtools/): used for troubleshooting and testing
- [Git](https://git-scm.com/): used for version control by utilising the Gitpod terminal to commit to Git and push to GitHub
- [GitHub](https://github.com/): used to save and store the files for the project
- [MongoDB](https://www.mongodb.com) was used for non-relational database management with Flask
- [Heroku](https://www.heroku.com/): used for hosting the deployed back-end website
- [Balsamiq](https://balsamiq.com/): used to create the wireframes during the design process
- [Am I Responsive?](https://ui.dev/amiresponsive): used to create an image depicting what the website looks like on different devices

## Database Structure

For this project, I used MongoDB, a non-relational database architecture.

My database is called concert_connect.

It contains 3 collections:

### categories

This contains the details of the categories used in the website

| Key | Type | Notes |
| --- | ---- | ----- |
| _id | ObjectId() | Automatically Generated |
| category_name | String | |

### posts

This contains the information about the posts that users add to the website

| Key | Type | Notes |
| --- | ---- | ----- |
| _id | ObjectId() | Automatically Generated |
| category_name | String | Taken from categories collection |
| artist_name | String | |
| venue | String | |
| concert_date | String | |
| favourite_song | String | |
| post_description | String | |
| post_title | String | |
| created_by | String | |
| post_image | String | | 

### users

This contains the information about the users that have signed up to the website

| Key | Type | Notes |
| --- | ---- | ----- |
| _id | ObjectId() | Automatically Generated |
| username | String | |
| password | String | Hashed Password |
| administrator | String | yes for administrator, set to no by default when registering |

## Testing

### Lighthouse Testing

For this project, I tested the performance, accessibility, best practices and SEO of the website using Lighthouse, one of the Chrome Developer Tools.

When initially testing using Lighthouse, the index page had an SEO score of 90 which increased after missing description and keywords were added to the head of the base template.

- [Lighthouse report for index page - desktop](./static/images/documentation/lighthouse_testing_index_desktop.pdf)
- [Lighthouse report for index page - mobile](./static/images/documentation/lighthouse_testing_index_mobile.pdf)
- [Lighthouse report for categories page - desktop](./static/images/documentation/lighthouse_testing_categories_desktop.pdf)
- [Lighthouse report for categories page - mobile](./static/images/documentation/lighthouse_testing_categories_mobile.pdf)
- [Lighthouse report for view posts by category page - desktop](./static/images/documentation/lighthouse_testing_view_posts_by_category_desktop.pdf)
- [Lighthouse report for view posts by category page - mobile](./static/images/documentation/lighthouse_testing_view_posts_by_category_mobile.pdf)
- [Lighthouse report for add category page - desktop](./static/images/documentation/lighthouse_testing_add_category_desktop.pdf)
- [Lighthouse report for add category page - mobile](./static/images/documentation/lighthouse_testing_add_category_mobile.pdf)
- [Lighthouse report for edit category page - desktop](./static/images/documentation/lighthouse_testing_edit_category_desktop.pdf)
- [Lighthouse report for edit category page - mobile](./static/images/documentation/lighthouse_testing_edit_category_mobile.pdf)
- [Lighthouse report for all posts page - desktop](./static/images/documentation/lighthouse_testing_all_posts_desktop.pdf)
- [Lighthouse report for all posts page - mobile](./static/images/documentation/lighthouse_testing_all_posts_mobile.pdf)
- [Lighthouse report for view post page - desktop](./static/images/documentation/lighthouse_testing_view_post_desktop.pdf)
- [Lighthouse report for view post page - mobile](./static/images/documentation/lighthouse_testing_view_post_mobile.pdf)
- [Lighthouse report for registration page - desktop](./static/images/documentation/lighthouse_testing_registration_desktop.pdf)
- [Lighthouse report for registration page - mobile](./static/images/documentation/lighthouse_testing_registration_mobile.pdf)
- [Lighthouse report for log in page - desktop](./static/images/documentation/lighthouse_testing_login_desktop.pdf)
- [Lighthouse report for log in page - mobile](./static/images/documentation/lighthouse_testing_login_mobile.pdf)
- [Lighthouse report for add post page - desktop](./static/images/documentation/lighthouse_testing_add_post_desktop.pdf)
- [Lighthouse report for add post page - mobile](./static/images/documentation/lighthouse_testing_add_post_mobile.pdf)
- [Lighthouse report for edit post page - desktop](./static/images/documentation/lighthouse_testing_edit_post_desktop.pdf)
- [Lighthouse report for edit post page - mobile](./static/images/documentation/lighthouse_testing_edit_post_mobile.pdf)

### Manual Testing

## Deployment

### Forking the GitHub Repository

### Making a Local Clone

## Credits

### Code

### Content

### Acknowledgements
