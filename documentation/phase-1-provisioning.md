# Entry 01: Provisioning & Hardening the Root Node
**Date:** April 12, 2026  
**Role:** IAM Lab Architect  
**Status:** Phase 1 Complete (System Initialized)

---

## Executive Summary
The objective of this phase was to provision a headless Linux environment to serve as a testing ground for automated identity lifecycles and **RBAC (Role-Based Access Control)** simulations. The environment was built on a Raspberry Pi 4 running Ubuntu Server 24.04 LTS.

## Technical Implementation
* **Imaging:** Utilized Raspberry Pi Imager to flash Ubuntu Server. Pre-configured the primary administrative identity (`mikeiamadmin`) and enabled SSH to ensure a secure, headless initial handshake.
* **Infrastructure Hardening:** Immediately upon successful authentication, I implemented a host-based firewall using **UFW**.
    * *Action:* Set default deny-all policy.
    * *Action:* Explicitly allowed Port 22/TCP to maintain encrypted administrative access.
* **Process Auditing:** During initial package installation, encountered a resource lock (`/var/lib/dpkg/lock-frontend`).
    * *Troubleshooting:* Used `ps aux | grep unattended-upgr` to identify that the system was performing automated security patching.
    * *Decision:* Allowed the automated integrity check to complete rather than forcing a process kill, ensuring a stable system state.

## Lessons Learned & IAM Insights
* **Identity vs. Hostname:** A brief authentication failure occurred when attempting to use the server's hostname as the UID. This reinforced the importance of precise attribute mapping during the SSH handshake.
* **System Integrity:** Before decommissioning the session due to external environmental factors (weather/power risk), I performed a manual audit of active processes to ensure no data corruption would occur during the shutdown sequence.

## Commands Mastered
* `ssh [User]@[IP]` — Remote Secure Access.
* `sudo ufw allow ssh / enable` — Perimeter Defense.
* `ps aux` — System Process Auditing.
* `hostnamectl` — System Identity Verification.
