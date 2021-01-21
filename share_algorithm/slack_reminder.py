"""
reference. https://dc7303.github.io/python/2019/12/08/pythonMakedCrawler5/
"""

from slacker import Slacker


class Slack(object):
    def __init__(self, token: str, channel: str, username: str):
        self.slack = Slacker(token)
        self.channel = channel
        self.username = username

    def send_slack_message(self, text: str):
        self.slack.chat.post_message(
            channel=self.channel, username=self.username, text=text
        )
