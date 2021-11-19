# QA_candidate_task
This home assignment is for a QA position at Cymptom.
This assignment has two sections:
* Writing a manual testing STD (Software Test Description) file for a feature in cymptom product.
* Writing a basic automated test suit with python and pytest for some simple python code.

The task should be submitted by mail. The code part can be submitted by a git hub repo or a zip file.

**Please don't fork this repo!**

## Part A - Test scenarios

### Writing an STD file
A test scenario is a use case that defines the functionality that can be tested. 
As a tester, you should consider in your tests real-world scenarios as part of the end user's workflow.

Your goal in this section is to write test scenarios for the Cymptom system Issue’s screen.
You will receive as part of the task email, a URL address for our test environment and a user and password for logging in.
Please keep the logging information to yourself!

Your user is an unprivileged "viewer" user. That means it shouldn't be allowed to change anything in the website.
To open the issue screen please log in to the URL provided, and go to the issue screen (marked as a triangle with an 
exclamation mark on the sidebar)

![image](https://user-images.githubusercontent.com/92513421/142606033-5d2287fc-eb3d-4b4a-9423-9f7186273f4b.png)


There are two main features we want you to write tests for:
* Issue Actions
![image-20211114-090623](https://user-images.githubusercontent.com/92513421/142605690-9068636d-2dc7-4a9b-8506-6bc63e7de962.png)

* Issue display grouping
![image-20211114-090815](https://user-images.githubusercontent.com/92513421/142605785-40447be9-6729-479b-8c88-26b1930d9c53.png)

Your task is to map out test steps for these features by yourself! 
Your end goal here will be to provide an STD file which you can send back by mail.

If you are unsure of what any part of these features does, try to guess.
Write down any assumptions you made on unclear parts of the features at the end of the STD file.

In your test scenarios, you should verify all components perform the way they should, both together and separately!
Also, please keep in mind there are two kinds of users for this system, `admin` and `viewer`.
**You should write tests for these features for both users!**
Some actions are possible for one user and should be disabled for another.
You should receive a viewer user with this assignment. 
With it, you could run part of your tests and write their results.

**It's ok to guess how should the viewer user work and what limitations it has by yourself!**
as long as you write down any assumption you make if it's not clear from the test step or expected results.

The table below is an example of an STD file and will be your template for this section. Each row is a test step.
In each step please make sure to fill in:
* What results are expected
* What was the actual result 
* If the test failed, please indicate what bugs you found and include screenshots.

### Example STD file
| Test Case ID | Test Scenario | Test Steps | Expected Results | Pass/Fail | Bugs |
| ----------- | ----------- | ----------- |----------- |----------- |----------- |
| 1 | Login with correct user and password | <ol><li>Insert user</li><li>Insert password</li><li>Click login button</li></ol> | Page should be navigate to the Dashboard
| 2 |  |
| 3 |  |

## Part B - Automation
This section is aimed to test your ability to write a simple test suit for a simple python code.
The runner you will need for running these tests is pytest.

### Setup
* install python (we use version 3.7)
* install requirements file `pip install -r requirements.txt`

### Task

1) Take a look at the calculator class in `calc.py`. Now, look at the test for that class in `test_calc.py`.
look at the test file there, can you fill in the purpose of the last two tests?
2) Now try to run the test with pytest. What happened? Can you fix the test so it will pass?
3) can you add tests for the rest of the calculator functions?
5) Take a look at the counter function in `counter.py`.
What does it do? can you update the docstring for that function to have the correct explanation?
6) Take a look at `test_counter.py`. Can you add a few tests for `counter.py` there?


## Assignment Submission
As described before, by an email containing the STD file and a zip file or a GitHub repo containing the code for section two.