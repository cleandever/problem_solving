"""
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath1(self, path: str) -> str:
        stack = []
        for dir_name in path.split('/'):
            if dir_name == '..':
                if stack:
                    stack.pop()
            elif dir_name and dir_name != '.':
                stack.append(dir_name)
        return '/' + '/'.join(stack)


    def simplifyPath2(self, path: str) -> str:
        # any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'
        path = path.replace('//', '/')

        # The path starts with a single slash '/'
        canonical_path = ['/']

        for dir_name in path.split('/')[1:]:
            if not dir_name:
                continue

            if dir_name == '..':
                if len(canonical_path) > 1:
                    # 마지막의 디렉토리 이름과 '/'를 제거
                    canonical_path = canonical_path[:-2]
            elif dir_name == '.':
                # do nothing
                pass
            else:
                canonical_path.append(dir_name)
                canonical_path.append('/')

        # the path does not end with a trailing '/
        while len(canonical_path) > 1 and canonical_path[-1] == '/':
            canonical_path = canonical_path[:-1]

        return ''.join(canonical_path)



    def simplifyPath(self, path: str) -> str:
        return self.simplifyPath1(path)


sol = Solution()
assert sol.simplifyPath("/home/") == "/home"
assert sol.simplifyPath("/../") == "/"
assert sol.simplifyPath("/home//foo/") == '/home/foo'
