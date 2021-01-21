from slack_reminder import Slack
from datetime import datetime

TOKEN = "TOKEN ID"
CHANNEL = "CHANNEL ID"
SENDER_NAME = "NOTINOTI"
TODAY = datetime.today()
YEAR, MONTH, DAY = TODAY.year, TODAY.month, TODAY.day

CONTENTS = f"[{YEAR}년 {MONTH}월 {DAY}일 피어세션] 주말 동안 풀이하신 알고리즘 코드를 답글로 달아주세요."

slack = Slack(token=TOKEN, channel=CHANNEL, username=SENDER_NAME)
slack.send_slack_message(text=CONTENTS)
