class AlphaBeta:

    def __init__(self, inputFile):
        self.max_min = {}
        self.edges = {}
        self.score = 0
        self.numLeafNodes = 0
        self.readFile(inputFile)

    def readFile(self, inputFile):
        f = open(inputFile, 'r')
        output = open("alphabeta_out.txt", 'w')
        counter = 0;
        for line in f:
            if len(line.strip()) == 0 :
                continue
            self.reset()
            counter += 1
            content = line.split()
            max_min = content[0]
            max_min = max_min[1:-1]
            edges = content[1]
            edges = edges[1:-1]

            self.max_min = self.formatString(max_min)
            self.max_min = self.formatMaxMin(self.max_min)
            self.edges = self.formatString(edges)
            self.edges = self.formatEdges(self.edges)
            self.alpha_beta("A", 0, 0)
            self.outputFile(counter, output)

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
            for child in self.edges[current_node]:
                alpha = max(alpha, self.alpha_beta(child, alpha, beta))
            self.score = alpha

        elif self.edges[current_node][0].isdigit():
            leaves = []
            for child in self.edges[current_node]:
                self.numLeafNodes += 1
                leaves.append(int(child))
            if self.max_min[current_node] == 'MAX':
                return max(leaves)
            return min(leaves)

        elif self.max_min[current_node] == 'MAX':
            for child in self.edges[current_node]:
                alpha  = max(alpha, self.alpha_beta(child, alpha, beta))
                if beta >= alpha:
                    return beta
            return alpha

        elif self.max_min[current_node] == 'MIN':
            for child in self.edges[current_node]:
                beta = min(beta, self.alpha_beta(child, alpha, beta))
                if beta <= alpha:
                    return alpha
            return beta

    def outputFile(self, num, output):
        output.write("Graph " + str(num) + " :Score: " + str(self.score) + "; Leaf Nodes Examined: " + str(self.numLeafNodes) + "\n")

    def reset(self):
        self.max_min = {}
        self.edges = {}
        self.score = 0
        self.numLeafNodes = 0

def main():
    test = AlphaBeta("alphabeta.txt")

main()
