import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email_to_check = "cnr-@capital.cloud"
if is_valid_email(email_to_check):
    print(f"{email_to_check} valid.")
else:
    print(f"{email_to_check} non valid.")
