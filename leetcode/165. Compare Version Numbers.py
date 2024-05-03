# https://leetcode.com/problems/compare-version-numbers/?envType=daily-question&envId=2024-05-03

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n_version1 = version1.split('.')
        n_version2 = version2.split('.')

        for v1, v2 in zip_longest(n_version1, n_version2, fillvalue='0'):
            # int를 하면 앞의 0은 사라진다
            v1, v2 = int(v1), int(v2)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        else:
            return 0
