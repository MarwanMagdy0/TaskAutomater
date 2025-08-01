import random
import string

def random_email():
    domains = ["eo.com", "te.com", "myma.com"]
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    random_domain = random.choice(domains)
    return f"{random_name}@{random_domain}"