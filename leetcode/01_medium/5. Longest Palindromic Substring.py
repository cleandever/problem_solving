class Solution:
    def longestPalindrome(self, s):
        def get_palindrome(left, right):
            # 왼쪽, 오른쪽으로 이동하면서 회문을 탐색
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ''
        for i in range(len(s)):
            # odd
            palindrome = get_palindrome(i, i)
            if len(longest_palindrome) < len(palindrome):
                longest_palindrome = palindrome

            # even
            palindrome = get_palindrome(i, i + 1)
            if len(longest_palindrome) < len(palindrome):
                longest_palindrome = palindrome

        return longest_palindrome

sol = Solution()
ret = sol.longestPalindrome("babad")
assert ret == "bab"