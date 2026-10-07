class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        return ("").join(result)


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        #print(s)
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            result.append(s[i:j])
            #print(f"current result {result}. current i {i}. current j {j}.")
            i=j

        return result


        """
test case:
5#Hello5#World



        """