import tweepy
import schedule
import time
import datetime

CK = 
CS =
AT =
AS = 


auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)
m = str(datetime.datetime.now().month)
d = str(datetime.datetime.now().day)

def tweet():
        api.update_status('おはようございます。\r\n今日は' + str(m) + '月' + str(d) + '日です.')#ツイートしたいテキスト
def job():
    if d == str(26):
        print('if')
        tweet()
    else:
        print('else')
schedule.every().day.at("21:27").do(job)#指定時刻
while True:
                    schedule.run_pending()
                    time.sleep(1)
