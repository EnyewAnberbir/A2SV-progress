class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        maps = {}
        
        for path in paths:
            files = path.split(' ')
            
            directory = files[0]
            for file in files[1:]:
                Information = file.split('(')
                asssignedName = Information[0]
                content = Information[1][:-1]
                
                file_path = directory + '/' + asssignedName
                
                if content not in maps:
                    maps[content] = []
                
                maps[content].append(file_path)
        
        return [paths for paths in maps.values() if len(paths) > 1]
