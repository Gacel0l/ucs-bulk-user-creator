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


Before running the bulk script, you must configure **`account.py`**.

### 1. Edit `account.py`

Open `account.py` and set the required parameters.

You **must paste your UCS session cookie** from your browser after logging into the UCS web interface.

Example workflow:

1. Log in to the **UCS web interface** in your browser.
2. Open **Developer Tools → Application/Storage → Cookies**.
3. Copy the **session cookie value**.
4. Paste it into the appropriate variable inside `account.py`.

---

# Usage

Once the configuration is complete, run the bulk script:

```bash
python account-bulk-create.py
