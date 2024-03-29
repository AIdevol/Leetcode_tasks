class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank_set = set(bank)
        queue = deque([(startGene, 0)])
        visited = set()
        
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for nucleotide in 'ACGT':
                    if nucleotide != gene[i]:
                        mutated_gene = gene[:i] + nucleotide + gene[i+1:]
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            visited.add(mutated_gene)
                            queue.append((mutated_gene, mutations + 1))
        
        return -1
