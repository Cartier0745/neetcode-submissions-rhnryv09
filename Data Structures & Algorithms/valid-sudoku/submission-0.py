class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictR = {}
        dictC = {}
        dictG = {}
        groupR, groupC = 0,0
        for i in range(len(board)): 
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                dictR[(i,num)] = dictR.get((i,num),0) + 1
                dictC[(j,num)] = dictC.get((j,num),0) + 1 
                if dictR[(i,num)] > 1 or dictC[(j,num)] > 1:
                    print("i,j" + str(i),","+ str(j))
                    return False
                if i<3:
                    groupR = 0
                elif i<6:
                    groupR = 1
                else: groupR = 2
                if j<3:
                     groupC = 0
                elif j<6:
                    groupC = 1
                else: groupC = 2
                dictG[(groupR,groupC, num)] = dictG.get((groupR,groupC,num),0) + 1
                if dictG[(groupR,groupC, num)] > 1:
                        print("i,j" + str(i)+","+ str(j))
                        return False
        return True
