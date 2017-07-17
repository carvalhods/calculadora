#language: pt
#encoding: utf-8

@001
Funcionalidade: Testar os métodos da classe Operações

Para implementar novas funcionalidades no software
Como programador
Desejo uma ferramenta de testes automatizados

@10
Cenário: Testar o método somar()
Dado o valor "1" e o valor "2" para somar
Quando a aplicação executar uma soma
Então a aplicação deve retornar o valor "3" para somar

@11
Cenário: Testar o método subtrair()
Dado o valor "3" e o valor "1" para subtrair
Quando a aplicação executar uma subtração
Então a aplicação deve retornar o valor "2" para subtrair

@12
Cenário: Testar o método multiplicar()
Dado o valor "5" e o valor "5" para multiplicar
Quando a aplicação executar uma multiplicação
Então a aplicação deve retornar o valor "25" para multiplicar

@13
Cenário: Testar o método dividir()
Dado o valor "10" e o valor "2" para dividir
Quando a aplicação executar uma divisão
Então a aplicação deve retornar o valor "5" para dividir
