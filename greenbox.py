import datetime
import os
from random import randint

now = datetime.datetime.now()
start = now.replace(year=2016)


def change_time():
    return datetime.timedelta(days=1, seconds=randint(0, 60), minutes=randint(0, 60), hours=randint(0, 24))


commit_date = (start + change_time())
times = randint(1, 3)

# while commit_date < now:
with open('data.txt', 'a+') as f:
    for i in range(times):
        commit_date = commit_date + change_time()
        f.writelines(commit_date.isoformat())
        os.system('git add .')
        os.system('git commit --date={time} -m "Update {time}"'.format(time=commit_date.isoformat()))

# os.system()
