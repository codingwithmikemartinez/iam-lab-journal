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
