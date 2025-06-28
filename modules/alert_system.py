import smtplib
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self, smtp_server, port, sender, password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender = sender
        self.password = password
    
    def send_alert(self, recipient, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = f"SECURITY ALERT: {subject}"
        msg['From'] = self.sender
        msg['To'] = recipient
        
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
                server.login(self.sender, self.password)
                server.sendmail(self.sender, recipient, msg.as_string())
            return True
        except Exception as e:
            print(f"Alert failed: {str(e)}")
            return False
