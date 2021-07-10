# Ideias
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

Insights:
Sempre que todos os valores das soluções forem iguais... Chegamos na melhor solução?
Quantidade de vezes sem melhoria

# Inferências da leitura do artigo original (Glover 1998)

## Intensificação
  Modificar as regras de escolha combinando atributos de soluções historicamente boas ou voltar a uma solução e explorar mais os vizinhos.

  Foca em examinar vizinhos de soluções elites. 


### Ideias
  - ter um histórico de soluções que chegam próximo do perfeito (SAT) e combiná-las -> "Conjunto elite"
  - armazenar a solução mais próxima do ótimo e, quando o algoritmo "enganchar", buscar os vizinhos dele (alterando apenas uma posição) -> para isso, devemos considerar uma quantidade de vizinhos inferior a nv

## Diversificação
  Busca em regiões não exploradas, ou seja, soluções significativamente diferentes das já exploradas.

### Exemplos
  - mudar regra de escolha
  - reiniciar -> inicia pela melhor solução encontrada durante a busca, com um meio de evitar retornar para a mesma
  
