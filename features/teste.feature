#language: pt
#encoding: utf-8

@001
Funcionalidade: Implementar algoritmos basicos de calculo

Para efetuar calculos de forma automatizada
Como usuario
Desejo uma calculadora

  Contexto:
    Dado os seguintes valores:
      | valor1 | valor2 |
      | 2      | 2      |

@10
Cenário: Desenvolver função de adição
Quando a aplicação executar uma soma
Então a aplicação deve retornar o valor "4"

@11
Cenário: Desenvolver função de subtração
Quando a aplicação executar uma subtração
Então a aplicação deve retornar o valor "0"

@12
Cenário: Desenvolver função de multiplicação
Quando a aplicação executar uma multiplicação
Então a aplicação deve retornar o valor "4"

@13
Cenário: Desenvolver função de divisão
Quando a aplicação executar uma divisão
Então a aplicação deve retornar o valor "1"
