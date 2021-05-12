# ECE140B-Individual-Website-Assignment


Once you created the website, please submit this form if you haven't already **(Due 5/10 11:59PM)** : https://forms.gle/5UTXRfHTJ2cZ861F7

## Project Overview
### A distributed ECE 140 bio / CV showcase! Students will each build and host a website that:
- Presents their personal CV – must include their ECE 140B MVP
- Provides a REST API to access their data: avatar image, name, email, projects, etc. (we should be explicit on the API requirements so that they don’t have trouble interfacing with each other.

## Grading Rubric

| Component | Description                                                  |
| --------- | ------------------------------------------------------------ |
| UX        | <ul><li>Website is simple, flexible and usable with diverse abilities</li><li>It is clear that the student has put thought into the design so as to minimize potential user frustrations or negative experiences</li><li>Website is learnable by customers at all experience levels</li><li>Website is tolerant of errors and adaptable to user preferences</li><li>Website works comfortably with low physical and cognitive effort</li><li>It is clear that the student kept the target demographic (personas) in mind when designing the website</li></ul>
| UI        | <ul><li>Website adhere to the 10 UI principles discussed in lecture</li><li>Styles and layout are consistent throughout</li><li>Website provides the user with direct control over the system</li><li>Website develops and maintains predictability</li><li>Website abides by all 10 laws of UI design discussed in lecture</li></ul>
| IA        | <ul><li>Navigation is easy to locate and operate</li><li>Applied consistently on each page</li><li>Works in full-size and reduced forms</li></ul>

## Deliverables

*Note that all deliverables are due on Monday after the end of the week specified, unless explicitly extended. For example, the end of week 7 is Monday May 17 at 11:59 pm*

| Week | Deliverable                                                  |
| :--: | ------------------------------------------------------------ |
|  6 (EXTENDED, due May 11th Tue 11:59PM)  | <ul><li>Website hosted on DigitalOcean and accessible via a URL</li><li>Website must contain some content that indicates that website is under construction (“coming soon” motif)</li><li>Must contain name of student</li><li>Website design uses custom CSS (not external library)</li></ul>
|  7 (Due May 17 Mon 11:59PM)   | <ul><li>Server on DigitalOcean has web and API routes</li><li>All API data must be stored in a MySQL database (schema up to you)</li><li>Web Routes:<ul><li><b>/welcome</b><ul><li>HTTP response:<ul><li>shows guestbook page that shows previously entered names and comments</li><li>a form where users can enter their <b>name</b> and <b>email</b> and <b>comment</b> and hit submit, which will store their data in the MySQL DB<ul><li>Schema is up to you, but you must store: name, email, comment, timestamp at a bare minimum</li></ul></li><li>when they submit the form, a “thank you for visiting” type of message should be displayed</li></ul></li></ul></li><li><b>/cv</b><ul><li>HTTP response:<ul><li>a placeholder site for your CV that can just say “coming soon” for now</li></ul></li></ul></li></ul><li>API routes (all must return JSON objects. For avatar any image is fine as long as it’s appropriate. All others fields come from the database – no hard-coded responses:</li><ul><li><b>/avatar</b><ul><li>JSON response:<ul><pre>{<br>“image_src”: <URL to personal image (in public folder)><br>}</pre></ul></li></ul><li><b>/personal</b><ul><li>JSON response:<ul><pre>{<br>“first_name”: \<your first name\>,<br>“last_name”: \<your last name\>,<br>“email": \<your email address\><br>}</pre></ul></li></ul></li><li><b>/education</b><ul><li>JSON response:<ul><pre>{<br>“school”: <school_name>,<br>“degree”: <degree_program>,<br>“major”: \<major\>,<br>“date”: <graduation_year><br>}</pre></ul></li></ul></li><li><b>/project</b><ul><li>JSON response:<ul><pre>{<br>“title”: \<project title>,<br>“description”: \<details of project>,<br>“link”: <external link to project (MVP on Digital Ocean)>,<br>“Image_src”: <URL to project image (in public folder)><br>“team”: {<br>    “api_link”: <URL of teammate’s REST API><br>}</pre></ul></li></ul></li></li></ul></li></ul>
|  8 (Due May 24 Mon 11:59PM)  | <ul><li>Complete CV web route and “about” page</li><li>Web Routes:<ul><li><b>/cv</b><ul><li>HTTP response:</li><ul><li>Personal resume page</li></ul></ul></li><li><b>/about</b><ul><li>a placeholder page which will catalog your UI/UX design ideas  that can just say “coming soon” for now</li></ul></li></ul></li><li>Wireframe of IA design<ul><li>Visual representation of product’s infrastructure, features and hierarchy</li><li>Defines every route customers can take through your product</li><li>Includes logical and physical models users are exposed to</li></ul></li></ul>
|  9 (Due May 31 Mon 11:59PM)  | <ul><li>Main landing page<ul><li>This should be your “/” route aka homepage.</li><li>This should not be a skeleton page, we expect decent design using the design principles presented in class</li><li>We expect to see CSS</li><li>We expect to see some functional Javascript<ul><li>must be part of the website design, can’t have things such as a random timer or something like that</li></ul></li></ul><li>All of your routes should be accessible from the page. Subpages don't have to be directly linked to the main page, but are accessible via buttons or other UI elements. Think of it as the root of all of your pages.<ul><li>This includes any pages that you have “under construction”</li></ul></li></li><li>You should have a UI element to navigate to any personal resumes of your group.</li><li>Be sure that your team member’s sites can navigate to yours as well.</li></ul>
|  10 (Due June 7 Mon 11:59PM) | <ul><li>Specify at least 3 media queries for various screen sizes (mobile, tablet, desktop)</li><li>Add alt text to your images for use with a screen reader</li><li>Your site is usable even when colors are removed (all greyscale) </li></ul>
  

### Good Luck!!!
*For questions -- please use Slidespace discussions or stop by office hours for help!!*
