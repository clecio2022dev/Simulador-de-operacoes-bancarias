#UTF-8 (pt - BR)

from random import randint

class ContaCorrente:
  def __init__(self, num_conta, nome_titular, saldo_corrente, senha):  
    self.num_conta = num_conta
    self.nome_titular = nome_titular
    self.saldo_corrente = saldo_corrente
    self.senha = senha

  def sacar(self, valor_saque):
    x = True
    while x == True:
      if valor_saque > self.saldo_corrente:
        x = False
        return x
      else:
        self.saldo_corrente -= valor_saque
        return self.saldo_corrente
    
  def depositar(self, valor_deposito):
    self.saldo_corrente += valor_deposito
    print("Depósito efetuado com sucesso!\n")
    print('+----------------------------------------+\n')
    return self.saldo_corrente

  def aplicar (self, valor_aplicar):
    x = True
    while x == True:
      if valor_aplicar > self.saldo_corrente:
        print('\033[31mERRO! Saldo Insuficiente!!\033[m\n')
        print('+----------------------------------------+\n')
        x = False
        return False
      else:
        self.saldo_corrente -= valor_aplicar
        self.saldo_poupanca += valor_aplicar
        return (self.saldo_corrente, self.saldo_poupanca)
      
class ContaPoupanca(ContaCorrente):
  def __init__(self, num_conta, nome_titular, saldo_corrente, senha, saldo_poupanca):
    super().__init__(num_conta, nome_titular, saldo_corrente, senha)
    self.saldo_poupanca = saldo_poupanca
    
  def resgatar (self, valor_resgate):
    x = True
    while x ==True:
      if valor_resgate > self.saldo_poupanca:
        x = False
        return False
      else:
        self.saldo_corrente += valor_resgate
        self.saldo_poupanca -= valor_resgate
        return (self.saldo_corrente, self.saldo_poupanca)   

  def mostrar_dados(self):
    print(f'+----------------------------------------+\nTitular: {self.nome_titular}\nConta: {self.num_conta}\nSaldo Conta Corrente: {self.saldo_corrente}\nSaldo Conta Poupança: {self.saldo_poupanca}\n+----------------------------------------+\n' )

  def validacaoSenhaAcesso (self):
    while True:
      s = input('Digite sua senha: ')
      print('')
      if not s.isdecimal() == True:
        print('\033[31mERRO! Senha inválida! Valor não numérico digitado.\033[m')
        print('+----------------------------------------+\n')
        continue
      elif s != self.senha:
        print('\033[31mERRO! Senha Errada!\033[m')
        print('+----------------------------------------+\n')
      elif s == self.senha:
        print('+----------------------------------------+\n')
        print('Acesso Liberado!\n')
        print('+----------------------------------------+\n')
        return True

  def criarConta(self):
    print('+----------------------------------------+')
    nome_titular = input('Digite seu nome: ').upper()
    depositoInicial = validacao_de_dados.validacaoDeposito()
    saldo_corrente = depositoInicial
    saldo_poupanca = 0
    senha = validacao_de_dados.validacaoSenha()
    num_conta = randint(100, 999)
    print('\nConta Criada com sucesso.\n\nSegue Menu com as opções de auto atendimento:')
    print('+----------------------------------------+')  
    
class ValidacaoDados:
  def __init__ (self):
   pass
      
  def validacaoSenha(self):
    while True:
      senha = input('Digite uma senha numérica com 4 dígitos: ')
      print('')
      if not senha.isdecimal() or ((len(str(senha))) != 4) == True:
        print('\033[31mERRO! Senha inválida! Senha não numérica digitada.\033[m')
        print('+----------------------------------------+\n')
        continue
      else:
        print('+----------------------------------------+\n')
        return senha
      
  def validacaoDeposito(self):
    while True:
      x = input('Digite o valor do depósito: ')
      print('')
      deposito = x
      if not deposito.isdecimal() == True:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      elif not int(deposito) > 0:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      else:
        print('+----------------------------------------+\n')
        return int(deposito)
              
  def validacaoSaque(self):
    while True:
      saque = input('Digite o valor do Saque: ')
      if not saque.isdecimal() == True:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      elif not int(saque) > 0:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
      else:
        print('+----------------------------------------+\n')
        print('Saque Realizado com Sucesso!')
        print('+----------------------------------------+\n')
        return int(saque)

  def validacaoAplicacao(self):
    while True:
      aplicacao = input('Digite o valor a ser aplicado: ')
      if not aplicacao.isdecimal() == True:
        print('\033[31mERRO! Valor inválido!\033[m\n')
        print('+----------------------------------------+\n')
        continue
      elif not int(aplicacao) > 0:
        print('\033[31mERRO! Valor inválido!\033[m\n')
        print('+----------------------------------------+\n')
      else:
        print('+----------------------------------------+\n')
        print('Aplicação Realizada com Sucesso!\n')
        print('+----------------------------------------+\n')
        return int(aplicacao)
      
  def validacaoResgate(self):
    while True:
      resgate = input('Digite o valor a ser resgatado: ')
      if not resgate.isdecimal() == True:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      elif not int(resgate) > 0:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
      else:
        print('+----------------------------------------+\n')
        return int(resgate)

  def validacaoMenu(self):
    while True:
      validacaoMenu = input('1 - Criar Conta\n2 - Mostrar Dados\n3 - Depositar\n4 - Sacar\n5 - Aplicar\n6 - Resgatar\n7 - Sair\nDigite a opção desejada: ')
      if not validacaoMenu.isdecimal() or len(str(validacaoMenu)) != 1 == True:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      elif not int(validacaoMenu) < 8:
        print('\033[31mERRO! Valor inválido!\033[m')
        print('+----------------------------------------+\n')
        continue
      else:
        print('+----------------------------------------+\n')
        return int(validacaoMenu)

