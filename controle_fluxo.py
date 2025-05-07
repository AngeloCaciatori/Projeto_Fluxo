import json
import os
#Variaveis --------------------------------------------
nome=''
codigo_diferente=''
codigo=0
codigo_turmas_disciplinas=0
codigo_turmas=0
cpf=''
texto_opcao_principal=''
codigo_da_turma=0
codigo_turmas_professor=0
codigo_da_disciplina=0
codigo_matricula=0
#Listas---------------------------------------------
lista_estudante=[]
lista_disciplinas=[]
lista_professores=[]
lista_turmas=[]
lista_matriculas=[]
principal=["Estudantes","Disciplinas","Professores","Turmas","Matriculas","Sair"]
#Dicionarios-----------------------------------------
estudante={"Codigo":codigo,"Nome":nome,"CPF":cpf}
disciplinas={"Codigo":codigo,"Nome":nome}
professores={"Codigo":codigo,"Nome":nome,"CPF":cpf}
turmas={"Codigo da Turma":codigo_da_turma,"Codigo do Professor":codigo_turmas_professor,"Codigo da Disciplina":codigo_da_disciplina}
matriculas={"Codigo da Turma":codigo_da_turma,"Codigo do Estudante":codigo_matricula}
encontrado=False
validacao=True
anti_validacao=False
#Funçoes
def validar_codigo_turma(codigo):
    arquivo = "dadossalvosturm.json"
    dados = carregar_do_json(arquivo)
    return any(turma["Codigo da Turma"] == codigo for turma in dados)

def validar_professor_existe(codigo_professor):
    arquivo = "dadossalvosprof.json"
    dados = carregar_do_json(arquivo)
    return any(prof["Codigo"] == codigo_professor for prof in dados)

def validar_disciplina_existe(codigo_disciplina):
    arquivo = "dadossalvosdisci.json"
    dados = carregar_do_json(arquivo)
    return any(disciplina["Codigo"] == codigo_disciplina for disciplina in dados)

def validar_estudante_existe(codigo_estudante):
    arquivo = "dadossalvosestu.json"
    dados = carregar_do_json(arquivo)
    return any(estudante["Codigo"] == codigo_estudante for estudante in dados)

def validacao_simples(escolha_principal,lista,escolha):
    for i,escolha_principal in enumerate(lista):
          if escolha_principal["Codigo"]==escolha:
               print("Este codigo ja esta em uso")
               return anti_validacao
          else:
              break

def validacao_turmas_disciplinas(escolha_principal,lista,escolha):
    for i,escolha_principal in enumerate(lista):
          if escolha_principal["Codigo da Turma"]==escolha:
               print("Este codigo ja esta em uso")
               return anti_validacao
               
def escolha_json():
 if texto_opcao_principal=="Estudantes":
    return "dadossalvosestu.json"
 elif texto_opcao_principal=="Disciplinas":
    return "dadossalvosdisci.json"
 elif texto_opcao_principal=="Professores":
    return "dadossalvosprof.json"
 elif texto_opcao_principal=="Turmas":
    return "dadossalvosturm.json"
 elif texto_opcao_principal=="Matriculas":
    return "dadossalvosmatr.json"

def salvar_para_json(lista_final):
    with open(arquivo_json,'w',encoding="utf-8") as arquivo:
        json.dump(lista_final,arquivo,ensure_ascii=False)

