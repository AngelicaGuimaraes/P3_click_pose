# Click Pose

![Responsive screenshot](/assets/images/screen_capture_responsive.png)

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

![Initial wireframe](/assets/images/wireframe_initial.png)

During the development process, a few things were changed in the wireframe. The main reason was that I wanted to leave some features to be added later, e.g different levels of difficulty for the user to challenge himself even more.

After the final modifications, the final application wireframe looks like this:

![Final wireframe](/assets/images/wireframe_final.png)

[Back to top](#click-pose)

## Features 

### Existing Features

#### Landing Page

On the Landing Page the user is greated and he has the option to choose between 4 different categories of poses.

![Landing Page](/assets/images/screen_capture_start.png)

#### First Pose Selected

After selection, the user is presented with a pose from the Google Sheets. The user is also asked whether he wants to practice another pose from the same category, with the option to choose between 'Yes' or 'No'.

![First Pose Selected](/assets/images/screen_capture_stretch.png)

#### Another Pose

When the option has been given by the user, he is brought to another pose of the same category or he is asked whether he wants to continue practicing yoga, depending on his previous choice.

![Another Pose](/assets/images/screen_capture_another_pose.png)

#### More Yoga

If 'No' is selected, the user will be asked whether he wants to practice more yoga and the option to answer with a 'Yes' or 'No'.

![More Yoga?](/assets/images/screen_capture_more_yoga.png)

#### Back to Menu

If the user chooses to continue practicing more yoga poses, he will be brougth back to the menu.

![Back to Menu](/assets/images/screen_capture_back_to_menu.png)

#### Leave Feedback

Otherwwise, he will be asked to leave a feedback before leaving the app.

![Leave Feedback](/assets/images/screen_capture_leave_feedback.png)

#### Quit App

User will be thanked for leaving his feedback and will be asked if he wants to quit the app.

![Quit App](/assets/images/screen_capture_quit.png)

## Features Left to Implement

For a future version of this app, options of different levels of dificulty will be added, as well as more poses for the user to practice.
Also, will be shown to the user, the avarage of the ratings.

[Back to top](#click-pose)

## Technologies and libraries used

Main language

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)

Python libraries and api used

- [Sys](https://docs.python.org/3/library/sys.html)
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Colorama](https://pypi.org/project/colorama/)

### Data storage

Poses, intructions, benefits and feedbacks are fetched and stored in a Google Sheet using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)

## Testing 

Testings have been conducted continuously during the development process.
Manual testings have been conducted by the author, my fellow student and friend [Mats Simonsson](https://www.linkedin.com/in/mats-simonsson-2aa6874/) and also my fellow student [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/).

### Bugs during development

- Problems to create a random loop between various poses from the same category.
  - <i>Left this version of the app with only two options for each category and placed them in different functions and used an if else statement to call them.</i>
- Problems to send the ratings to the Google Sheet.
  - <i>My fellow student, Mats Simonsson, helped me to create the right function for that purpose.

### Validator Testing 

The code has also been tested by using PEP8 Online http://pep8online.com/.

Final testing warned about long lines. This has been corrected and the code passes without any issues.

![PEP8 Validation](/assets/images/screen_capture_PEP8.png)

### Unfixed Bugs

- No known bugs at this point.

 [Back to top](#click-pose)

## Development and Deployment

The development environment used for this project was GitPod. To track the development stage and handle version control regular commits and pushes to GitHub have been conducted. The GitPod environment was created using a template provided by Code Institute.

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

After those steps were taken the application was deployed at the following link: https://click-pose.herokuapp.com

## Content 

- All instructions and benefits on the Google Sheet are credited to:
- [Prevention](https://www.prevention.com/fitness/workouts/g30417941/best-yoga-stretches/)
- [Yogi Approved.com](https://www.yogiapproved.com)
- [Daily Burn](https://dailyburn.com/)
- [Yoga Baics](https://www.yogabasics.com)

## Credits 

### For code inspiration, design inputs, help and advice.

I have consulted numerous websites, individuals and slack channels to get support for the code. No code block is directly copied but some generates from information I gathered from other developers and sites:

 - [Google Sheets for Developers](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells) for information about exctracting information from a Google Sheet.
 - [Code Institute - Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) for inspiration and understanding on how to develope the project.
 - [W3 Schools](https://www.w3schools.com/python/python_lists_loop.asp) for understanding how to loop trhough lists.
 - [pypi.org](https://pypi.org/project/colorama/) for understanding how to change text color on the console.
 - [PEP 8](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator) to understand about line breaks.
 - [Code Institute](https://codeinstitute.net/) for all course material leading up to this project.
 

### Acknowledgment

 - [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) My amazing mentor at Code Institute. Thank you for your support, feedback, and for keeping me on the right track.
 - [Mats Simonsson](https://www.linkedin.com/in/mats-simonsson-2aa6874/) My fellow student, dear friend and mentor. Thank you for all the patience, for spending so much time helping me with my questions, for helping me during the tough moments and for helping me with the code.

 - [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe

 - [Canva](https://www.canva.com/) was used to create the wireframe for this project.

[Back to top](#click-pose)