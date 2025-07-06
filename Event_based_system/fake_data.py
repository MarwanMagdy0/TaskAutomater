import random
import string

def random_email():
    domains = ["example.com", "testmail.com", "mymail.com"]
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_domain = random.choice(domains)
    return f"{random_name}@{random_domain}"