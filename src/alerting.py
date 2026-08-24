import smtplib
import json
import urllib.request

class AlertManager:
    def __init__(self):
        self.rules = []
        self.alert_history = []

    def add_rule(self, metric, threshold, action):
        self.rules.append({"metric": metric, "threshold": threshold, "action": action})

    def check_rules(self, current_metrics):
        for rule in self.rules:
            if current_metrics.get(rule['metric'], 0) > rule['threshold']:
                self.alert_history.append(f"Alert: {rule['metric']} exceeded {rule['threshold']}")

    def send_email_alert(self, to, subject, body):
        pass # mock

    def send_webhook(self, url, payload):
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req)

    def send_slack_alert(self, webhook_url, message):
        self.send_webhook(webhook_url, {"text": message})
