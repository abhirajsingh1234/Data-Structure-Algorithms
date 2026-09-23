class Solution:
    def removeSpaces(self, s):
        chars = list(s)

        j = 0
        for i in range(len(chars)):
            if chars[i] != ' ':
                print(chars)
                chars[j] = chars[i]
                j += 1

        return ''.join(chars[:j])

obj = Solution()
print(obj.removeSpaces('as sa f retgaer ergtw ergs segae e asdrg'))


