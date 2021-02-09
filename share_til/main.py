from slack_reminder import Slack
from datetime import datetime

TOKEN = "TOKEN ID"
CHANNEL = "CHANNEL ID"
SENDER_NAME = "NOTINOTI"
TODAY = datetime.today()
YEAR, MONTH, DAY = TODAY.year, TODAY.month, TODAY.day

CONTENTS = f"{YEAR}년 {MONTH}월 {DAY}일 오늘 무엇을 하셨는지 또는 하실 예정인지 간단히 알려주세요."

slack = Slack(token=TOKEN, channel=CHANNEL, username=SENDER_NAME)
slack.send_slack_message(text=CONTENTS)
