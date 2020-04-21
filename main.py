
import random

from variaveis_letras_numeros_simbolos import (letras_lower,letras_upper,letras_lower_e_upper, pontuacoes,numeros,todos_os_caracteres)

input_usuario_p_tamanho_da_senha = 6

lista_caracteres_importados = [letras_lower,letras_upper,pontuacoes,numeros]

lista_com_os_caracteres = []

def mensagem_inicial_pedindo_input():
  
  global input_do_usuario_p_gerar_senha

  print("Para sair digite 0")
  print("Para uma senha mais diferenciada digite 2")
  input_do_usuario_p_gerar_senha = int(input("Digite 1 para gerar uma senha rápida: "))

def gera_e_imprime_senha_rapida():

  global n_aleatorio

  if input_do_usuario_p_gerar_senha == 1:
  
    print()

    for i in range(input_usuario_p_tamanho_da_senha):

      n_aleatorio = random.randrange(len(lista_com_os_caracteres))

      print(lista_com_os_caracteres[n_aleatorio], end = " ")
    print()
    print()

def gera_e_imprime_senha_diferenciada():

  if input_do_usuario_p_gerar_senha == 2:
  
    while True:
      
      pede_inputs_diferenciados_e_soma_os_mesmos()

      if soma_dos_inputs <= input_usuario_p_tamanho_da_senha:

        gera_senha_diferenciada()
        break

      else:
        
        print("\nA quantidade da caracteres excedeu o tamanho selecionada para senha!")
        print("Você pediu {} caracteres, mas definiu {} como tamanho para senha".format(
          soma_dos_inputs, input_usuario_p_tamanho_da_senha))

def pede_inputs_diferenciados_e_soma_os_mesmos():

  global input_usuario_p_tamanho_da_senha, input_usuario_quant_n_da_senha, input_usuario_quant_letras_da_senha, input_usuario_quant_pontuacao_da_senha, soma_dos_inputs

  input_usuario_p_tamanho_da_senha = int(input("\nTamanho da senha que você quer: "))

  input_usuario_quant_n_da_senha = int(input("Quantos numeros quer?: "))

  input_usuario_quant_letras_da_senha = int(input("Quantas letras quer?: "))

  input_usuario_quant_pontuacao_da_senha = int(input("Quantas pontuacoes quer?: "))

  # dps que fazer a funcao acima, colocar essa var do lado de fora(se der)
  soma_dos_inputs = input_usuario_quant_n_da_senha + input_usuario_quant_letras_da_senha + input_usuario_quant_pontuacao_da_senha

def gera_senha_diferenciada():
  
  global guarda_caracteres_diferenciados
  
  lista_inputs_p_senha_diferenciada = [
    input_usuario_quant_n_da_senha,
    input_usuario_quant_letras_da_senha,
    input_usuario_quant_pontuacao_da_senha]
  
  contador_p_iteracao = 0 # isso deve ser relido como '0' msm

  guarda_caracteres_diferenciados = []


  for item in [numeros,letras_lower_e_upper,pontuacoes]:

    for i in range(lista_inputs_p_senha_diferenciada[contador_p_iteracao]):

      guarda_caracteres_diferenciados.append(item[random.randrange(len(item))])

    contador_p_iteracao += 1

  questiona_falta_d_caractere()

  random.shuffle(guarda_caracteres_diferenciados)
  random.shuffle(guarda_caracteres_diferenciados)
  
  print()
  for caractere in guarda_caracteres_diferenciados: print(caractere, end= " ")
  print()
  print()

def questiona_falta_d_caractere():

  if soma_dos_inputs < input_usuario_p_tamanho_da_senha:

    input_faltando_caractere = int(input("\nAinda estah faltando {} caractere(s), quer quer completar com aleatorio(s)? 1 (sim) 2 (nao): ".format(
      input_usuario_p_tamanho_da_senha - soma_dos_inputs)))
    print

    if input_faltando_caractere == 1:
      for i in range(input_usuario_p_tamanho_da_senha - soma_dos_inputs):
        guarda_caracteres_diferenciados.append(todos_os_caracteres[random.randrange(len(todos_os_caracteres))])

print("Voce está em um gerador de senhas!\n")

while True:

  try:

    mensagem_inicial_pedindo_input()

    if input_do_usuario_p_gerar_senha == 0: break

    if input_do_usuario_p_gerar_senha > 2 or input_do_usuario_p_gerar_senha < 0: raise ValueError

    for item in lista_caracteres_importados:
      lista_com_os_caracteres += item
    
    gera_e_imprime_senha_rapida()

    gera_e_imprime_senha_diferenciada()
  
  except ValueError:
    print("\nEntrada invalida!\n")

print("\nGerador de senhas fechado.")