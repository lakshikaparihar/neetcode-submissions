class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        champ = -1
        for i in range(len(arr)-1,-1,-1):
            new_champ = max(champ,arr[i])
            arr[i] = champ
            champ = new_champ

        return arr
        