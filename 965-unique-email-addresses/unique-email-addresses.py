class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email:set[str]=set()
        for email in emails:
            local_name,domain_name=email.split('@')
            local_name=local_name.split('+')[0]
            local_name=local_name.replace('.','')
            email=local_name+'@'+domain_name
            unique_email.add(email)
        return len(unique_email)