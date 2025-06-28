class ComplianceChecker:
    HIPAA_REQUIREMENTS = [
        'data_encryption_at_rest',
        'access_controls',
        'audit_logs',
        'backup_procedure'
    ]
    
    def verify_environment(self, config):
        missing = []
        for requirement in self.HIPAA_REQUIREMENTS:
            if not config.get(requirement, False):
                missing.append(requirement)
        
        if missing:
            return {
                "compliant": False,
                "missing": missing
            }
        return {"compliant": True}
