import tweepy
import schedule
import time
import datetime

CK = ""
CS = ""
AT = ""
AS = ""

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)
m = datetime.datetime.now().month
d = datetime.datetime.now().day
def tweet():
    api.update_status('おはようございます。\r\n今日は' + str(m) + '月' + str(d) + '日です')#ツイートしたいテキスト

schedule.every().day.at("06:00").do(tweet)#指定時刻
while True:
            schedule.run_pending()
            time.sleep(1)