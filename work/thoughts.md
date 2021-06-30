1 - S0: lista com todos os valores falsos
2 - Gera os vizinhos
  NV: 100
    cada vizinho vai alterar 2 posições aleatórias
3 - Considera a melhor solução dentro do conjunto de vizinhos
4 - Lista tabu (movimentos proibidos)
  tamanho 7
  lista de tuplas que tem as posições que foram modificadas 
5 - Função de aspiração, aceitar se for uma melhor solução

Aspiração: 
Considerar a troca se a solução for melhor q a melhor solução encontrada até então

Questionamentos:
Como pontuar (fitness) uma solução?
R: Quantidade de clausulas verdadeiras


O que a lista Tabu representa?
Conjunto de melhores soluções geradas

O que retornamos de resultado?

7 - lista tabu
100 - soluções
delta = 1

