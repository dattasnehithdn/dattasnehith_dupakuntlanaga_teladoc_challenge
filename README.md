# dattasnehith_dupakuntlanaga_teladoc_challenge
Code performing the assignment from Teladoc organization for the purpose of Interview

This module returns a list of movie titles from the defined end point by using the substring from the Movie title. By passing the substring to this code, the script will do a API call to the end point with the inputted substring which will return the response in JSON. The code will then parse all the pages, capture the movie titles and sort them before returning it.

Pre-requisites:
python 3.9 or above is installed
pip in installed
Ensure requests (pip install requests) is installed
Install Pycharm Community Edition and open the project

Configurations:
In the Edit configurations, set the "Script path" as project location followed by "\FetchMovieTitles\TestCases\GetTotalTitlesforSubstr.py"
And the Python interpreter as Python 3.9
Save the configuration

Run the Project:
click on Run button
Enter the value of the string which needs to be searched in the API to fetch the Movie titles list.


Troubleshooting:
Ensure Python, pip and requests are installed.
Verify the script path is properly referring to the project and script locations.
Confirm the Python Interpreter is referring to the correct python version.
Make sure script which we are running is: GetTotalTitlesforSubstr.py
Once the script is run, enter the substring for which we want the movie titles list in ascending order in which the inputted title is a substring of.
