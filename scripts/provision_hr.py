import subprocess

# Define our variables
group = "hr"
user = "hr_specialist"

# Tell Python to execute the Linux commands
subprocess.run(["sudo", "groupadd", group])
subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", user])
subprocess.run(["sudo", "usermod", "-aG", group, user])

print(f"Successfully provisioned {user} into the {group} group.")
