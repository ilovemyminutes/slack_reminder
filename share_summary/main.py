from slack_reminder import Slack
from datetime import datetime

TOKEN = 'xoxb-1630254642305-1660700008340-aIYRhxMZzbMmIEB4uBL6WoWs'
CHANNEL = 'C01JVVA1TC6'
SENDER_NAME = 'NOTINOTI'
TODAY = datetime.today()
YEAR, MONTH, DAY = TODAY.year, TODAY.month, TODAY.day

CONTENTS = f'[{YEAR}년 {MONTH}월 {DAY}일 피어세션] 전날 학습 정리를 답글로 달아주세요.'

slack = Slack(token=TOKEN, channel=CHANNEL, username=SENDER_NAME)
slack.send_slack_message(text=CONTENTS)