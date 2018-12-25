# Googletestpy

This is project for testing google homepage using Selenium and Python on Mac .

Following tests are performed

1.The Google logo image is present.
2.The Search text field is present.
3. The Google Search button is present. 
4.Clicking the ‘Google Search’ button with no search text will not perform a search.
5.Search text may be entered into the Search text field
6.Clicking the ‘Google Search’ button with search text yields search results. 

Requirements: - 

Install Homebrew(For installing dependencies) – Add this to command line(without quotes) “ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
You will be asked for password.


Once Homebrew is installed following dependencies needs to be installed

1.	Git -- brew install git
2.	Python 2.7 -- brew install python@2
Add python to the path -- export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"

3.	Java -- brew cask install java
4.	Allure -- brew install allure
5.	Behave -- pip install behave
6.	Allure-behave -- pip install allure-behave
7.	Selenium -- pip install selenium


To run the Project
1.	Go to terminal in Pycharm
2.	Add this to command line (without quotes) and execute --  “behave -f allure_behave.formatter:AllureFormatter -o ./Reports ./src/feature”
3.	The project will run and show log statements in the terminal.
4.	For Allure report, run the command (without quotes) – “allure serve ./Reports”
5.	Once the report is generated the default browser will open with the report.
6.	To change the browser for the Selenium driver to open – Goto behave.ini and change from “firefox” to “chrome” or vice versa
7.	In the Allure report – Click on Suites to see the test cases executed.

I have used behave as BDD and allure to generate reports

Note –
1.	Chrome has issues running in maximize mode – Added a workaround for that which meant I had to hardcode screen size.
2.	Google homepage Logo changes i.e. either it is Google logo or Google Doodle. I have added code for logo encapsulated in try/catch. If there is a change the step might fail.
3.	Added explicit wait times in few conditions if the search results are shown slowly.
4.	Safari to be automated needs developer certificates hence just added Chrome and Firefox.
