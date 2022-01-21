class BTreeList:
    def __init__(self, value:int, deg:int=5) -> None:
        self.root=BTNode(value=value, deg=deg)
        self.deg=deg
    def searchValue(self, value:int) -> bool:
        (n, f, i)=self.root.searchValue(value)
        return f

    def insertValue(self, value: int):
        (node, isFound, index) = self.root.searchValue(value)
        if node.keys() != node.minKeys():
            newnode = BTNode(value=value, deg=node.deg)
            if len(node.L) == index:
                node.L.append(value)
                node.L.append(None)
                BTNode(L=newnode.L, deg=node.deg)
            else:
                if index == 1:
                    node.L.push(value)
                    node.L.push(None)
                    BTNode(L=newnode.L, deg=node.deg)
def knapsack(items: List[Item], capacity: int):
	table = createKnapsackTable(len(items), capacity)
	for c in range(1, len(items)+1):
		for i in range(1, capacity+1):
			kNo = table[c][i-1]
			if c >= items[i-1][0]:
				kYes = table[c-items[i-1][0]][i-1] + items[i-1][1]
			else:
				kYes = kNo
			if kYes > kNo:
				table[c][i] = kYes
			else:
				table[c][i] = kNo
	return table

class BTNode:
    def __init__(self, value: int= None, L:list=None, deg:int=5, P:BTNode=None):
        if value is not None:
            self.L=[None, value, None]
        else:
            self.L = L
            for item in self.L:
                if type(item) is BTNode: item.P=self
        self.deg = deg
        self.P = P

    def searchValue(self, value:int):
        for index in range(len(self.L)):
            item = self.L[index]
            if type(item) is int:
                lc = self.L[index-1]
                if value == item:
                    return (self, True, index)
                if value < item:
                    if lc is not None: return lc.searchValue(value)
                    else: return (self, False, index)
        rc = self.L[len(self.L)-1]
        if rc is not None: return rc.searchValue(value)
        else: return (self, False, len(self.L))
    def keys(self):
        return int((len(self.L)-1)/2)
    def minKeys(self):
        return ceil((self.deg-1)/2)