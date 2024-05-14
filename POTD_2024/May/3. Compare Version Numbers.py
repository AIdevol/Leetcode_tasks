class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Get the maximum length to iterate up to
        max_length = max(len(v1), len(v2))
        
        for i in range(max_length):
            # Convert the current revision of each version to integer, if it exists, otherwise 0
            revision1 = int(v1[i]) if i < len(v1) else 0
            revision2 = int(v2[i]) if i < len(v2) else 0
            
            # Compare the revisions
            if revision1 > revision2:
                return 1
            elif revision1 < revision2:
                return -1
        
        # If all revisions are equal
        return 0
