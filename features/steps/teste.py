"""
script: teste.py
"""
from behave import given, when, then
from operacoes import Operacoes


##########################################
# Cenário: Testar o método somar()
##########################################
@given(u'o valor "{num1}" e o valor "{num2}" para somar')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'a aplicação executar uma soma')
def step_impl(context):
    operacoes = Operacoes(context.num1, context.num2)
    context.retorno = operacoes.somar()


@then(u'a aplicação deve retornar o valor "{soma}" para somar')
def step_impl(context, soma):
    assert context.retorno == int(soma)


##############################################
# Cenário: Testar o método subtrair()
##############################################
@given(u'o valor "{num1}" e o valor "{num2}" para subtrair')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'a aplicação executar uma subtração')
def step_impl(context):
    operacoes = Operacoes(context.num1, context.num2)
    context.retorno = operacoes.subtrair()


@then(u'a aplicação deve retornar o valor "{subtr}" para subtrair')
def step_impl(context, subtr):
    assert context.retorno == int(subtr)


##############################################
# Cenário: Testar o método multiplicar()
##############################################
@given(u'o valor "{num1}" e o valor "{num2}" para multiplicar')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'a aplicação executar uma multiplicação')
def step_impl(context):
    operacoes = Operacoes(context.num1, context.num2)
    context.retorno = operacoes.multiplicar()


@then(u'a aplicação deve retornar o valor "{multipl}" para multiplicar')
def step_impl(context, multipl):
    assert context.retorno == int(multipl)


##############################################
# Cenário: Testar o método dividir()
##############################################
@given(u'o valor "{num1}" e o valor "{num2}" para dividir')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'a aplicação executar uma divisão')
def step_impl(context):
    operacoes = Operacoes(context.num1, context.num2)
    context.retorno = operacoes.dividir()


@then(u'a aplicação deve retornar o valor "{div}" para dividir')
def step_impl(context, div):
    assert context.retorno == int(div)
