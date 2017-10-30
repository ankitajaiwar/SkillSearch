# SkillSearch
A web app to search skilled people within your university or college campus. Here you can create your own user account, Add skills to your Account, Evaluate your skills and get a score and search people with particular skillset.   

### WebApp Front-end: 
Used a combination of Bootstap CDN and HTML 5 / CSS 5.

### WebApp Back-end: 
Used the Python based Flask framework, with pyhton support classes and MongoDB Database. 

### Location of Source codes: 
Check the "Final Version Iteration_1" folder for full source code developed as part of Iteration 1.


## Pre-requisites: 
1. A Running MongoDB instance in your machine.
If you are not familiar how to do this, refer this stackoverflow link => https://stackoverflow.com/questions/20796714/how-do-i-start-mongo-db-from-windows

2. A basic Command Prommpt(in case of Windows) or Terminal(Linux users). If you are not planning to use any of these, you need a Python IDE like PyCharm. Thats where this app is being developed and tested. 


## Run Instructions:
This Project can be run in three ways:
1. Make sure there is an active MongoDB instance, irrespective of the way you are choosing below.
_(Note: No need to configure MongoDB in the app, if the mongodb settings are left default.  The defaults values are pid=9444 port=27017. If there is a custom setting, change common\database\Database.py with appropriate  settings)_

### Using Makefile:
1. There is a zip file named EasyLaunch_Makefile.zip, extract it and then open the location of extracted folder in CMD prompt(if Windows) or in Terminal(if Linux).

2. Run the command `Scripts\activate`. You should see the "(software_eng)" tag on left side of cursor. 

3. Make sure you have make installed in the system and added to Environment variable PATH. 

4. Run the command make or mingw32-make or gnu-make depending upon the kind of make you have configured in your system. This will run two unnittests first then launch the app. You should be seeing the Test results and App launch messages at the end of execution. 
Then copy the local host address mentioned at the bottom and paste it in browser, to launch the app. 

### Using CMD prompt / Terminal:(without using makefile)
1. There is a zip file named EasyLaunch_Makefile.zip, extract it and open the location of extracted in CMD prompt(if Windows) or in Terminal(if Linux).

2. Go into the Scripts directory.

3. Run the command `activate`. You should see the "(software_eng)" tag on left side of cursor.

4. Then, run the command (without quotes) `'python Final_Version_Iteration_1\src\app.py'` 
You should the local instance address on which app is running. Something like http://127.0.0.1:4995/
Go to the address to access the web app. 

5. To run the two Unittests, execute below commands 
```
python -m unittest Scripts\Final_Version_Iteration_1\src\test.py
python -m unittest Scripts\Final_Version_Iteration_1\src\test_ui.py
```
To teardown test data, please execute below:
```
python Final_Version_Iteration_1\src\clean.py
```
_(Note) Make sure to run the test.py unittest before running test_ui.py as test_ui.py uses test entries of test.py_

### Using PyCharm IDE:
1. If you are using PyCharm IDE, Load the project files "Iteration2_Final_Version" and Make src/ folder as root folder(Right click -> MakeDirectoryas >).

2. Go to File -> Settings -> Project  Interpreter -> Click settings icon at the rightmost -> Create a new Virtual env -> finish creating env. 

3. Install all libraries as mentioned in requirements.txt (present under Project root folder)

4. Once all libraries are installed and no squiggly lines in code, execute app.py to launch the server. go to the localhost address as shown in console bottom (http://127.0.0.1:4995/).

5. To run unittests, run the test.py and test_ui.py. Then do clean.py for cleaning test data.

_(Note) Make sure to run the test.py unittest before running test_ui.py as test_ui.py uses test entries of test.py_



## Unit-test Run:
* To run unit tests please refer above Run Instructions. 
* (Note) The deprecation warnings on running the test_ui.py can be ignored.
* __(Note) Make sure to run the test.py unittest before running test_ui.py as test_ui.py uses test entries of test.py__



## Inputs and Outputs: (Acceptance criteria for Iteration 2)
1. Once you see the App main page, You can click Register. (since you don't have an account yet).

2. Complete Registration form and click 'Submit'. You should see a "Registered Successfully" message in next Page.  

3. From there, You can choose to go to 'User-Home' page or Try out your new credentials in 'Login-Page'

4. Once you are in User-Home, click either 'Add Skills' or 'Search People'

5. 'Add Skills' will redirect you to a page, where you can choose a pre-defined set of skills(drop-down) or choose a custom skill and click 'Submit'

6. 'Search People' will redirect you to a page, where you can select one or more skills and get a list of people matched with the database. 

7. Once you done, you can click logout. If you don't logout, your session will be saved and maintained for future logins(no need repetitive logins).