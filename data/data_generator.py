import os.path
import string
import random
import jsonpickle

def random_data(maxlen):
    symbols = string.ascii_letters + string.digits
    random_name_from = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    random_name_to = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    random_email_from = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))]) + '@' + 'mail.ru'
    random_email_to = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))]) + '@' + 'mail.ru'
    return {'random_name_from':random_name_from, 'random_email_from':random_email_from,
            'random_name_to':random_name_to, 'random_email_to':random_email_to}

testdata = [
    random_data(7) for i in range(5)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))