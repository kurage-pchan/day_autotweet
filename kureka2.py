import tweepy
import schedule
import time
import datetime

CK = "o4HQvi7D0fkPI6zHFJaRztdyK"
CS = "Uhptvl5WFmiGJdQ15yoTWlP4zyGyeY46QBauvLZNBpVKICObDA"
AT = "1344572902994104322-gddLXqVqRNUayLiiI9aRxX3k9MV1Cq"
AS = "IC0BscOP1zhY7YUuyBaey31tzZG8F94l45fkxCXbgmQpQ"

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)
m = datetime.datetime.now().month
d = datetime.datetime.now().day
def tweet():
    api.update_status('おはようございます。\r\n今日は' + str(m) + '月' + str(d) + '日です')#ツイートしたいテキスト

schedule.every().day.at("16:37").do(tweet)#指定時刻
while True:
            schedule.run_pending()
            time.sleep(1)