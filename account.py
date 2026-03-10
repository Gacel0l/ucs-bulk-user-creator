import requests
import json
debug = False
UMC_SESSION_ID     = "8c91f3e4-2bfc-42ee-ad8f-cd44a343ee55"   # ← Paste Heare Value From Your Brosware
X_XSRF_TOKEN       = UMC_SESSION_ID

BASE_URL = "http://10.113.109.73/"  # CONFIGURATE
SCHOOL   = "spbaboszewo" # CONFIGURATE
CLASS = "spbaboszewo-4b" #REMEMBER TO CHCECK AND USE VALID VALUE


def main(username, first_name, last_name, password):


    if not all([username, first_name, last_name, password]):
        print("All values are required!")
        return

    payload = {
        "options": [{
            "object": {
                "school": SCHOOL,
                "type": "student",
                "schools": [],
                "ucsschool_roles": [],
                "firstname": first_name,
                "disabled": False,
                "birthday": None,
                "expiration_date": None,
                "lastname": last_name,
                "name": username,
                "school_classes": {SCHOOL: [CLASS]},
                "email": "",
                "legal_wards": [],
                "legal_guardians": [],
                "password": password
            },
            "options": None
        }],
        "flavor": "schoolwizards/users"
    }

    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json",
        "X-XSRF-Protection": X_XSRF_TOKEN,
    }

    cookies = {
        "UMCSessionId": UMC_SESSION_ID,
        "UMCLang": "en-US",
    }

    url = f"{BASE_URL}/univention/command/schoolwizards/users/add"
    if debug:
        print(f"\nSending → {url}")

    try:
        r = requests.post(
            url,
            json=payload,
            headers=headers,
            cookies=cookies,
            timeout=12
        )
        if debug:
            print(f"\nStatus: {r.status_code}")

        if r.status_code in (200, 201, 204):
            print("\n=== SUCCESS ===")
            if debug:
                try:
                    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
                except:
                    print("not a JSON →", r.text[:600])
        else:
            print("\nServer Error:")
            print(r.text[:1400])
            if r.status_code == 401:
                print("\nMost likely the session has expired → log in again in the solution and get a fresh UMCSessionId")

    except Exception as e:
        print(f"\nConnecton Error: {e}")

