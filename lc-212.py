from collections import defaultdict

class Node:
    def __init__(self, char):
        self.children = defaultdict(Node)
        self.isEnd = False
        self.char = char

    def __str__(self):
        result = f'''---------------
value: {self.char}
children: {self.children.keys()}
---------------
'''
        return result

class Solution:
    def findWords(self, board, words):
        root = Node('root')
        m = len(board)
        n = len(board[0])
        hashmap = defaultdict(int) # { char: idx }

        board_clone = [['' for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                char = board[row][col]
                if char in hashmap:
                    hashmap[char] += 1
                idx = str(hashmap[char])
                board_clone[row][col] = char + idx

        def add_new_node(char, mountNode):
            newNode = Node(char)
            mountNode.children[char] = newNode
            return newNode

        # Build dict-tree.
        for row in range(m):
            for column in range(n):
                char = board_clone[row][column]
                newNode = add_new_node(char, root)
                # Add it's adjacent nodes.
                directions = [[row, column-1], [row, column+1], [row-1, column], [row+1, column]]
                for d in directions:
                    r, col = d
                    if r >= 0 and r < m and col >= 0 and col < n:
                        char = board_clone[r][col]
                        subNode = add_new_node(char, newNode)
                        subNode.isEnd = True
        # Find word in dict-tree
        result = []

        # DFS solution will be more suitable to this problem.
        def dfs(word, wordIdx, node, visited):
            nextVisited = visited.union({node.char})
            if wordIdx == len(word):
                return True, nextVisited
            char = word[wordIdx]
            for key in node.children:
                subNode = node.children[key]
                if subNode.isEnd:
                    subNode = root.children[key]
                if subNode.char in visited:
                    continue
                if key[0] == char:
                    r, resultVisited = dfs(word, wordIdx+1, subNode, nextVisited)
                    if r:
                        return True, resultVisited
            return False, None

        def reverse_word(word):
            return ''.join(list(reversed(word)))

        def get_word_parts(word):
            minIdx = 0
            minCharCount = 100000000
            for idx in range(len(word)):
                char = word[idx]
                if char not in hashmap:
                    return False
                if hashmap[char] < minCharCount:
                    minIdx = idx
                    minCharCount = hashmap[char]
            return word[0:minIdx+1], word[minIdx:]


        for word in words:
            nodes = []

            word_parts = get_word_parts(word)

            if not word_parts:
                continue

            left_part, right_part = word_parts
            startChar = right_part[0]

            print(word_parts, startChar)

            for idx in range(hashmap[startChar] + 1):
                nodes.append(root.children[startChar + str(idx)])

            left_part_result = False
            left_part_path = None
            right_part_result = False
            right_part_path = None

            # Left part
            left_part = reverse_word(left_part)
            for node in nodes:
                if len(left_part) < 2:
                    left_part_result = True
                    break
                r, resultVisited = dfs(left_part[1:], 0, node, {node.char}) # Pass visited set from right-part.
                if r:
                    left_part_result = True
                    left_part_path = resultVisited
                    break

            print(left_part_path)
            if not left_part_result:
                continue

            # Right part
            for node in nodes:
                if len(right_part) < 2:
                    right_part_result = True
                    break
                r, resultVisited = dfs(right_part[1:], 0, node, {node.char})
                if r:
                    right_part_result = True
                    right_part_path = resultVisited
                    break

            print(right_part_path)
            if not right_part_result:
                continue

            if len(left_part_path.intersection(right_part_path)):
                result.append(word)

        return result

solution = Solution()

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "aakl"]
#words = ["eat"]

board = [["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]

words = ["ababababaa","ababababab","ababababac","ababababad","ababababae","ababababaf","ababababag","ababababah","ababababai","ababababaj","ababababak","ababababal","ababababam","ababababan","ababababao","ababababap","ababababaq","ababababar","ababababas","ababababat","ababababau","ababababav","ababababaw","ababababax","ababababay","ababababaz","ababababba","ababababbb","ababababbc","ababababbd","ababababbe","ababababbf","ababababbg","ababababbh","ababababbi","ababababbj","ababababbk","ababababbl","ababababbm","ababababbn","ababababbo","ababababbp","ababababbq","ababababbr","ababababbs","ababababbt","ababababbu","ababababbv","ababababbw","ababababbx","ababababby","ababababbz","ababababca","ababababcb","ababababcc","ababababcd","ababababce","ababababcf","ababababcg","ababababch","ababababci","ababababcj","ababababck","ababababcl","ababababcm","ababababcn","ababababco","ababababcp","ababababcq","ababababcr","ababababcs","ababababct","ababababcu","ababababcv","ababababcw","ababababcx","ababababcy","ababababcz","ababababda","ababababdb","ababababdc","ababababdd","ababababde","ababababdf","ababababdg","ababababdh","ababababdi","ababababdj","ababababdk","ababababdl","ababababdm","ababababdn","ababababdo","ababababdp","ababababdq","ababababdr","ababababds","ababababdt","ababababdu","ababababdv","ababababdw","ababababdx","ababababdy","ababababdz","ababababea","ababababeb","ababababec","ababababed","ababababee","ababababef","ababababeg","ababababeh","ababababei","ababababej","ababababek","ababababel","ababababem","ababababen","ababababeo","ababababep","ababababeq","ababababer","ababababes","ababababet","ababababeu","ababababev","ababababew","ababababex","ababababey","ababababez","ababababfa","ababababfb","ababababfc","ababababfd","ababababfe","ababababff","ababababfg","ababababfh","ababababfi","ababababfj","ababababfk","ababababfl","ababababfm","ababababfn","ababababfo","ababababfp","ababababfq","ababababfr","ababababfs","ababababft","ababababfu","ababababfv","ababababfw","ababababfx","ababababfy","ababababfz","ababababga","ababababgb","ababababgc","ababababgd","ababababge","ababababgf","ababababgg","ababababgh","ababababgi","ababababgj","ababababgk","ababababgl","ababababgm","ababababgn","ababababgo","ababababgp","ababababgq","ababababgr","ababababgs","ababababgt","ababababgu","ababababgv","ababababgw","ababababgx","ababababgy","ababababgz","ababababha","ababababhb","ababababhc","ababababhd","ababababhe","ababababhf","ababababhg","ababababhh","ababababhi","ababababhj","ababababhk","ababababhl","ababababhm","ababababhn","ababababho","ababababhp","ababababhq","ababababhr","ababababhs","ababababht","ababababhu","ababababhv","ababababhw","ababababhx","ababababhy","ababababhz","ababababia","ababababib","ababababic","ababababid","ababababie","ababababif","ababababig","ababababih","ababababii","ababababij","ababababik","ababababil","ababababim","ababababin","ababababio","ababababip","ababababiq","ababababir","ababababis","ababababit","ababababiu","ababababiv","ababababiw","ababababix","ababababiy","ababababiz","ababababja","ababababjb","ababababjc","ababababjd","ababababje","ababababjf","ababababjg","ababababjh","ababababji","ababababjj","ababababjk","ababababjl","ababababjm","ababababjn","ababababjo","ababababjp","ababababjq","ababababjr","ababababjs","ababababjt","ababababju","ababababjv","ababababjw","ababababjx","ababababjy","ababababjz","ababababka","ababababkb","ababababkc","ababababkd","ababababke","ababababkf","ababababkg","ababababkh","ababababki","ababababkj","ababababkk","ababababkl","ababababkm","ababababkn","ababababko","ababababkp","ababababkq","ababababkr","ababababks","ababababkt","ababababku","ababababkv","ababababkw","ababababkx","ababababky","ababababkz","ababababla","abababablb","abababablc","ababababld","abababable","abababablf","abababablg","abababablh","ababababli","abababablj","abababablk","ababababll","abababablm","ababababln","abababablo","abababablp","abababablq","abababablr","ababababls","abababablt","abababablu","abababablv","abababablw","abababablx","abababably","abababablz","ababababma","ababababmb","ababababmc","ababababmd","ababababme","ababababmf","ababababmg","ababababmh","ababababmi","ababababmj","ababababmk","ababababml","ababababmm","ababababmn","ababababmo","ababababmp","ababababmq","ababababmr","ababababms","ababababmt","ababababmu","ababababmv","ababababmw","ababababmx","ababababmy","ababababmz","ababababna","ababababnb","ababababnc","ababababnd","ababababne","ababababnf","ababababng","ababababnh","ababababni","ababababnj","ababababnk","ababababnl","ababababnm","ababababnn","ababababno","ababababnp","ababababnq","ababababnr","ababababns","ababababnt","ababababnu","ababababnv","ababababnw","ababababnx","ababababny","ababababnz","ababababoa","ababababob","ababababoc","ababababod","ababababoe","ababababof","ababababog","ababababoh","ababababoi","ababababoj","ababababok","ababababol","ababababom","ababababon","ababababoo","ababababop","ababababoq","ababababor","ababababos","ababababot","ababababou","ababababov","ababababow","ababababox","ababababoy","ababababoz","ababababpa","ababababpb","ababababpc","ababababpd","ababababpe","ababababpf","ababababpg","ababababph","ababababpi","ababababpj","ababababpk","ababababpl","ababababpm","ababababpn","ababababpo","ababababpp","ababababpq","ababababpr","ababababps","ababababpt","ababababpu","ababababpv","ababababpw","ababababpx","ababababpy","ababababpz","ababababqa","ababababqb","ababababqc","ababababqd","ababababqe","ababababqf","ababababqg","ababababqh","ababababqi","ababababqj","ababababqk","ababababql","ababababqm","ababababqn","ababababqo","ababababqp","ababababqq","ababababqr","ababababqs","ababababqt","ababababqu","ababababqv","ababababqw","ababababqx","ababababqy","ababababqz","ababababra","ababababrb","ababababrc","ababababrd","ababababre","ababababrf","ababababrg","ababababrh","ababababri","ababababrj","ababababrk","ababababrl","ababababrm","ababababrn","ababababro","ababababrp","ababababrq","ababababrr","ababababrs","ababababrt","ababababru","ababababrv","ababababrw","ababababrx","ababababry","ababababrz","ababababsa","ababababsb","ababababsc","ababababsd","ababababse","ababababsf","ababababsg","ababababsh","ababababsi","ababababsj","ababababsk","ababababsl","ababababsm","ababababsn","ababababso","ababababsp","ababababsq","ababababsr","ababababss","ababababst","ababababsu","ababababsv","ababababsw","ababababsx","ababababsy","ababababsz","ababababta","ababababtb","ababababtc","ababababtd","ababababte","ababababtf","ababababtg","ababababth","ababababti","ababababtj","ababababtk","ababababtl","ababababtm","ababababtn","ababababto","ababababtp","ababababtq","ababababtr","ababababts","ababababtt","ababababtu","ababababtv","ababababtw","ababababtx","ababababty","ababababtz","ababababua","ababababub","ababababuc","ababababud","ababababue","ababababuf","ababababug","ababababuh","ababababui","ababababuj","ababababuk","ababababul","ababababum","ababababun","ababababuo","ababababup","ababababuq","ababababur","ababababus","ababababut","ababababuu","ababababuv","ababababuw","ababababux","ababababuy","ababababuz","ababababva","ababababvb","ababababvc","ababababvd","ababababve","ababababvf","ababababvg","ababababvh","ababababvi","ababababvj","ababababvk","ababababvl","ababababvm","ababababvn","ababababvo","ababababvp","ababababvq","ababababvr","ababababvs","ababababvt","ababababvu","ababababvv","ababababvw","ababababvx","ababababvy","ababababvz","ababababwa","ababababwb","ababababwc","ababababwd","ababababwe","ababababwf","ababababwg","ababababwh","ababababwi","ababababwj","ababababwk","ababababwl","ababababwm","ababababwn","ababababwo","ababababwp","ababababwq","ababababwr","ababababws","ababababwt","ababababwu","ababababwv","ababababww","ababababwx","ababababwy","ababababwz","ababababxa","ababababxb","ababababxc","ababababxd","ababababxe","ababababxf","ababababxg","ababababxh","ababababxi","ababababxj","ababababxk","ababababxl","ababababxm","ababababxn","ababababxo","ababababxp","ababababxq","ababababxr","ababababxs","ababababxt","ababababxu","ababababxv","ababababxw","ababababxx","ababababxy","ababababxz","ababababya","ababababyb","ababababyc","ababababyd","ababababye","ababababyf","ababababyg","ababababyh","ababababyi","ababababyj","ababababyk","ababababyl","ababababym","ababababyn","ababababyo","ababababyp","ababababyq","ababababyr","ababababys","ababababyt","ababababyu","ababababyv","ababababyw","ababababyx","ababababyy","ababababyz","ababababza","ababababzb","ababababzc","ababababzd","ababababze","ababababzf","ababababzg","ababababzh","ababababzi","ababababzj","ababababzk","ababababzl","ababababzm","ababababzn","ababababzo","ababababzp","ababababzq","ababababzr","ababababzs","ababababzt","ababababzu","ababababzv","ababababzw","ababababzx","ababababzy","ababababzz"]


#board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#words = ["oath","pea","eat","rain", "aakl"]

board = [["b","d","a","a","c","c","b","e"],["d","c","e","b","b","e","e","b"],["b","d","b","e","b","a","a","e"],["b","c","d","a","d","d","a","c"],["e","d","b","c","a","d","a","c"],["e","b","a","a","c","d","c","d"],["d","e","c","c","b","d","d","c"],["c","a","c","e","c","b","d","c"],["a","e","d","b","c","b","a","a"],["e","a","a","a","a","c","c","b"],["d","e","e","e","c","b","c","e"]]

words = ["cbcccec"]

board = [["d","c","e","b","d","e","d","a"],["c","a","e","a","d","d","e","e"],["a","c","e","d","b","c","c","b"],["c","b","a","a","a","e","e","e"],["a","e","d","e","b","d","d","e"],["a","a","d","c","e","a","d","e"],["b","d","e","b","b","b","c","e"],["d","a","e","e","b","e","b","d"],["b","b","c","a","b","b","b","a"],["a","c","b","a","c","a","d","d"]]

words = ["ab","bddbebcba","ededa","daebeda","edecaeabc","cbeedad","bcaaecb","c","eb","aadbdbacee","dcaaba"]
#words = ["aadbdbacee"]

result = solution.findWords(board, words)

print('result : ------------------------- ')
print(result)
