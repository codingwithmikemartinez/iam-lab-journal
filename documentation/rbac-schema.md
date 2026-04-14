# Martinez FinTech: RBAC Governance Plan

## Objective
To implement a strict Role-Based Access Control (RBAC) model on a Linux-based system, ensuring the Principle of Least Privilege (PoLP) is maintained across all departments.

## Departmental Mapping
| Department | Group Name | Access Level | Directory |
| :--- | :--- | :--- | :--- |
| Finance | `finance` | Read/Execute | `/data/finance` |
| HR | `hr` | Read/Execute | `/data/hr` |
| Engineering | `sudo` | Full Admin | System-wide |

## Security Controls
1. **No Shared Accounts:** Every user has a unique UID.
2. **Directory Hardening:** Folders will be set to `750` permissions to prevent unauthorized lateral movement between departments.
3. **Shell Restriction:** Standard users are restricted to `/bin/bash` with no global sudoers privileges.

## Implementation Guide (Technical SOP)

### 1. Group Provisioning
Establish the departmental security boundaries:
`sudo groupadd finance`
`sudo groupadd hr`

### 2. User Provisioning & Identity Mapping
Create specific identities with home directories and standard bash shells:
`sudo useradd -m -s /bin/bash f_analyst`
`sudo useradd -m -s /bin/bash hr_specialist`

### 3. Access Granting (RBAC Assignment)
Assign users to their respective security groups:
`sudo usermod -aG finance f_analyst`
`sudo usermod -aG hr hr_specialist`

### 4. Filesystem Permission Hardening
Set directory ownership and restrict access to the group (750):
`sudo chown :finance /data/finance`
`sudo chmod 750 /data/finance`
