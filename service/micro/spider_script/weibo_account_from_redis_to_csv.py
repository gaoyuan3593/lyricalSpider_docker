
import pandas as pd

from service.db.utils.redis_utils import RedisClient

accounts_db = RedisClient('accounts', "weibo")
accounts = accounts_db.all()

file_name = 'weibo.csv'

data = [
    dict(account=k, password=v)
    for k, v in accounts.items()
]
df = pd.DataFrame(data)

csv_headers = ['account', 'password']
df.to_csv(file_name, header=csv_headers, index=False, encoding='utf-8')
