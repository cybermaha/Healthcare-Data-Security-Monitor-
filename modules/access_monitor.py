import datetime
from collections import defaultdict

class AccessMonitor:
    def __init__(self, threshold=5, time_window=10):
        self.access_log = defaultdict(list)
        self.THRESHOLD = threshold  # Max allowed accesses per time window
        self.TIME_WINDOW = time_window  # Minutes
        
    def log_access(self, user_id, patient_id, access_type):
        timestamp = datetime.datetime.now()
        self.access_log[user_id].append((timestamp, patient_id, access_type))
        self._check_anomalies(user_id)
    
    def _check_anomalies(self, user_id):
        now = datetime.datetime.now()
        window_start = now - datetime.timedelta(minutes=self.TIME_WINDOW)
        
        # Get accesses within current time window
        recent_accesses = [
            access for access in self.access_log[user_id] 
            if access[0] > window_start
        ]
        
        # Detect suspicious patterns
        if len(recent_accesses) > self.THRESHOLD:
            self._trigger_alert(
                user_id=user_id,
                event="EXCESSIVE_ACCESS_ATTEMPT",
                details=f"{len(recent_accesses)} accesses in {self.TIME_WINDOW} minutes"
            )
        
        # Detect unusual hours (10PM-6AM)
        if any(22 <= access[0].hour or access[0].hour < 6 for access in recent_accesses):
            self._trigger_alert(
                user_id=user_id,
                event="NON_BUSINESS_HOURS_ACCESS",
                details="Access during high-risk hours"
            )
    
    def _trigger_alert(self, user_id, event, details):
        # Placeholder - would connect to alert_system.py
        print(f"ALERT: {event} by {user_id} - {details}")
