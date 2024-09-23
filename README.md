# Walk Anglesey Blog Website

Walk Anglesey is a blogging website focused on sharing walking routes and encouraging a vibrant community of users passionate about exploring the Isle of Anglesey. 

The website offers detailed walk guides, user-contributed posts, weather information, and an interactive map to help users discover and enjoy the amazing walks on offer. Let's [Walk Anglesey!](https://walk-anglesey-84445998906a.herokuapp.com/)

![Hero Image](images/hero-image.jpg)

### [View Walk Anglesey hosted on Heroku](https://walk-anglesey-84445998906a.herokuapp.com/)

![Last commit](https://img.shields.io/badge/Last_Commit-4th_June-orange)
![Contributors](https://img.shields.io/badge/Contributors-1-purple) ![W3C Validation](https://img.shields.io/badge/W3C-validated-green) 
![HTML Validation](https://img.shields.io/badge/HTML-validated-green) ![Languages](https://img.shields.io/badge/Languages-4-blue) ![Frameworks](https://img.shields.io/badge/Frameworks-2-blue) ![API](https://img.shields.io/badge/API's-4-blue)

## User Experience 

### Website Concept 

[Walk Anglesey](https://walk-anglesey-84445998906a.herokuapp.com/) is a new walking blog website built from the ground up, with 2 main goals. To showcase the fantastic walks on Anglesey and to create a community. By developing a welcoming and easy to use website, we want to attract new users to become part of our walking family.

To create a passionate community, we welcome new users to comment on our walk posts, sign up to newsletters and also to get in touch with us and become bloggers themselves, so they can share their love and knowledge of walks on Anglesey.

### Key Features of the Website

* Welcome page with key information about the website.
* Interactive Map with walk route locations.
* Highly Detailed Walk route information.
* Pictures of each walk and points of interest along the route.
* Difficulty rating for each walk.
* Live Weather information.
* Comment on walk blogs.
* Collaboration form for users to get in touch with site owner.
* Newsletter that site users can sign up to.

### User Stories

#### Owner/Admin Goals

* The website needs to be responsive on all devices to ensure a good user experience.
* Ease of use for admin users to create, edit, and delete their own walk blogs and owner can manage all content.
* Ability to moderate comments and manage user interactions to maintain a positive community environment.
* Users wishing to collaborate can be viewed and managed in the back end, facilitating easy communication and coordination.

#### Registered User Goals

* Ability to create an account and log in securely.
* Option to comment on blog posts, sharing their thoughts and experiences about different walks.
* Has the ability to reach out to site owner to recommend walks or become a blogger themselves.
* Option to sign up for newsletters to stay updated on new walks, community news, and other relevant information.

#### Visitor Goals

* Easy navigation to explore the website and find information about various walks on Anglesey.
* Access to general content without needing to register, such as detailed walk guides, maps, and weather information.
* Encouragement to register for an account to access more features and participate in the community.
* Access to subscribe form to join the Newsletter group.

## Design

### Colour Scheme

The colour scheme selected for the website is inspired by nautical themes, reflecting the fresh and vibrant colours walkers would encounter on their coastal walks around Anglesey. The design aims to create a clean, uncluttered, and welcoming environment for users, enhancing their browsing experience and making navigation intuitive.

These are the colours used:

![Colours](images/ux-colours.jpg)

The color scheme features #F9FAFC for a light, airy background, #006b99 for primary text and buttons representing the sea, #004e73 for dynamic hover effects, #fff for clean text and backgrounds, and #848484 for neutral secondary elements with vibes of coastal rocks, creating a cohesive and uncluttered nautical theme.

### Typography

We selected "Lato" for its modern and friendly look, using bold for headings to draw attention and lighter weights for body text to ensure readability. Additionally, "Helvetica" is used in the walk blogs to provide a clear and professional appearance, complementing the overall clean design of the website.

### Imagery & Layout

The website is designed to look great on any device, from desktops to mobile phones, so you get a smooth experience no matter how you browse. We've made sure navigation, the interactive map, weather information, and walk guides are easy to find and use.

Imagery plays a crucial role in the design, with high-quality photos of Anglesey’s landscapes enhancing the visual appeal and providing a glimpse of the stunning walks available. Each guide is packed with pictures of interesting spots along the way, making the content engaging and fun.

With a carefully chosen colour scheme, typography, and layout, Walk Anglesey aims to create a welcoming and user-friendly site that invites you to explore and be part of our walking community.

### Images of Design Mockups

#### Home Page

![Colours](images/mockup_1.png)

#### Walk Blog List

![Colours](mockup_2.png)

#### Walk Details Page

![Colours](mockup_3.png)

## Features

The Website consists of a Responsive Navbar and Footer, a Homepage, a Walks page, About page and a Newsletter sign up page.

## All pages on the website are responsive and have:

* favicon in the web browser tab:

![favicon](images/fav-pic.jpg)


* Every page has a responsive Navbar:

![Navbar](images/nav-pic.jpg)


* There is a footer with social media links on each page:

![footer](images/footer-pic.jpg)


## The Home Page

* A large header image taken by the site owner.

![header image](images/header-pic.jpg)


* Introductory text, A section with a detailed introduction about the website, its purpose, and the types of walking routes and experiences available on Anglesey.

![Intro Text](images/intro-pic.jpg)


* The Interactive map, an embedded Google Map to display walking route locations, enhancing the user's ability to explore visually.

![Map](images/map-pic.jpg)


* A section titled "Walk Blogs" to highlight recent posts. Blog entries displayed in a card layout with images, titles, excerpts, and authors. Pagination to navigate through multiple blog post pages if needed. These blogs are selected from the back end in a random format 

![Homepage Walks](images/home-walks-pic.jpg)


## Walk Blog List Page

* The Walks blog page starts with a randomised image from one of the walk blogs, to offer a unique experience each time a user visits the page. Following that is a list of all the walk blogs featured on the site.

![Walk Page Pic](images/walkpage-pic.jpg)

## Walk Blog Detail

* The top of the page includes a large header image that either displays the featured image of the post or a default placeholder image. Overlaid on this image are the title, author, creation date, and difficulty level of the walk.

![Walk Header](images/walk-detail-pic1.jpg)


* The main content area displays the detailed description of the walk. This includes the author’s narrative and photographs related to the walk, making it informative and engaging highlighting the points of interest walkers will see along the way.

![Walk pictures](images/walk-detail-pic2.jpg)


* Beneath the main walk content follows a map of the walking route, allowing users to visualize the path. Additionally, it includes real-time weather information for the location, helping users prepare for their walk.

![Walk Map and Weather](images/walk-detail-pic3.jpg)


* Below the post content and route map and weather, there is a section that displays comments left by other users. Each comment shows the author, creation date, and content, fostering community interaction. Users must be logged in to view comments.

![Walk Comment](images/walk-detail-pic4.jpg)


* Users can create, delete or edit their own comments, and unapproved comments are marked for the user’s awareness, awaiting admin approval.

![Walk comment box](images/walk-detail-pic5.jpg)

## About Us Page

* The About Us page contains useful information about the group of walkers that make up this passionate group. This content is created on the back end django administration.

![About Header](images/about-pic1.jpg)


* Registered and logged-in users can complete a form for either a walk suggestion or a request to join the walk blog team. This encourages engagement and allows users to share their thoughts and experiences related to the walk.

![About Form](images/about-pic2.jpg)

### Newsletter Subscription Page

* The Subscribe page also contains a hero image which is randomly selected from the walk blogs. Following that is some information for the user and an email and submit function. This information is then sent to the back end for the site owner to send out the Newsletters.

![Subscribe Form](images/subscribe-pic1.jpg)

### Comment Edit Page

* The **Comment Edit** page allows registered and logged-in users to update their comments on a walk blog. The form is pre-filled with the existing comment, and users can either update the comment or cancel the action, which takes them back to the walk details page.

![Comment Edit Page](images/comment_edit.html_screenshot.png)


### Future Implementations

In future updates, we plan to add the following features to enhance the user experience and functionality of the Walk Anglesey website:

* **User Profiles**: Allow users to create and customize their own profiles.
* **Favorite Walks**: Enable users to save their favorite walks for easy access later.
* **Like Functionality**: Implement a like feature for users to express their appreciation for specific walks and posts.
* **Wildlife Section**: Add a dedicated section for wildlife sightings and information, enriching the content with details about the flora and fauna encountered on walks.
* **Photo Drop Box**: Create a section where users can share their own images from walks, contributing to a community-driven gallery.
* **Social Sharing**: Integrate social media sharing options for users to share walks on their social networks.

These features aim to build a more interactive, engaging, and community-focused platform for all users.

### Accessibility 

We are committed to making Walk Anglesey accessible to all users.

![Lighthouse](images/lighthouse.jpg)

## Technologies Used

### Languages Used

* **HTML5**: For structuring the content.
* **CSS3**: For styling the content.
* **JavaScript**: For interactive elements and functionalities.
* **Python**: For back-end development with Django framework.

### Frameworks, Libraries and programmes used

* **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* **Bootstrap**: A popular front-end framework for developing responsive and mobile-first websites using HTML, CSS, and JavaScript.
* **Django Allauth**: A package for Django that provides a comprehensive set of user authentication, registration, and account management tools.
* **Cloudinary**: A cloud-based service that offers comprehensive image and video management, including storage, transformation, and delivery.
* **Google Maps API**: An application programming interface that allows you to embed Google Maps on your web pages and customize them with your own content.
* **OpenWeatherMap API**: A service that provides weather data, including current weather, forecasts, and historical data to developers through an API.
* **Django Crispy Forms**: A Django application that helps you create beautiful, Bootstrap-compatible forms easily.
* **Django Summernote**: A package for integrating the Summernote WYSIWYG editor into Django projects, enabling rich text editing.
* **Gunicorn**: A Python WSGI HTTP server for running web applications, commonly used to serve Django applications in production.
* **Whitenoise**: A middleware for Django that helps serve static files efficiently in production.
* **PostgreSQL**: An advanced, open-source relational database management system known for its reliability and robustness.

## Deployment & Local Development

### Agile Development

When building this project, I used Agile methodology to keep things flexible, collaborative, and always improving. I broke down the project into smaller chunks and worked on each piece one at a time, making sure each part was solid before moving on to the next.

![Agile Development](images/agile-development.jpg)

Below is an example of the user stories:

![User Story Example](images/error_page_userstory.png)

[Here is the current Project Board.](https://github.com/users/cniblock/projects/4)

To define the project's scope and requirements, I used user stories with each story having a clearly defined set of acceptance criteria. Due to time constraints, two user stories were prioritized as "won't have" using the MOSCOW model, meaning they will be part of the future development of the site.

### Models

The following models are used in this application:

### Entity Relationshop Diagram

#### Post Model

The Post model represents a blog post or article. It has the following fields:

![Post Model](images/erd-1.jpg)

The Post model has a many-to-one relationship with the User model through the author foreign key.

#### Comment Model

The Comment model represents a comment left on a blog post. It has the following fields:

![Comment Model](images/erd-2.jpg)

The Comment model has a many-to-one relationship with the Post model through the post foreign key:

#### About Model

The About model represents information about the application. It has the following fields:

![About Model](images/erd-4.jpg)

#### CollaborateRequest Model

The CollaborateRequest model represents a collaboration request from another user. It has the following fields:

![Collaboration Model](images/erd-5.jpg)

#### Newsletter Model

The NewsletterSubscriber model represents a subscriber to a newsletter. It has the following fields:

![Newsletter Model](images/erd-3.jpg)

### Forms

#### Forms Used in the Project

The project uses several forms to interact with the user and collect data. Below is a brief description of each form:

#### Post Form

The Post Form is used to create new blog posts. It includes fields for the post content, title, and other metadata. The form uses a template to generate a default content structure for new posts.

![Post Form](images/post-form.jpg)

#### Comment Form

The Comment Form is used to allow users to leave comments on blog posts. It includes a single field for the comment body, which is required.

![Comment Form](images/comment-form.jpg)

#### Collaborate Form

The Collaborate Form is used to collect requests for collaborations from users. It includes fields for the user's name, email address, and a message describing the collaboration request.

![Collab Form](images/colab-form.jpg)

#### Newsletter Form

The Newsletter Form is used to send newsletters to subscribers. It includes two fields: a subject line and a message body, which can be a short text or a longer text area.

![Newsletter Form](images/newsletter-form.jpg)

#### Newsletter Subscription Form

The Newsletter Subscription Form is used to collect email addresses for newsletter subscribers. It requires a single field for the email address, which is used to send newsletters to subscribers.

![Newsletter Sub Form](images/newsletter-sub-form.jpg)

### Views

#### Views Used in the Project

The project uses several views to handle user interactions and display data. Below is a brief description of each view:

#### Post List View
The Post List View displays a list of blog posts, with pagination and filtering by post status. It uses a template to display the list of posts.

![Post View](images/post-view.jpg)

#### Post Detail View
The Post Detail View displays a single blog post, along with its comments and weather data. It allows users to leave comments and edit or delete their own comments.

![Post detail view](images/post-detail-view.jpg)

#### About View

The About view is used to display information about the application. It also handles collaboration requests.

![About View](images/about-view.jpg)

#### Comment Edit View
The Comment Edit View allows users to edit their own comments on a blog post.

![comment edit view](images/comment-edit-view.png)

#### Comment Delete View
The Comment Delete View allows users to delete their own comments on a blog post.

![comment delete view](images/comment-delete-view.png)

#### Walks List View
The Walks List View displays a list of all blog posts, with the option to display a random hero image.

![Walks List View](images/walklist-view.jpg)

#### Subscribe Newsletter View
The Subscribe Newsletter View allows users to subscribe to the newsletter by submitting their email address. It also displays a hero image.

![Subscribe Newsletter View](images/sub-news-view.jpg)

#### Weather Function
The get_weather function fetches the current weather data for a specified location using the OpenWeatherMap API.

![Weather Function](images/weather-view.jpg)

These views work together to provide a comprehensive blogging platform with commenting, editing, and deleting features, as well as newsletter subscription.

### URLs

#### URL Patterns Used in the Project

The project uses the following URL patterns to map URLs to views and templates.

![URLs](images/urls.jpg)

### Template

Django templates provide a way to define the presentation layer of the application, rendering dynamic content generated by views and presenting it to users in a structured and customizable format.

![Template 1](images/template-1.jpg)
![Template 2](images/template-2.jpg)
![Template 3](images/template-3.jpg)
![Template 4](images/template-4.jpg)

## Custom Error Pages

I have created custom error pages for **403**, **404**, and **500** errors to enhance user experience. Below are the details of each error page along with descriptions and screenshots.

### 1. 404 Page Not Found

This page is displayed when a user attempts to access a page that does not exist on the website. The page informs users that the requested page could not be found and provides a link to return to the homepage.

#### Screenshot of 404 Page:
![404 Page Screenshot](images/404_error_page.png)
![404 Page Code](images/404_error_code.png)

---

### 2. 403 Forbidden

This page is displayed when a user tries to access a page they don't have permission to view. The error page clearly communicates that the user does not have the necessary permissions to access the resource.

#### Screenshot of 403 Page:
![403 Page Screenshot](images/403-page-screenshot.jpg)
![404 Page Code](images/403_error_code.png)

---

### 3. 500 Server Error

This page is displayed when there is a server-side error. It informs the user that something went wrong on the server and provides an option to return to the home page.

#### Screenshot of 500 Page:
![500 Page Screenshot](images/500-page-screenshot.jpg)
![404 Page Code](images/500_error_code.png)

---

## Testing

Throughout the development of this project, manual testing has been conducted to ensure that the application functions as expected. Additionally, 13 automated tests have been written to cover a range of scenarios, including form validation and collaboration request submission. All of these tests have been run and have passed without issue, providing confidence in the stability and reliability of the application.

### Manual Testing

* Registration

![Registration Test](images/account-test.jpg)

* Navbar

![Navbar test](images/nav-test.jpg)

* CRUD

![CRUD Test](images/crud-test.jpg)

* General Tests

![General tests](images/general-test.jpg)

### Automated Testing

#### TestPostViews:
**test_render_post_detail_page_with_comment_form:**

* Checks if the post detail page renders correctly and contains the post title, content, and a comment form.

**test_render_post_list_page:**

* Verifies if the post list page renders correctly and contains the post title and excerpt.

**test_render_post_list_page_with_placeholder_image:**

* Ensures that the post list page renders with a placeholder image if no featured image is provided for a post.

**test_successful_comment_submission:**

* Tests the successful submission of a comment on a post. It verifies if the comment submission returns a success message.

**test_successful_newsletter_subscription:**

* Tests the successful subscription to the newsletter. It verifies if the subscription redirects to the home page and adds the subscriber to the database.

#### TestCommentForm:

**test_form_is_valid:**

* Checks if the comment form is valid when provided with valid data.

**test_form_is_invalid:**

* Verifies that the comment form is invalid when submitted with empty data.

### TestAboutView:

**test_render_about_page_with_collaborate_form:**

* Checks if the about page renders correctly and contains the about content and a collaboration form.

**test_successful_collaboration_request_submission:**

* Tests the successful submission of a collaboration request. It verifies if the request submission returns a success message.

#### TestCollaborateForm:

**test_form_is_valid:**

* Tests if the collaborate form is valid when provided with valid data for all fields.

**test_name_is_required:**

* Verifies that the name field is required in the collaborate form.

**test_email_is_required:**

* Ensures that the email field is required in the collaborate form.

**test_message_is_required:**

Checks that the message field is required in the collaborate form.

### Code Validation

* HTML Validation Pass

![HTML Validation](images/W3C-validator.jpg)

* w3c Validation Pass

![CSS Validation](images/css-validation.jpg)

* JSHint validation Pass

![jshint](images/jshint.jpg)

* Python

All Python code has been passed through Code Institute Python Linter tool and no major errors were found. There are however several "line too long" and "trailing whitespace" errors and suggestions. These errors have no major impact on the website but future iterations of the website will address these suggestions.

## Deployment & Local Development

This project was developed using the Django framework and deployed to Heroku. Below is a step-by-step guide to deploy the project on Heroku and also run it locally on your machine.

### Deployment to Heroku

1. **Create a Heroku account**:  
   If you don’t have one, sign up for an account on [Heroku](https://www.heroku.com/).

2. **Create a new app**:
   - Log in to Heroku and click on "New" and then "Create new app".
   - Choose an app name (this must be unique) and select your region (e.g., Europe).

3. **Set up Buildpacks**:
   - Go to the "Settings" tab of your app and scroll down to "Buildpacks".
   - Add `Python` as a buildpack.
   - Optionally, you can add `Node.js` as a buildpack if you’re using JavaScript-related tools.

4. **Configure Environment Variables**:
   - In the "Settings" tab, click "Reveal Config Vars".
   - Add the following key-value pairs for your environment variables:
     - `SECRET_KEY`: Your Django secret key.
     - `CLOUDINARY_URL`: Your Cloudinary API key (if using Cloudinary for media).
     - `DATABASE_URL`: This will be automatically set by Heroku after you add PostgreSQL.
     - `ALLOWED_HOSTS`: Set to `your-app-name.herokuapp.com`.
     - `DEBUG`: Set to `False` for production.

5. **Connect to PostgreSQL**:
   - Go to the "Resources" tab.
   - Under "Add-ons", search for `Heroku Postgres` and provision it.

6. **Deploy the App**:
   - Go to the "Deploy" tab.
   - Under "Deployment Method", select GitHub and connect your GitHub repository.
   - Choose the branch you want to deploy from (usually `main` or `master`).
   - Enable "Automatic Deploys" or deploy manually by clicking "Deploy Branch".

7. **Run Database Migrations**:
   - Go to the "More" dropdown in the top-right corner of the app’s dashboard and select "Run Console".
   - Run the following commands to migrate the database:
     ```bash
     python manage.py migrate
     ```
   - Create a superuser to access the admin panel:
     ```bash
     python manage.py createsuperuser
     ```

8. **Collect Static Files**:
   - Run the following command to collect static files for production:
     ```bash
     python manage.py collectstatic
     ```

9. **Access the app**:
   - Your app should now be live at `https://your-app-name.herokuapp.com`.

### Local Development Setup

To run this project locally on your machine, follow these steps:

1. **Clone the Repository**:
   - Clone the project from GitHub using the following command:
     ```bash
     git clone https://github.com/your-username/your-repository.git
     ```

2. **Create a Virtual Environment**:
   - Inside the project folder, create and activate a virtual environment:
     ```bash
     venv\Scripts\activate
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   - Install all required Python packages from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add the following environment variables:
     ```env
     SECRET_KEY=your-secret-key
     DEBUG=True
     CLOUDINARY_URL=your-cloudinary-url
     DATABASE_URL=sqlite:///db.sqlite3  # For local development, use SQLite
     ```

5. **Run Migrations**:
   - Apply migrations to set up the local database:
     ```bash
     python manage.py migrate
     ```

6. **Create a Superuser**:
   - Create a superuser to access the admin panel:
     ```bash
     python manage.py createsuperuser
     ```

7. **Run the Local Development Server**:
   - Run the Django development server to view the site locally:
     ```bash
     python manage.py runserver
     ```

8. **Access the App**:
   - Open your web browser and go to `http://127.0.0.1:8000/` to view the application locally.

## Updates Based on Assessor's Feedback

After receiving feedback on the project, several changes and improvements have been made to address the issues raised and enhance the overall functionality and design. Below is a list of changes:

### 1. **Fixed CRUD Functionality**
- Implemented missing Create, Read, Update, and Delete (CRUD) functionality for comments and posts.
- Users can now successfully add, edit, and delete their comments on blog posts.
- Admins can now fully approve, edit, and delete walking routes and posts.

### 2. **Enhanced Agile Documentation**
- User stories were refined with better structure and more detailed acceptance criteria.
- Added user stories related to the new features, including CRUD functionality, custom error pages, and admin privileges.

### 3. **Custom Error Pages**
- Added custom error pages for 403, 404, and 500 errors to improve user experience when encountering issues.
    - **403 Forbidden**: Displayed when a user tries to access restricted content.
    - **404 Page Not Found**: Displayed when a user navigates to a non-existent page.
    - **500 Server Error**: Displayed when there is an issue with the server.
- Included images and better design for these error pages.
- Added handling of error views in `views.py` and updated `urls.py` to manage custom error pages.

### 4. **Design Mockups and Design Rationale**
- Added mockups for all key pages in the README.
- Included a visual representation of the user interface, providing clear insight into the design process.
- Provided a more in-depth explanation of the design choices, including the color scheme, typography, and responsive layout.
- Justified the selection of colors and fonts to match the nautical and outdoor theme of the website.
- Included details on imagery, visual hierarchy, and layout improvements.

### 5. **Improved Deployment Documentation**
- Expanded the "Deployment & Local Development" section of the README.
- Provided step-by-step instructions on how to deploy the application on Heroku and how to run it locally.
- Documented necessary environment variables and database setup, improving clarity for future developers.

### 6. **Improved Commit Messages**
- Following the assessor’s advice, we improved the commit messages to make them more descriptive and specific about the changes made.
- Ensured commits are atomic and focused on individual changes, making the Git history easier to follow.

### 7. **Test Coverage**
- Reviewed and updated the automated and manual tests to ensure they cover all key functionalities, especially CRUD operations.
- Documented all tests in the README, including descriptions of the tests and their results.

---

These changes were made to enhance the user experience, improve functionality, and ensure that the application meets the required assessment criteria. The updates make the project more robust, scalable, and user-friendly, while also improving the backend logic and documentation.

### Bugs

#### Known Issues

* The Send_Newsletter function is currently unavailable. The html and form has been set up but as of deployment, the superuser is unable to send the Newsletter to all subscribers.

* Googlemaps error in console suggesting to use AdvancedMarker, however, when this is implemtented, the map does not work.
![googlemapserror 1](images/googlemap-error.jpg)

* Performance issue with Googlemaps
![googlemapserror 2](images/googlemap-error-2.jpg)

* Error related to Cloundinary image links being http instead of https
![https](images/https-error.jpg)

## Credits

### Media

* Code Institute django blog walk through.

* All Images are linked from googleimages and are only intended for educational purposes.

* Googlemaps 
https://developers.google.com/maps

* Weather App API
https://openweathermap.org/

### Acknowledegments 

I'd like to take the opportunity to thank the Code Institute team for their support and the amazing community on slack who are always there to help, no matter what time of the day it is. Tomas_K !