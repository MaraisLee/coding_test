# https://leetcode.com/problems/group-anagrams/description/
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램은 알파벳순서로 정렬시 같아짐
        anagrams = {}
        for i in strs:
            # 하나의 키를 만들어주고
            key = tuple(sorted(i))
    
            if key not in anagrams:
                anagrams[key] = []
            # 키에 해당하는 애너그램들을 넣기
            anagrams[key].append(i)
        # 값들만 빼서 리스트로
        return list(anagrams.values())
