class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        
        
        for cpdomain in cpdomains:
           
            count, domain = cpdomain.split(' ')
            count = int(count)
            
            
            partdomains = domain.split('.')
            
           
            for i in range(len(partdomains)):
                partdomain = '.'.join(partdomains[i:])
                
                
                if partdomain in domains:
                    domains[partdomain] += count
                else:
                    domains[partdomain] = count
        result = []
        for domain, count in domains.items():
            result.append(str(count) + ' ' + domain)
        
        return result