def carregar_do_json(nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = arquivo_json
    if not os.path.exists(nome_arquivo):
        return []
    try:
        with open(nome_arquivo,'r',encoding="utf-8") as arquivo:
         return json.load(arquivo)
    except(json.JSONDecodeError):
            return[]

def texto_principal():
    print("\nMENU PRINCIPAL\n(1)Estudantes\n(2)Disciplinas\n(3)Professores\n(4)Turmas\n(5)Matriculas\n(6)Sair")

def texto_operacoes(opcao):
    print(opcao,":\n\n(1)Incluir\n(2)Listar\n(3)Editar\n(4)Excluir\n(5)Menu Principal")

def incluir_turmas_matriculas(escolha_principal,lista):
    print("\nIncluir")
    while True:
        try:
            codigo_da_turma=int(input("Insira o codigo da Turma:"))
            if validar_codigo_turma(codigo_da_turma):
                print("Erro: Este código de turma já está em uso!")
                continue
                
            if texto_opcao_principal=="Matriculas":
                try:
                    codigo_matricula=int(input("Insira o codigo do Estudante:"))
                    if not validar_estudante_existe(codigo_matricula):
                        print("Erro: Estudante não encontrado!")
                        continue
                    escolha_principal={"Codigo da Turma":codigo_da_turma,"Codigo do Estudante":codigo_matricula}
                except:
                    print("Dados Invalidos! Tente Novamente")
                    continue
            else:
                try:
                    codigo_turmas_professor=int(input("Insira o codigo do Professor:"))
                    if not validar_professor_existe(codigo_turmas_professor):
                        print("Erro: Professor não encontrado!")
                        break
                    codigo_da_disciplina=int(input("Insira o codigo da Disciplina:"))
                    if not validar_disciplina_existe(codigo_da_disciplina):
                        print("Erro: Disciplina não encontrada!")
                        break
                    escolha_principal={"Codigo da Turma":codigo_da_turma,"Codigo do Professor":codigo_turmas_professor,"Codigo da Disciplina":codigo_da_disciplina}
                except:
                    print("Dados Invalidos! Tente Novamente")
                    continue
            
            lista.append(escolha_principal)
            salvar_para_json(lista)
            print("Cadastro realizado com sucesso!")
            break
        except ValueError:
            print("Dados Inválidos! Digite um número inteiro.")

def incluir(escolha_principal,lista):
    print("\nIncluir")
    while True:
     try:
         print("Insira o codigo da(o)",texto_opcao_principal,":")
         codigo=int(input())
     except:
         print("Dados Invalidos! Tente Novamente")
     try:
            print("Insira o nome da(o)",texto_opcao_principal,":")
            nome=str(input())
     except:
            print("Dados Invalidos! Tente Novamente")
     if texto_opcao_principal=="Disciplinas":
               escolha_principal={"Codigo":codigo,"Nome":nome}
     else:
            try:
             cpf=str(input("Digite o CPF :"))
             escolha_principal={"Codigo":codigo,"Nome":nome,"CPF":cpf}
            except:
             print("Dados Invalidos! Tente Novamente")
     lista.append(escolha_principal)
     salvar_para_json(lista)
     print("Contato adicionado com sucesso!")
     break

def listar(lista):
    print("\nListar :\n")
    lista=carregar_do_json()
    if lista==[]:
        print("Não ha estudantes cadastrados")
    else:
     for i in lista:
        print(i,"\n")

def editar(escolha_principal,lista):
    print("\nEditar")
    lista=carregar_do_json()
    encontrado=True
    if lista==[]:
       print("Não ha ",texto_opcao_principal,"cadastrados")
       encontrado=False
    while encontrado:
     try:
        print("Qual o codigo da(o)",texto_opcao_principal,"que você deseja editar ?: ")
        escolha_codigo=int(input())
     except:
        print("Dados Invalidos! Tente Novamente")
     for i,escolha_principal in enumerate(lista):
        if escolha_principal["Codigo"]==escolha_codigo:
         lista.pop(i)
         try:
          print("Insira o novo codigo da(o)",texto_opcao_principal,":")
          novo_codigo=int(input())
         except:
            print("Dados Invalidos! Tente Novamente")
     try:
            print("Insira o novo nome da(o)",texto_opcao_principal,":")
            novo_nome=str(input())
     except:
            print("Dados Invalidos! Tente Novamente")
     if texto_opcao_principal=="Disciplinas":
               escolha_principal={"Codigo":novo_codigo,"Nome":novo_nome}
     else:
            try:
             novo_cpf=str(input("Digite o CPF :"))
             escolha_principal={"Codigo":novo_codigo,"Nome":novo_nome,"CPF":novo_cpf}
            except:
             print("Dados Invalidos! Tente Novamente")
     lista.append(escolha_principal)
     salvar_para_json(lista)
     print("Arquivo editado com sucesso!")
     break

def editar_turmas_matriculas(escolha_principal,lista):
    print("\nEditar")
    lista=carregar_do_json()
    encontrado=True
    if lista==[]:
       print("Não ha ",texto_opcao_principal,"cadastrados")
       encontrado=False
    while encontrado:
     try:
        print("Qual o codigo da(o)",texto_opcao_principal,"que você deseja editar ?: ")
        escolha_codigo=int(input())
     except:
        print("Dados Invalidos! Tente Novamente")
     for i,escolha_principal in enumerate(lista):
        if escolha_principal["Codigo da Turma"]==escolha_codigo:
         lista.pop(i)
         try:
          novo_codigo_da_turma=int(input("Insira o codigo da Turma:"))
         except:
          print("Dados Invalidos! Tente Novamente")
         if texto_opcao_principal=="Matriculas":
               try:
                   novo_codigo_matricula=int(input("Insira o codigo do Estudante:"))
               except:
                   print("Dados Invalidos! Tente Novamente")
                   break
               escolha_principal={"Codigo da Turma":novo_codigo_da_turma,"Codigo do Estudante":novo_codigo_matricula}
         else:
            try:
             novo_codigo_turmas_professor=int(input("Insira o codigo do Professor:"))
             novo_codigo_da_disciplina=int(input("Insira o codigo da turma :"))
             escolha_principal={"Codigo da Turma":novo_codigo_da_turma,"Codigo do Professor":novo_codigo_turmas_professor,"Codigo da Disciplina":novo_codigo_da_disciplina}
            except:
             print("Dados Invalidos! Tente Novamente")
             break
     lista.append(escolha_principal)
     salvar_para_json(lista)
     print("Contato editado com sucesso!")
     break

def excluir(escolha_principal,lista):
     lista=carregar_do_json()
     try:
         print("\nExcluir\nQual o codigo da(o)",texto_opcao_principal,"que você deseja excluir ?: ")
         escolha_codigo=int(input())
     except :
         print("Dados Invalidos!Tente Novamente")
         encontrado=False
     for i,escolha_principal in enumerate(lista):
          if escolha_principal["Codigo"]==escolha_codigo:
               lista.pop(i)
               print("Excluido com sucesso!")
               encontrado=True
               salvar_para_json(lista)
               break

def excluir_turmas_matriculas(escolha_principal,lista):
     lista=carregar_do_json()
     try:
         escolha_codigo=int(input("\nExcluir\nQual o codigo da turma que você deseja excluir ?: "))
     except :
         print("Dados Invalidos!Tente Novamente")
     encontrado=False
     for i,escolha_principal in enumerate(lista):
          if escolha_principal["Codigo da Turma"]==escolha_codigo:
               lista.pop(i)
               print("Excluido com sucesso!")
               encontrado=True
               salvar_para_json(lista)
               break
     if encontrado==False:
          print("Este codigo não esta cadastrado")

while True:
    texto_principal()
    try:menu_principal=int(input("\nInforme a opção desejada : "))
    except:
         print("Valor invalido!\nPor favor tente novamente.")
         continue
    if menu_principal>6 or menu_principal<1:
        print("Valor Invalido! Tente Novamente")
    while menu_principal==1:
         texto_opcao_principal=principal[0]
         arquivo_json=escolha_json()
         lista_estudante=carregar_do_json()
         texto_operacoes(texto_opcao_principal)
         try:menu_operacoes=int(input("\nInforme a opção desejada :"))
         except:
              print("Valor invalido!Por favor tente novamente .")
              continue
         if menu_operacoes==1:
              incluir(estudante,lista_estudante)
         elif menu_operacoes==2:
               listar(lista_estudante)
         elif menu_operacoes==3:
               editar(estudante,lista_estudante)
         elif menu_operacoes==4:
               excluir(estudante,lista_estudante)
         elif menu_operacoes==5:
              break
         elif menu_operacoes>5 or menu_operacoes<1:
              print("Valor invalido, por favor tente novamente")
    while menu_principal==2:
        texto_opcao_principal=principal[1]
        arquivo_json=escolha_json()
        lista_disciplinas=carregar_do_json()
        texto_operacoes(texto_opcao_principal)
        try:menu_operacoes=int(input("\nInforme a opção desejada :"))
        except:
              print("Valor invalido!Por favor tente novamente .")
              continue
        if menu_operacoes==1:
              incluir(disciplinas,lista_disciplinas)
        elif menu_operacoes==2:
               listar(lista_disciplinas)
        elif menu_operacoes==3:
               editar(disciplinas,lista_disciplinas)
        elif menu_operacoes==4:
               excluir(disciplinas,lista_disciplinas)
        elif menu_operacoes==5:
              break
        elif menu_operacoes>5 or menu_operacoes<1:
              print("Valor invalido, por favor tente novamente")
    while menu_principal==3:
        texto_opcao_principal=principal[2]
        arquivo_json=escolha_json()
        lista_professores=carregar_do_json()
        texto_operacoes(texto_opcao_principal)
        try:menu_operacoes=int(input("\nInforme a opção desejada :"))
        except:
              print("Valor invalido!Por favor tente novamente .")
              continue
        if menu_operacoes==1:
              incluir(professores,lista_professores)
        elif menu_operacoes==2:
               listar(lista_professores)
        elif menu_operacoes==3:
               editar(professores,lista_professores)
        elif menu_operacoes==4:
               excluir(professores,lista_professores)
        elif menu_operacoes==5:
              break
        elif menu_operacoes>5 or menu_operacoes<1:
              print("Valor invalido, por favor tente novamente")
    while menu_principal==4:
        texto_opcao_principal=principal[3]
        arquivo_json=escolha_json()
        lista_turmas=carregar_do_json()
        texto_operacoes(texto_opcao_principal)
        try:menu_operacoes=int(input("\nInforme a opção desejada :"))
        except:
              print("Valor invalido!Por favor tente novamente .")
              continue
        if menu_operacoes==1:
              incluir_turmas_matriculas(turmas,lista_turmas)
        elif menu_operacoes==2:
               listar(lista_turmas)
        elif menu_operacoes==3:
               editar_turmas_matriculas(turmas,lista_turmas)
        elif menu_operacoes==4:
               excluir_turmas_matriculas(turmas,lista_turmas)
        elif menu_operacoes==5:
              break
        elif menu_operacoes>5 or menu_operacoes<1:
              print("Valor invalido, por favor tente novamente")
    while menu_principal==5:
        texto_opcao_principal=principal[4]
        arquivo_json=escolha_json()
        lista_matriculas=carregar_do_json()
        texto_operacoes(texto_opcao_principal)
        try:menu_operacoes=int(input("\nInforme a opção desejada :"))
        except:
              print("Valor invalido!Por favor tente novamente .")
              continue
        if menu_operacoes==1:
              incluir_turmas_matriculas(matriculas,lista_matriculas)
        elif menu_operacoes==2:
               listar(lista_matriculas)
        elif menu_operacoes==3:
               editar_turmas_matriculas(matriculas,lista_matriculas)
        elif menu_operacoes==4:
               excluir_turmas_matriculas(matriculas,lista_matriculas)
        elif menu_operacoes==5:
              break
        elif menu_operacoes>5 or menu_operacoes<1:
              print("Valor invalido, por favor tente novamente")
    if menu_principal==6:
         print("Finalizando Operação...")
         break