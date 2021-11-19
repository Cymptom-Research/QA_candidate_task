# QA_candidate_task
This home assignment for a QA position at Cymptom.
This assignment has two sections:
* Writing a manual testing STD (Software Test Description) file for a feature in cymptom product.
* Writing a basic automated test suit with python and pytest for some simple python code.

The task should be submitted by mail. The code part can be submitted by a git hub repo or a zip file.

###**Please Don't fork this repo!**

## Part A - Test scenarios

### Writing an STD file
A test scenario is a use case that defines the functionality that can be tested. 
As a tester, you should consider in your tests real-world scenarios as part of the end-user's workflow.

Your goal in this section is to write test scenarios for the Cymptom system Issue’s screen.
You will receive as part of the task email, an url address for our test environment and a user and password for logging in.
Pleas keep the logging information to yourself!

Your user is an unprivileged "viewer" user. That means it shouldn't be allowed to change anything in the website.
There are two main features we want you to write tests for:
* Issue Actions
* Issue display grouping
* 

## Part B - Automation
This section is aimed to test your ability to write a simple test suit for a simple python code.
The runner you will need for running these test is pytest.

### Setup
* install python (we use version 3.7)
* install requirements file `pip install -r requirements.txt`

### Task

1) Take a look at the calculator class in `calc.py`. Now look at the test for that class in `test_calc.py`.
look at the test file there, can you fill in the purpose of the last two tests?
2) Now try to run the test with pytest. What happened? Can you fix the test so it will pass?
3) can you add tests for the rest of the calculator functions?
5) Take a look at counter function in `counter.py`.
What does it do? can you update the docstring for that function to have the correct explanation?
6) Take a look at `test_counter.py`. Can you add a few tests for `counter.py` there?



