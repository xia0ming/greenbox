import datetime
from random import randint

now = datetime.datetime.now().replace(year=2016)

print(now + datetime.timedelta(days=1, seconds=randint(0, 60), minutes=randint(0, 60), hours=randint(0, 24)))
# os.system()
