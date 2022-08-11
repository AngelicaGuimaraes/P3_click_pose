# Click Pose

![Responsive screenshot](/images/screen_capture_responsive.png)

# The purpose with this project

Click Pose is a console based application for individuals that want to dedicate some time practicing yoga and experiencing its benefits. The user interface is text based and it is run from a text terminal or other types of command-line interfaces.

The application gives the user the possibility to practice four different types of yoga poses, stretch, strength, torion and balance. Each category with two different poses that the user can go through.
On the landing page the user will be greated and will have the four otions to choose from. After that, the user will have the option to practice one more pose from the same category, choose to practice a pose from another category or quit the app.
When choosing to quit, the user will be asked to leave a feedback to qualify his experience on the app.

Target audience: All individuals that want to practice and experience the benefits of yoga.

This project is the third of five milestone projects that needs to be completed in order for me to receive a diploma in Software Development from The Code Institute https://codeinstitute.net/

Required technologies for this project: Python

A live version of this project can be found at this url: https://click-pose.herokuapp.com/

# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Goals](#user-goals "User goals")
  + [Project Requirements](#project-requirements "Project Requirements")
  + [Design Diagram](#design-diagram "Design Diagram")
    + [Wireframe](#wireframe "Wireframe")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Landing Page](#landing-page "Landing Page")
    + [First Pose Selected](#first-pose-selected "First Pose")
    + [Another Pose](#another-pose "Another Pose")
    + [More Yoga](#more-yoga "More Yoga")
    + [Back to Menu](#back-to-menu "Back to Menu")
    + [Leave Feedbback](#leave-feedback "Leave Feedback")
    + [Quit App](#quit-app "Quit App")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Technologies and Libraries Used](#technologies-and-libraries-used "Technologies and Libraries Used")
  + [Data storage](#data-storage "Data Storage")
+ [Testing](#testing "Testing")
  + [Bugs during development](#bugs-during-development "Bugs during development")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Content](#content "Content")
+ [Credits](#credits "Credits")

## UX

### User Demographic

This application is ment for:

 - All individuals that want to practice some yoga poses.
 - All individuals that want to learn a bit about yoga's benefits.

### User Goals

To have the possibility of taking some time for themselves, relax and unwind through the practice of yoga poses.

### Project Requirements

Python application using libraries/API and deployed to a cloud-based platform.

### Design Diagram

Click Pose is a console based application. For that reason, not much work was put on the graphical design.

#### Wireframe

This is the initial wireframe:

![Initial wireframe](/images/wireframe_initial.png)

During the development process, a few things were changed in the wireframe. The main reason was that I wanted to leave some features to be added later, e.g different levels of difficulty for the user to challenge himself even more.

After the final modifications, the final application wireframe looks like this:

![Final wireframe](/images/wireframe_final.png)

[Back to top](#click-pose)

## Features 

### Existing Features

#### Landing Page

On the Landing Page the user is greated and he has the option to choose between 4 different categories of poses.

![Landing Page](/images/screen_capture_start.png)

#### First Pose Selected

After selection, the user is presented with a pose from the Google sheets. The user is also asked whether he wants to practice another pose from the same category, with the option to choose between 'Yes' or 'No'.

![First Pose Selected](/images/screen_capture_stretch.png)

#### Another Pose

When the option has been given by the user, he is brought to another pose of the same category or he is asked whether he wants to continue practicing yoga, depending on his previous choice.

![Another Pose](/images/screen_capture_another_pose.png)

#### More Yoga

If 'No' is selected, the user will be asked whether he wants to practice more yoga and the option to answer with a 'Yes' or 'No'.

![More Yoga?](/images/screen_capture_more_yoga.png)

#### Back to Menu

If the user chooses to continue practicing more yoga poses, he will be brougth back to the menu.

![Back to Menu](/images/screen_capture_back_to_menu.png)

#### Leave Feedback

Otherwwise, he will be asked to leave a feedback before leaving the app.

![Leave Feedback](/images/screen_capture_leave_feedback.png)

#### Quit App

User will be thanked for leaving his feedback and will be asked if he wants to quit the app.

![Quit App](/images/screen_capture_quit.png)

## Features Left to Implement

For a future version of this app, options of different levels of dificulty will be added, as well as more poses for the user to practice.

[Back to top](#click-pose)

## Technologies and libraries used

Main language

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)

Python libraries and api used

- [Sys](https://docs.python.org/3/library/sys.html)
- [Random](https://docs.python.org/3/library/random.html)
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Termcolor](https://pypi.org/project/termcolor/)

### Data storage

Jokes, submitted jokes, sumbmitter name and scores are fetched and stored in a Google Sheet using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)



## Testing 

Testing has been conducted continuously during the development process. Manual testing has been conducted by the author and my mentor [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) and fellow student [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/). Read more about bugs during development and unfixed bugs for more information.



### Bugs during development

- Using Colorama library but my tests are not working. When I do a print syntax with the provided syntax to change the font color "Hello World" is not printing.
  - <i>Used the wrong syntax. Needed to add a "+" sign before the string</i>
- Pure strings are using the selected colors but all prints from the worksheet are still white and I get a syntax error.
  - <i>Tried Termcolor library instead of Colorama library and it did the trick</i>
- Get error messages when I try to access a specific row in the worksheet
  - <i>Used the wrong syntax for the library Gspread. Tried to install and import a different library but that was also problematic. Eventually I found the syntax for the Gspread library and it worked.</i>
- Not able to add new rating with total rating
  - <i>The variables were strings, converted them to int's and it worked</i>
- Not able to get a proper error message when rating not entered correctly
  - <i>Used an if/else statement to check and return if input is faulty</i>
- The worksheet is not updating correctly. Can't figure out why.
  - <i>Went back to look at Love Sandwiches and created a function that updates the worksheet based on that project</i>
- Can't figure out how to correctly copy the formula needed in the spreadsheet to get average rating.
  - <i>Will try to do the calculation inside Python instead. Update: Did overhaul all that had to do with average score. Removed the calculation of score from the spreadsheet and did the calculation in run.py instead</i>
- When a joke is rated with a number containing a . or a , the application crashes.
  - <i>Added a try statement to check that the input is an integer</i>
- On the end screens: If an integer or float value is entered the application crashes.
  - <i>Created a nested function inside the end function that validates the input and prevents crashing</i>
- Application crashes if enter is pressed without a value in the end screens.
  - <i>Created a nested function inside the end function that validates the input and prevents crashing</i>
- Users can submit joke and name with only white spaces.
  - <i>Added nested functions in both submit functions for joke and name that controlls lenght and check for white spaces.Found information on how to do it on https://www.geeksforgeeks.org/python-string-isspace-method/</i>
- Average score is not calculated properly.
  - <i>The formula for average score was not correct. It contained wrong values. Corrected.</i>

### Validator Testing 

The code has also been tested by using PEP8 Online http://pep8online.com/.

Final testing warned about long lines. This has been corrected and the code passes without any issues.

### Unfixed Bugs

Currently working to solve the bugs in this list. They will be moved to the Bugs during development section when they are solved.

- No known bugs at this point

 [Back to top](#dad-jokes)

## Development and Deployment

The development environment used for this project was GitPod. To track the development stage and handle version control regular commits and pushes to GitHub has been conducted. The GitPod environment was created using a template provided by Code Institute.

The live version of the project is deployed using Heroku(https://heroku.com)

This is how this project was deployed using Heroku:

To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in GitPod. This file needs to contain a list of all libraries the project needs to run as a Heroku App.

Then follow these steps:

 - Login to Heroku (Create an account if necessary)
 - Click on New in the Heroku dashboard and select ”Create new app”
 - Write a name for the app and choose your region and click ”Create App”
 - In the settings tab for the new application I created two Config vars.
   - One is named CREDS and contains the credentials key for Google Drive API
   - One is name PORT and has the value of 8000
 - Two buildpack scripts were added: Python and Nodejs (in that order)

Heroku CLI was used to deploy the project. The following steps were taken in the terminal in GitPod

Deploying your app to heroku
1. Login to heroku and enter your details.
 - command: heroku login -i
2. Get your app name from heroku.
 - command: heroku apps
3. Set the heroku remote. (Replace <i>app_name</i> with your actual app name)
 - command: heroku git:remote -a <i>app_name</i>
4. Add, commit and push to github
 - command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
 - command: git push origin main
 - command: git push heroku main

After those steps were taken the application was deployed at the following link: https://dad-jokes-1.herokuapp.com/

## Content 

- All text content in the application is created by the author of the project.
- The initial 24 jokes in the Google Sheet are credited to [Country Living](https://www.countryliving.com/life/a27452412/best-dad-jokes/) and the submitter name for these jokes are set to CL

## Credits 

### For code inspiration, design inputs, help and advice.

I have consulted numerous websites, individuals and slack channels to get support for the code. No code block is directly copied but some generates from information I gathered from other developers and sites:

 - [Google Sheets for Developers](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells) for information about exctracting information from a Google Sheet.
 - [Code Institute - Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) for inspiration and understanding on how to develope the project.
 - [W3 Schools](https://www.w3schools.com/python/python_lists.asp) for understanding how to remove items from lists.
 - [W3 Schools](https://www.w3schools.com/python/gloss_python_type_conversion.asp) for understanding variable conversion.
 - [Code Institute](https://codeinstitute.net/) for all course material leading up to this project.

### Acknowledgment

 - [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) My fantastic mentor at Code Institute, thank you for your support, feedback, bug testing and great sense of humor.
 - [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/) Thank you for testing and contribution of ideas and dealing with my stress over this project.

 [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe

[Back to top](#dad-jokes)