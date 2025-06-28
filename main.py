from modules.access_monitor import AccessMonitor
from modules.phi_scanner import PHIScanner
from modules.compliance_check import ComplianceChecker
from modules.alert_system import AlertSystem
import config

def main():
    # Initialize components
    monitor = AccessMonitor(threshold=5, time_window=10)
    scanner = PHIScanner()
    hipaa_check = ComplianceChecker()
    alerter = AlertSystem(
        smtp_server=config.SMTP_SERVER,
        port=config.SMTP_PORT,
        sender=config.EMAIL_USER,
        password=config.EMAIL_PASS
    )
    
    # Simulate access monitoring
    monitor.log_access("nurse_jane", "patient_12345", "medical_records")
    
    # PHI scan on sample file
    scan_result = scanner.scan_file("patient_data/sample_report.txt")
    if scan_result:
        alerter.send_alert(
            recipient="security_team@hospital.com",
            subject="PHI Exposure Detected",
            body=f"Found sensitive data: {scan_result}"
        )
    
    # Compliance check
    compliance_status = hipaa_check.verify_environment(config.SECURITY_SETTINGS)
    if not compliance_status["compliant"]:
        print(f"Compliance issues: {compliance_status['missing']}")

if __name__ == "__main__":
    main()
