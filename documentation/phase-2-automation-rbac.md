# Entry 02: Phase 2 — Automated Provisioning & RBAC Design

**Date:** April 18, 2026  
**Role:** IAM Automation Engineer  
**Status:** Phase 2 Active (Identity Lifecycle Management)

---

### Executive Summary
The goal of this entry was to move away from creating users one-by-one and start building a **Scalable Identity Lifecycle**. I designed a basic RBAC (Role-Based Access Control) structure for different departments and built a Python tool to handle the "heavy lifting" of adding users to the system without manual typos or errors.

### Technical Implementation
* **RBAC Design:** Set up specific security groups (`finance` and `hr`) on the Raspberry Pi to simulate how a real company separates access.
* **Automation Tool:** Created a Python script using the `subprocess` module to bridge the gap between code and the Linux OS.
    * **Logic:** The script executes system-level commands to create a user account and immediately lock them into their assigned departmental group.
* **Verification & Auditing (The "Trust but Verify" Phase):**
    * **Identity Check:** Used the `id` command to verify that the UID and GIDs were assigned correctly for each new user.
    * **System Audit:** Manually audited the `/etc/group` file to ensure the new identities were properly mapped to their departmental silos.
    * **Directory Audit:** Used `ls -la` to confirm that the system successfully provisioned home directories with the correct ownership permissions.

### Lessons Learned & IAM Insights
* **Wrestling with Python:** Moving from simple Bash commands to Python logic was a jump. I realized I don't need to write the whole script in one go. Breaking the problem down into small, **"win-the-moment"** steps—like just getting the user created before worrying about the groups—made it much easier to handle.
* **The "What If" Factor:** Building this manually taught me that I’m the "safety net." When I started scripting, I realized the *code* needs its own safety net. I learned to think about things like: *"What if this user already exists?"* and adding checks to keep the script from crashing.
* **Trust but Verify:** I learned that automation is only as good as the audit that follows it. Even though my script said "Success," I didn't truly believe it until I went into the `/etc/group` file and saw the names listed under the correct GIDs. In IAM, if you didn't verify it, it didn't happen.
* **Efficiency vs. Accuracy:** Automation is fast, but it’s also fast at making mistakes if you don't double-check your group logic first. I spent more time verifying the Linux group IDs than I did actually typing the code.

### Commands & Tools Mastered
* **`python3`** — Executing the automation engine and testing logic.
* **`subprocess` (Python Module)** — The bridge used to make Python talk to the Linux Kernel.
* **`groupadd` / `useradd`** — Core Identity Lifecycle commands for provisioning.
* **`cd` / `ls -la`** — Navigating the file system and auditing hidden file permissions.
* **`cat /etc/group`** — Directly auditing the system's group database to verify RBAC mapping.
* **`nano`** — CLI-based text editing for script development on the fly.
* **`id [username]`** — Instant identity verification to check UID/GID alignment.
