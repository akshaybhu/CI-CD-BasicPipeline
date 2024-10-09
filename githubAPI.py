import requests
import json, os, subprocess

owner = "akshaybhu"
repo_name = "CI-CD-BasicPipeline"

def call_bash():
    result = subprocess.run([ '/usr/bin/bash', '/home/ec2-user/bash-git_update.sh' ], capture_output=True, text=True)
    #print(result.stdout)
    #print(result.stderr)

response = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/commits")
#print(response.status_code)
commit = response.json()
#print(json.dumps(commit[0], indent=4))
latest_commit = commit[0]["sha"]

print(latest_commit)

#response1 = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/commits/{latest_commit}")
#print(response1.json())

if os.path.exists("commit_file.txt"):
    with open("commit_file.txt") as f:
        old_commit = f.read().strip()
        if latest_commit == old_commit:
            print("we have no update, lets check in 5mins..")
        else:
            with open("commit_file.txt", "w") as f:
                f.write(latest_commit)
                print("We have new commit available, pushing with bash to deploy new chnages now!!")
                call_bash()
                print("Process completed")
else:
    with open("commit_file.txt", "w") as f:
        f.write(latest_commit)
        print("This is first run, current commit is stored now")
        call_bash()
        print("Process completed")
