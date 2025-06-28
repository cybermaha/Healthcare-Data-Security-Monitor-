import re
from pathlib import Path

class PHIScanner:
    PHI_PATTERNS = {
        'SSN': r'\b\d{3}-\d{2}-\d{4}\b',
        'MEDICARE': r'\b[A-Z]\d{9}\b',
        'PHONE': r'\b\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
        'EMAIL': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    }
    
    def scan_file(self, file_path):
        results = {}
        try:
            content = Path(file_path).read_text()
            for phi_type, pattern in self.PHI_PATTERNS.items():
                matches = re.findall(pattern, content)
                if matches:
                    results[phi_type] = len(matches)
        except Exception as e:
            print(f"Scan error: {str(e)}")
        return results
