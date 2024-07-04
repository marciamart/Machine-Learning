#### 1. Explique, com suas palavras, o que é machine learning?

Machine Learning (ML) é uma forma algorítmica de uma máquina aprender. Ou seja, o modelo tenta encontrar padrões e inferir regras a partir de um grande conjunto de dados. A partir disso, a máquina arrisca um valor que busca prever, classificar e entre outras coisas, com base nos dados que ela possui.

#### 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

Para efetuar o treinamento do modelo de Machine Learning, o conjunto de dados é repartido para que cada parte seja utilizada com intuitos diferentes.
- **Conjunto de treinamento:** Esta repartição será utilizada para treinar o modelo. Ou seja, ele vai pegar esse conjunto de dados e relacioná-los (dependendo do método que será empregado) entre si para chegar a uma resposta plausível para o que se deseja.
- **Conjunto de validação:** Esta repartição contém os dados utilizados para ajustar o modelo. Assim, o modelo utiliza os dados do conjunto de treinamento para chegar a resultados próximos aos do conjunto de validação, permitindo ajustes e melhorias no modelo.
- **Conjunto de teste:** Esta repartição é utilizada para avaliar a eficácia do modelo. Os dados do conjunto de teste são utilizados como entrada e, a partir de suas saídas, é observada a eficácia do treinamento e do modelo.

#### 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.
Dependendo do contexto dos dados, geralmente lido com dados ausentes de duas maneiras: ou os deixo como Nulos para que não interfiram diretamente na análise, ou substituo o dado ausente por um valor padrão (como a média, moda ou mediana) dos valores presentes na mesma coluna. Essas são as abordagens que mais utilizo.  
No entanto, pode haver situações em que é necessário excluir toda a linha de dados relacionada, ou simplesmente interpretá-la como "não aplicável".   
A forma como lido com os dados ausentes pode variar bastante conforme o contexto.

#### 4. O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?
A matriz de confusão avalia o desempenho de um modelo de ML. Ela visualiza quatro situações:

- **Verdadeiros positivos**: O modelo previu que era positivo e ele realmente era positivo.
- **Verdadeiros negativos**: O modelo previu que era negativo e ele realmente era negativo.
- **Falsos positivos**: O modelo previu que era positivo, mas na verdade era negativo.
- **Falsos negativos**: O modelo previu que era negativo, mas na verdade era positivo.

#### 5. Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, entre outras) você acha mais interessante aplicar algoritmos de machine learning?

Particularmente, acredito que em todas as áreas é possível utilizar modelos desse tipo, desde que o objetivo seja classificar ou prever algo de maneira mais rápida e eficiente.
