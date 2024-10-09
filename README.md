# CI-CD-BasicPipeline

# Step 1

Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository. 
a. Used simple project that we have created for adding/updating/deleting tasks.

Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx

a. I installed python and pip using yum, also added venv to install few libraries
b. installed cronie to use crontab
c. Created crontab to run every 5mins for python script.
d. Used yum install for nginx
e. Started nginx and verified status

Cron job configured is below

*/5 * * * * /usr/bin/python3 /home/ec2-user/github-api-code.py >> /home/ec2-user/my_script.log 2>&1

Task 3: Write a Python Script to Check for New Commits
 Create a Python script to check for new commits using the GitHub API.
 
Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.

Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.

Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 
