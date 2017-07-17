"""
script: teste.py
"""
from behave import given, when, then
from operacoes import Operacoes



@given(u'os seguintes valores')
def step_impl(context):
    for row in context.table:        
        num1 = int(row['valor1'])
        num2 = int(row['valor2'])

    context.operacoes = Operacoes(num1, num2)


@then(u'a aplicação deve retornar o valor "{valor}"')
def step_impl(context, valor):
    assert context.retorno == int(valor)

##########################################
# Cenário: Desenvolver função de adição
##########################################
@when(u'a aplicação executar uma soma')
def step_impl(context):    
    context.retorno = context.operacoes.somar()

##############################################
# Cenário: Desenvolver função de subtração
##############################################
@when(u'a aplicação executar uma subtração')
def step_impl(context):    
    context.retorno = context.operacoes.subtrair()

##############################################
# Cenário: Desenvolver função de multiplicação
##############################################
@when(u'a aplicação executar uma multiplicação')
def step_impl(context):    
    context.retorno = context.operacoes.multiplicar()


##############################################
# Cenário: Desenvolver função de divisão
##############################################
@when(u'a aplicação executar uma divisão')
def step_impl(context):    
    context.retorno = context.operacoes.dividir()


