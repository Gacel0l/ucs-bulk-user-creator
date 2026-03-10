# ucs-bulk-user-creator

Script for **mass account creation on a UCS (Univention Corporate Server) domain**.

This tool automates the creation of multiple user accounts by sending the same requests that the UCS web interface performs. It is designed to save time in environments where creating many accounts manually through the GUI would be slow and inefficient.

⚠️ **Status:** Beta  
The script works and has been tested, but it is still under development and improvements will be made in the future.

---

# Features

- Bulk user creation
- Uses an authenticated UCS session
- Designed primarily for **school environments** (e.g., creating many student accounts)
- Simple workflow

---

# Requirements

- Python 3
- A valid **UCS web session**
- Access to the UCS admin interface

---

# Setup

Make sure **both scripts are placed in the same folder**:
