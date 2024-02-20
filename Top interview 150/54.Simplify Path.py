class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        stack = []
    # Iterate through the names
        for name in names:
            if name == '..':
            # Pop the top directory from stack (if not empty)
                if stack:
                   stack.pop()
            elif name != '' and name != '.':
            # Push the name onto the stack (if not empty and not '.')
                stack.append(name)
    # Construct the canonical path by popping directories from stack
    # and appending them to the front of the canonical path string
        canonical_path = ''
        while stack:
            canonical_path = '/' + stack.pop() + canonical_path
    # If stack is empty, append a single '/' at the beginning
        if not canonical_path:
            canonical_path = '/'
        return canonical_path