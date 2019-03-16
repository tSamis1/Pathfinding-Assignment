class AlphaBeta:

    def __init__(self, inputFile):
        self.max_min = {}
        self.edges = {}
        self.alpha = 0
        self.numLeafNodes = 0
        self.readFile(inputFile)
        self.alpha_beta("A", 0, 0)

    def readFile(self, inputFile):
        f = open(inputFile, 'r')
        content = f.readlines()
        content = str(content[0])
        content = content.split()
        max_min = content[0]
        max_min = max_min[1:-1]
        edges = content[1]
        edges = edges[1:-1]

        self.max_min = self.formatString(max_min)
        self.max_min = self.formatMaxMin(self.max_min)
        self.edges = self.formatString(edges)
        self.edges = self.formatEdges(self.edges)

    def formatString(self, input):
        input = input.split("),")
        for i in range(len(input)):
            input[i] = input[i][1:]
        input[-1] = input[-1][:-1]
        return input

    def formatMaxMin(self, format_MaxMin):
        input_dict = {item.split(",")[0] : item.split(",")[1] for item in format_MaxMin}
        return input_dict

    def formatEdges(self, format_Edges):
        input_dict = {item.split(",")[0] : [] for item in format_Edges}
        for item in format_Edges:
            item = item.split(",")
            input_dict[item[0]].append(item[1])
        return input_dict

    def alpha_beta(self, current_node, alpha, beta):
        if current_node == 'A':     #redundancy
            alpha =  float("inf") * -1
            beta = float("inf")
            #need to recursively iterate through each root child
            for child in self.edges[current_node]:
                print("Parent child: " + str(child))
                print("Parent child edges: " +(self.edges[child][0]))
                alpha = max(alpha, self.alpha_beta(child, alpha, beta))
            self.alpha = alpha

        elif self.edges[current_node][0].isdigit():
            leaves = []
            for child in self.edges[current_node]:
                print("Leaf: " + str(child))
                self.numLeafNodes += 1
                leaves.append(int(child))
            if self.max_min[current_node] == 'MAX':
                return max(leaves)
            return min(leaves)

        elif self.max_min[current_node] == 'MAX':
            for child in self.edges[current_node]:
                print("MAX child: " + str(child))
                alpha  = max(alpha, self.alpha_beta(child, alpha, beta))
                print("MAX beta: " + str(beta))
                print("MAX alpha: " + str(alpha))
                if beta >= alpha:
                    #THEN CUT OFF SEARCH BELOW CURRENT NODE
                    return beta
            return alpha

        elif self.max_min[current_node] == 'MIN':
            for child in self.edges[current_node]:
                print("MIN child: " + str(child))
                beta = min(beta, self.alpha_beta(child, alpha, beta))
                print("MIN beta: " + str(beta))
                print("MIN alpha: " + str(alpha))
                if beta <= alpha:
                    #THEN CUT OFF SEARCH BELOW CURRENT NODE
                    return alpha
            return beta
def main():
    test = AlphaBeta("test2.txt")
    print()
    print(test.max_min)
    print(test.alpha)
    print(test.numLeafNodes)

main()
