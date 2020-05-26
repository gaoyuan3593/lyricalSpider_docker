import pytz
from pymongo import MongoClient
import pickle
import time
import datetime
import pytz

EPOCH = 1970
_EPOCH_ORD = datetime.date(EPOCH, 1, 1).toordinal()

tz = pytz.timezone('Asia/Shanghai')


def timegm(tuple):
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    year, month, day, hour, minute, second = tuple[:6]
    days = datetime.date(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
    hours = days*24 + hour
    minutes = hours*60 + minute
    seconds = minutes*60 + second
    return seconds


print(time.time())
client = MongoClient('localhost', 27017)
collection = client.apscheduler.jobs
for post in collection.find({"_id":"765edbe9233dab19c3ea7ef21ad8f45e"}):#.limit(12):
    #print('id: ',post['_id'],'next_run_time: ',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(post['next_run_time'])))
    #print('job detail: ', pickle.loads(post['job_state']))
    #tz = datetime.datetime.now(tz)
    next_ = post["next_run_time"]
    _id = post.get("_id")
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(next_))
    _time = datetime.datetime.now(tz) + datetime.timedelta(minutes=3)
    _da = timegm(_time.utctimetuple()) + _time.microsecond / 1000000
    data = pickle.loads(post['job_state'])
    data.update(next_run_time=_time)
    post.update(job_state=pickle.dumps(data))
    post.update(next_run_time=_da)
    collection.save(post)
client.close()