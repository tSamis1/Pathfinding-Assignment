class AlphaBeta:

    def __init__(self, inputFile):
        self.max_min = {}
        self.edges = {}
        self.nodes = []
        self.alpha = 0
        self.beta = 0
        self.readFile(inputFile)
        self.initializeNodes()

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
        self.edges = self.formatString(edges)

    def formatString(self, input):
        input_dict = {}
        input = input.split("),")
        for i in range(len(input)):
            input[i] = input[i][1:]
            input[i] = input[i][:1] + ":" + input[i][2:]

        for item in input:
            item = item.split(":")
            input_dict[item[0]] = item[1]

        return input_dict

    def initializeNodes(self):
        for i in self.max_min.keys():
            self.nodes.append(i)

    def dfs_alpha_beta(self):
        '''DFS ALGORITHM THRU ALPHA BETA'''

    def alpha_beta(self, current_node):
        if current_node == 'A':
            self.alpha = float("inf") * -1
            self.beta = float("inf")
        elif self.edges[current_node].isdigit():
            return self.edges[current_node]
        elif self.max_min[current_node] == 'MAX':
            self.alpha = max(self.alpha, self.alpha_beta(self.edges[current_node]))
            if self.alpha >= self.beta:
                '''THEN CUT OFF SEARCH BELOW CURRENT NODE'''
        elif self.max_min[current_node] == 'MIN':
            self.beta = min(self.beta, self.alpha_beta(self.edges[current_node]))
            if self.beta <= self.alpha:
                '''THEN CUT OFF SEARCH BELOW CURRENT NODE'''



def main():
    test = AlphaBeta("alphabeta_small.txt")
    print(test.max_min)
    print(test.edges)
    print(test.nodes)

main()
