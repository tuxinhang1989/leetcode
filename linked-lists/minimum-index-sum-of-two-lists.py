class Trie(object):
    def __init__(self):
        self.children = {}
        self.index = None
        self.end = False

    def insert(self, index, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True
        node.index = index

    def find(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        if not node.end:
            return None
        return node.index


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if len(list1) < len(list2):
            return self.findRestaurant(list2, list1)
        root = Trie()
        for index, word in enumerate(list1):
            root.insert(index, word)

        sum_index = []
        res = []
        for i, word in enumerate(list2):
            j = root.find(word)
            if j is None:
                continue
                
            if not res:
                sum_index.append(i+j)
                res.append(i)
            elif sum_index[0] == i+j:
                sum_index.append(i+j)
                res.append(i)
            elif sum_index[0] > i+j:
                sum_index = [i+j]
                res = [i]

        return [list2[i] for i in res]

    def use_dict(self, list1, list2):
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        h = {}
        for i, word in enumerate(list1):
            h[word] = i

        sum_index = []
        res = []
        for j, word in enumerate(list2):
            if word not in h:
                continue

            i = h[word]
            if not sum_index:
                sum_index.append(i+j)
                res.append(j)
            elif sum_index[0] == i+j:
                sum_index.append(i+j)
                res.append(j)
            elif sum_index[0] > i+j:
                sum_index = []
                res = []
        return [list2[i] for i in res]

if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    print Solution().use_dict(list1, list2)