print('+----------------------------------------+')
print('Bem vindos ao Fuctura Bank!!')
print('Porque seu dinheiro é nossa alegria!!')
print('Aqui seu dinheiro é bem tratado!\n')
print('Preencha os dados solicitados para efetivação de sua conta!')
print('+----------------------------------------+\n')

validacao_de_dados = ValidacaoDados()

print('+----------------------------------------+')
nome_titular = input('\nDigite seu nome: ').upper()
depositoInicial = validacao_de_dados.validacaoDeposito()
saldo_corrente = depositoInicial
saldo_poupanca = 0
senha = validacao_de_dados.validacaoSenha()
num_conta = randint(100, 999)
print('Conta Criada com sucesso.\n\n+----------------------------------------+\n\nSegue Menu com as opções de auto atendimento:\n')
print('+----------------------------------------+')

cliente = ContaPoupanca(num_conta, nome_titular, saldo_corrente, senha, saldo_poupanca) #Objeto criado e instanciado: Cliente

verificadorMenu = validacao_de_dados.validacaoMenu()

while verificadorMenu <= 7:
  if verificadorMenu == 1: # Opção 1 do Menu 
    cliente.criarConta()
    verificadorMenu = validacao_de_dados.validacaoMenu()

  elif verificadorMenu == 2: # Opção 2 Mostrar Dados
    cliente.validacaoSenhaAcesso()
    cliente.mostrar_dados()
    verificadorMenu = validacao_de_dados.validacaoMenu()

  elif verificadorMenu == 3: # Opção 3 Depositar
    cliente.validacaoSenhaAcesso()
    valorDeposito = validacao_de_dados.validacaoDeposito()
    cliente.depositar(valorDeposito)
    verificadorMenu = validacao_de_dados.validacaoMenu()

  elif verificadorMenu == 4: # Opção 4 Sacar
    cliente.validacaoSenhaAcesso()
    valorSaque = validacao_de_dados.validacaoSaque()
    if cliente.sacar(valorSaque) == False:
      print('\033[31mERRO! Saldo insuficiente!\033[m\n')
      print('+----------------------------------------+\n')
      print('Segue opções do menu principal\n')
      print('+----------------------------------------+\n')
      verificadorMenu = validacao_de_dados.validacaoMenu()
    else:
      verificadorMenu = validacao_de_dados.validacaoMenu()    

  elif verificadorMenu == 5: # Opção 5 Aplicar
    cliente.validacaoSenhaAcesso()
    valorAplicacao = validacao_de_dados.validacaoAplicacao()
    if cliente.aplicar(valorAplicacao) == False:
      
      print('+----------------------------------------+\n')
      print('Segue opções do menu principal\n')
      print('+----------------------------------------+\n')
      verificadorMenu = validacao_de_dados.validacaoMenu()
    else:
      verificadorMenu = validacao_de_dados.validacaoMenu()
  
  elif verificadorMenu == 6: # Opção 6 Resgatar
    cliente.validacaoSenhaAcesso()
    valorResgate = validacao_de_dados.validacaoResgate()
    if cliente.resgatar(valorResgate) == False:
      print('\033[31mERRO! Saldo insuficiente!\033[m\n')
      print('+----------------------------------------+\n')
      print('Segue opções do menu principal\n')
      print('+----------------------------------------+\n')
      verificadorMenu = validacao_de_dados.validacaoMenu()
    else:
      print('Resgate Realizado com Sucesso!\n')
      verificadorMenu = validacao_de_dados.validacaoMenu()

  elif verificadorMenu == 7: # Opção 7 Sair 
    print('Volte sempre!\n')
    print('+----------------------------------------+\n')
    break