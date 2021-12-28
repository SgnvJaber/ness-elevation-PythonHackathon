#QA Automation Testing Showcase
####This project is made during our bootcamp to demonstrate our knowledge and capabilities in QA Automation.

Authors: Diana Choubaev, Saed Jaber, Tehila Yafee
Overview

###This project performs automated testing of various applications:

Web based Real World App  <br>
API - JSON-Server <br>
Mobile application - Financial Calculators App <br>
Electron application - API Demos App <br>
Desktop application - Windows Calculator <br>
###Infrastructure includes:

- Layers (utilities, extensions, workflows...)
- Page object model design pattern
- External files Support
- Failure mechanisms
- Electron driver
- Reporting system
- Support for different client browsers
- API support
- Visual testing (Aplitools)
- Database support
- CI & CD support
###Tools & Frameworks:

- PyTest Framework
- Listeners interface for Logs & Customizable PyTest Reports
- Selenium Python & API
- Requests for API Testing
- Aplitools for Visual Testing
- Appium Studio & Python-Appium for Mobile Testing
- MySQL Database to store inputs to add new users in Real World App
- DDT using CSV file holding math calculations for Desktop tests
- Jenkins for Automating Test executions & Test Pipelines
- Allure Reports - Reporting System
##Test Overview

Api tests:
1. Post a new song
2. Show all songs 
3. Update specific song details

####Desktop tests:

1. Addition between 2 numbers using DDT

####Web tests:

1. Log in
2. Signup new users using the database
3. Transaction from logged-in username to one of the contacts
4. Notifications count using Aplitools
5. Verify left-side menu has 4 options

####Mobile tests:

1. Verify number of calculators in total 
2. Verify app title
3. Verify multiplication
4. Verify addition

####Electron tests:

1. Verify number of menu options
2. Verify an element was selected

Drivers needed to be executed before run: <br>
JSON-Server: https://github.com/typicode/json-server <br>
Real World App: https://github.com/cypress-io/cypress-realworld-app
