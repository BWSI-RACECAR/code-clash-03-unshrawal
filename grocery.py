class Solution:
    def my_grocery_list(self,str1,str2):
        # type str1:string
        # type str2: string
        # return: list

        # TODO: Write code below to return a list with the solution to the prompt
        l1 = str1.split(" ")
        l2 = str2.split(" ")
        l3 = []
        for i in l1:
            if i not in l3 and i != "":
                l3.append(i)
        for i in l2:
            if i not in l3 and i != "":
                l3.append(i)
        return l3
        pass

def main():
    string1 = input().strip()
    string2 = input().strip()

    tc1 = Solution()
    ans = tc1.my_grocery_list(string1,string2)
    print(ans)

if __name__ == "__main__":
     main()
