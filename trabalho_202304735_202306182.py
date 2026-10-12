#######################################################################################################################
### Este documento corresponde ao Trabalho Prático para a unidade curricular Programação II no ano letivo 2024/2025 ###
#######################################################################################################################

### Grupo: 41

### Estudante 1 ###
### Nome: Nuno Miguel da Silva Costa
### Número mecanográfico: 202304735

### Estudante 2 ###
### Nome: João Pereira Lobato
### Número mecanográfico: 202306182

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################################ LOTARIA ###############################

# Fazer load dos conteúdos do ficheiro "lottery-draws.txt" (descomenta a linha abaixo, se a quiseres modificar podes fazê-lo)
# dados_lotaria = np.loadtxt('lottery-draws.txt', delimiter = ' ', skiprows = 1)

# Aqui em baixo deves escrever todo o código que permite responder às perguntas feitas no enunciado do trabalho prático para os dados do ficheiro "lottery-draws.txt".
# Identifica a resposta obtida para cada pergunta num COMENTÁRIO BEM IDENTIFICADO.
# Se gerares em algum ponto um gráfico usando matplotlib, deves guardá-lo numa imagem e juntá-la à pasta com o trabalho para submissão.
# Nesse caso, a resposta à pergunta será o código que permitiu gerar o gráfico mais o gráfico em si, e qualquer texto que querias adicionar.


#1
def ex1_1(nome_ficheiro:str)->int:
  coluna_premios = np.loadtxt(nome_ficheiro,dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(7)) #lê a coluna do ficheiro que contém o valor dos prémios recebidos
  return np.max(coluna_premios)

print(ex1_1('lottery-draws.txt'))

#Resposta: O maior prémio total foi 22590829



#2
def ex1_2(nome_ficheiro:str)->int:
  coluna_vencedores = np.loadtxt(nome_ficheiro,dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(6)) #lê a coluna do ficheiro que contém o número de vencedores
  n=np.size(coluna_vencedores)                  #número de elementos da coluna
  k=np.count_nonzero(coluna_vencedores)         #número total de elementos diferentes de zero
  return n-k                                    #número total de elementos iguais a zero = nº de vezes que ocorreram 0 vencedores

print(ex1_2('lottery-draws.txt'))

#Resposta: Houveram 276 lotarias sem qualquer vencedor



#3
def ex1_3(nome_ficheiro:str)->list[int]:
  numero_bolas = np.loadtxt('lottery-draws.txt',dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(0,1,2,3,4,5)) #lê as colunas com os números das bolas
  d=dict()                                      #dicionário d associa a cada número das bolas (chaves) a sua frequência (valor)
  for line in numero_bolas:
    for num in line:                            #lê número de 6 bolas por linha e atualiza a sua frequência
        if num not in d:
          d[num]=1
        else: d[num]+=1
  max=0                                         #frequência máxima
  l=[]                                          #lista que guarda todos os elementos com a maior frequência
  for k in d.keys():
    if d[k]>max:                                #caso frequência seja superior ao máximo registado até agora, atualiza máximo e apaga antigos elementos da lista l
      l=[k]
      max=d[k]
    elif d[k]==max:                             #caso seja igual, acrescentamos à lista
      l.append(k)
  return l                                      #retorna lista l com todos os número que mais vezes saíram na lotaria

for ele in ex1_3('lottery-draws.txt'):          #imprime todos os elementos da lista l
  print(ele)

#Resposta: O número que mais vezes saiu foi o 38



#4
def ex1_4(nome_ficheiro:str)->int:
  coluna_vencedores = np.loadtxt(nome_ficheiro,dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(6)) #lê a coluna do ficheiro que contém o número de vencedores
  c=0
  l=[]
  for nv in coluna_vencedores:
    if nv==0:
      c+=1                                     #contador de número de vezes que houveram 0 vencedores
    else:
      l.append(c)                              #guarda intervalo de tempo onde houveram 0 vencedores na lista l
      c=0
  return max(l)                                #retorna o máximo da lista l, ou seja, o maior intervalo de tempo sem vencedores

print(ex1_4('lottery-draws.txt'))

#Resposta: O maior intervalo de tempo em que ninguém ganhou prémio foram 3 sorteios


#5
def ex1_5(nome_ficheiro:str)->list[int]:
  numero_bolas = np.loadtxt('lottery-draws.txt',dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(0,1,2,3,4,5)) #lê as colunas com os números das bolas
  c3=0                      #contador de quantas vezes existem 3 números seguidos em todas as linhas
  c4=0                      #contador de quantas vezes existem 4 números seguidos em todas as linhas

  for line in numero_bolas: #percorre cada linha
    A=np.sort(line)         #ordena cada linha por ordem crescente
    B=np.diff(A)            #cria array com diferença entre cada elemento consecutivo --> 1 implica dois elementos consecutivos (pois a diferença entre os dois é 1)
    c=0
    m=0

    for ele in B:          #percorre todos os elementos de cada linha
      if ele==1:
        c+=1
        m=max(m,c)
      else:
        c=0
    if m==2:          #3 números consecutivos 
      c3+=1
    if m>=3:          #4 números consecutivos (ou mais)
      c3+=1
      c4+=1
  return (c3,c4)
print(ex1_5('lottery-draws.txt'))

#Resposta: Houveram 62 combinações com 3 ou mais números consecutivos e houve 1 combinação com 4 ou mais números consecutivos


#6
def ex1_6(nome_ficheiro:str):
  numero_bolas_e_vencedores = np.loadtxt('lottery-draws.txt',dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(0,1,2,3,4,5,6)) #lê as colunas com os números das bolas e vencedores
  i=-1
  soma=0
  nv_0c=0
  nv_2c=0
  nv_3c=0
  nv_4c=0
  nv_5c=0
  nv_6c=0


  for line in numero_bolas_e_vencedores[0:, 0:6]: #percorre cada linha
    i+=1
    A=np.sort(line)         #ordena cada linha por ordem crescente
    B=np.diff(A)            #cria array com diferença entre cada elemento consecutivo --> 1 implica dois elementos consecutivos (pois a diferença entre os dois é 1)
    c=0
    m=0

    for ele in B:          #percorre todos os elementos de cada linha
      if ele==1:
        c+=1
        m=max(m,c)
      else:
        c=0
    nv=numero_bolas_e_vencedores[i][6] #em cada linha guarda número de vencedores
    if m==0:          #nenhum número consecutivos
      nv_0c+=nv
    if m>=1:          # 2 números consecutivos
      nv_2c+=nv
    if m>=2:          # 3 números consecutivos
      nv_3c+=nv
    if m>=3:          # 4 números consecutivos
      nv_4c+=nv
    if m>=4:          # 5 números consecutivos
      nv_5c+=nv
    if m>=5:          # 6 números consecutivos
      nv_6c+=nv
    soma+=nv

  #Cálculo da percentagem de vencedores com k bolas consecutivas
  r0=nv_0c/soma *100
  r2=nv_2c/soma *100
  r3=nv_3c/soma *100
  r4=nv_4c/soma *100
  r5=nv_5c/soma *100
  r6=nv_6c/soma *100

  #Criar gráfico
  fig, ax = plt.subplots()
  x=np.array(['0','2','3','4','5','6'])
  y=np.array([r0,r2,r3,r4,r5,r6])
  ax.plot(x, y, marker='o', label='Custom Data')
  plt.plot()
  plt.title('Probabilidade(em percentagem) de vencer em função do número máx. de bolas com números consecutivos')
  plt.xlabel('Nº máximo de bolas com números consecutivos')
  plt.ylabel('Probabilidade de vencer (%)')
  plt.savefig('grafico_probabilidades.pdf', format='pdf', bbox_inches='tight')
  return fig,ax

print(ex1_6('lottery-draws.txt'))

#Resposta: Pela análise do gráfico podemos concluir que a teoria é verdadeira, uma vez que o gráfico tem tendência decrescente, ou seja, a probabilidade de vencer diminui à medida que o número de números consecutivos aumenta


#7
def ex1_7(nome_ficheiro:str):
  numero_bolas_e_vencedores = np.loadtxt('lottery-draws.txt',dtype= np.int32, delimiter = ' ', skiprows = 1,usecols=(0,1,2,3,4,5,6)) #lê as colunas com os números das bolas e vencedores
  sv0,sv1,sv2,sv3,sv4,sv5,sv6=0,0,0,0,0,0,0
  for line in numero_bolas_e_vencedores:
    nv=line[6]
    contador=0
    for i in range(6):
      if line[i]>31:
        contador+=1
    if contador==0:
      sv0+=nv
    elif contador==1:
      sv1+=nv
    elif contador==2:
      sv2+=nv
    elif contador==3:
      sv3+=nv
    elif contador==4:
      sv4+=nv
    elif contador==5:
      sv5+=nv
    elif contador==6:
      sv6+=nv

  t=sv0+sv1+sv2+sv3+sv4+sv5+sv6
  p0=(sv0/t)*100
  p1=(sv1/t)*100
  p2=(sv2/t)*100
  p3=(sv3/t)*100
  p4=(sv4/t)*100
  p5=(sv5/t)*100
  p6=(sv6/t)*100

  fig, ax = plt.subplots()
  x=np.array(['0','1','2','3','4','5','6'])
  y=np.array([p0,p1,p2,p3,p4,p5,p6])
  plt.bar(x,y)
  plt.plot()
  plt.title('Probabilidade em percentagem de vencer em função do número de bolas numeradas acima de 31')
  plt.xlabel('Nº de bolas numeradas acima de 31')
  plt.ylabel('Probabilidade de vencedores')
  plt.savefig('grafico_números_maiores_que_31.pdf', format='pdf', bbox_inches='tight')
  return fig,ax

print(ex1_7('lottery-draws.txt'))

#Resposta: A teoria é falsa pois é mais provável vencer com 2 bolas acima de 31 do que com 1 ou nenhuma bolas acima de 31



################################ OSCARS ################################

# Fazer load dos conteúdos do ficheiro "the_oscar_award.csv" (descomenta a linha abaixo, se a quiseres modificar podes fazê-lo)
# dados_oscars = pd.read_csv('the_oscar_award.csv')

# Aqui em baixo deves escrever todo o código que permite responder às perguntas feitas no enunciado do trabalho prático para os dados do ficheiro "the_oscar_award.csv".
# Identifica a resposta obtida para cada pergunta num COMENTÁRIO BEM IDENTIFICADO.
# Se gerares em algum ponto um gráfico usando matplotlib, deves guardá-lo numa imagem e juntá-la à pasta com o trabalho para submissão.
# Nesse caso, a resposta à pergunta será o código que permitiu gerar o gráfico mais o gráfico em si, e qualquer texto que querias adicionar.


#1
def ex2_1(nome_ficheiro:str)->list[str]:
  data_cat_nam=pd.read_csv(nome_ficheiro,usecols=(3,4)) #lê 4º e 5º colunas (categorias e nomes) e converte-as numa dataframe
  atrizes_p = data_cat_nam[data_cat_nam['category'].isin(['ACTRESS', 'ACTRESS IN A LEADING ROLE'])]['name'] #dá o nome das atrizes (procurar na coluna com index 'name') que estão em linhas onde a 'category' é igual a 'actress' ou 'actress in a leading role'
  atrizes_s = data_cat_nam[data_cat_nam['category'] == 'ACTRESS IN A SUPPORTING ROLE']['name']

  atrizes=pd.Series(np.intersect1d(atrizes_p,atrizes_s)).sort_values()  #cria uma Series com as atrizes que foram nomeadas para ambas as categorias e ordena-as por ordem alfabética

  l=[]
  for ele in atrizes: #cria uma lista com todas as atrizes que estiveram em ambas as categorias
      l.append(ele)
  return(l)
print("Resposta: ", ex2_1('the_oscar_award.csv'))


#2
def ex2_2(nome_ficheiro:str)->list[str]:
  data_cat_nam_win=pd.read_csv(nome_ficheiro,usecols=(3,4,6)) #lê as 4º, 5º e 7º colunas (categorias,nomes e vencedores) e converte-as num dataframe

  #criar dicionário d com nome de vencedores(chave) e a 1ª categoria onde venceram(valor)
  #se voltarem a vencer e a nova categoria não corresponder ao valor guardado inicialmente adicionamos nome à lista l (vencedores de mais de 1 categoria)
  d=dict()
  l=[]
  for i,j in data_cat_nam_win.iterrows():  #j->Series com nomes, categoria e referência a se é vencedor ou não
    if j['winner']==True:
      if j['name'] not in d:
        d[j['name']]=j['category']
      elif (d[j['name']]!=j['category'] and j['name'] not in l): #verificamos ainda que o nome ainda não está na lista l, para evitar adicionar o mesmo nome múltiplas vezes
        l.append(j['name'])
  return l
print("Resposta: ", ex2_2('the_oscar_award.csv'))

#3
def ex2_3(nome_ficheiro:str)->tuple[list[tuple[str,int],int]]:
  data_fil_nom=pd.read_csv(nome_ficheiro,usecols=(0,5)) #lê a 1ª e 6ª colunas (ano do filme e nome do filme) e converte-os num dataframe
  d=dict()
  l=[]
  max=0
  for i,j in data_fil_nom.iterrows():
    t=(j['film'],j['year_film'])               #tuple com nome do filme e ano em que foi criado (para resolver problema de filmes diferentes com mesmo nome)
    if pd.isnull(j['film']):                   #ignora casos onde não há dados na coluna 'film' (nan)
      pass
    elif t not in d:                           #dicionário que conta frequência das vezes que cada filme foi nomeado(independemenete de vencer ou não)
      d[t]=1
    else:
      d[t]+=1
  for k in d.keys():                            #k[0] permite retornar apenas nome do filme (k[1] seria o ano desse mesmo filme)
    if d[k]>max:                                #caso frequência seja superior ao máximo registado até agora, atualiza máximo e apaga antigos elementos da lista l
      l=[k[0]]
      max=d[k]
    elif d[k]==max:                             #caso seja igual, acrescentamos à lista
      l.append(k[0])
  return (l,max)                                #retorna um tuple com a lista dos filmes com o nºmáximo de vitórias e esse mesmo número

print(ex2_3('the_oscar_award.csv'))

#Resposta: O número máximo foi 14 e os filmes foram: "All about Eve", "Titanic" e "La La Land"


#4
def n_maiores_chaves(dict:dict, n:int)->list:  #função auxiliar que devolve n chaves com maior valor do dicionário dict
    maiores_chaves = []
    for i in range(n):
        # Encontra chave com maior valor associado no dicionário
        maior_chave = max(dict, key=dict.get)
        # Adiciona essa maior chave à lista
        maiores_chaves.append(maior_chave)
        # Remove o par chave-valor máximo para repetir busca pela chave com o próximo valor associado mais elevado
        del dict[maior_chave]
    return maiores_chaves   #retorna lista com as n chaves com valores mais elevados do dicionário

def ex2_4(nome_ficheiro:str)->list[str] | dict:
  data_cat_nom=pd.read_csv(nome_ficheiro,usecols=(3,4)) #lê a 4ª e 5ª colunas (categoria e nomes dos nomeados) e converte-os num dataframe
  d=dict()
  l=[]
  for i,j in data_cat_nom.iterrows():
    categoria=j['category']
    if categoria=='HONORARY AWARD':
      nome=j['name']
      palavras=nome.lower().split()      #lista com todas as palavras em minúsculas do nome dos nomeados para honorary award
      for palavra in palavras:           #percorre todas as palavras do 'name' desta linha e conta a sua frequência no dicionário d
        if palavra not in d:
          d[palavra]=1
        else:
          d[palavra]+=1
  return d

print(ex2_4('the_oscar_award.csv'))                         #retorna dicionário
print(n_maiores_chaves(ex2_4('the_oscar_award.csv'),10))    #retorna 10 chaves do dicionário com maiores valores ->lista com 10 palavras mais frequentes (e se 10ª e 11ª tiverem mesmo valor???)

#Resposta: A lista das 10 palavras mais comuns é: ['the', 'of', 'for', 'his', 'to', 'and', 'in', 'motion', 'art', 'recognition']


#5
def ex2_5(nome_ficheiro:str)->list[tuple[str,dict]]:
  data_cat_nom=pd.read_csv(nome_ficheiro,usecols=(3,4)) #lê a 4ª e 5ª colunas (categoria e nomes dos nomeados) e converte-os num dataframe

  d_nomes=dict()
  lista=[]

  possibilidades=['ACTOR','ACTRESS','ACTOR IN A SUPPORTING ROLE','ACTRESS IN A SUPPORTING ROLE','ACTOR IN A LEADING ROLE','ACTRESS IN A LEADING ROLE']  #categorias possíviveis
  for i,j in data_cat_nom.iterrows():
    categoria=j['category']
    nome=j['name']
    if categoria in possibilidades:
      if nome not in d_nomes:
        d_nomes[nome]=1
      else:
        d_nomes[nome]+=1

  #nº máximo de nomeações nas categorias de ator/atriz
  max=0
  for k in d_nomes.keys():
    if d_nomes[k]>=max:
      max=d_nomes[k]

  #lista com o nome de todos/as os/as mais nomeados/as nas categorias de ator/atriz
  mais_nomeados=[]
  for nomes in d_nomes.keys():
    if d_nomes[nomes]==max:
      mais_nomeados.append(nomes)

  #Para cada nomeado da lista anterior, cria um dicionário com frequência das nomeações em cada categoria distinta
  for nomeados in mais_nomeados:
    d_nomeacoes=dict()
    for h,l in data_cat_nom.iterrows():
      n=l['name']
      c=l['category']
      if n==nomeados:
        if c not in d_nomeacoes:
          d_nomeacoes[c]=1
        else:
          d_nomeacoes[c]+=1
    tup=(nomeados,d_nomeacoes)
    lista.append(tup)
  return lista
print(ex2_5('the_oscar_award.csv'))

#Resposta: A pessoa mais nomeada foi a Meryl Streep com 21 nomeações, 4 como atriz secundária e 17 como principal


#6
def ex2_6(nome_ficheiro:str)->tuple[str,str]:
  dic_win=dict()
  dic_nom=dict()
  data_cat_nom_win=pd.read_csv(nome_ficheiro,usecols=(3,4,6)) #lê a 4ª e 5ª e 7ª colunas (categoria, nomes dos nomeados e indicação se venceu ou não) e converte-os num dataframe
  for i, j in data_cat_nom_win.iterrows():
    category=j['category']
    nome=j['name']
    win=j['winner']
    if category=="INTERNATIONAL FEATURE FILM" or category=="FOREIGN LANGUAGE FILM":
      if nome not in dic_nom: #criamos dicionários com países como chaves e nºde nomeações (dic_nom) e de vitórias (dic_win) como valores associados
        dic_nom[nome]=1
      else:
        dic_nom[nome]+=1
      if win==True:
        if nome not in dic_win:
          dic_win[nome]=1
        else:
          dic_win[nome]+=1

  max_nom = max(dic_nom, key=dic_nom.get) #país com mais nomeações (chave com maior valor)
  max_vit=max(dic_win, key=dic_win.get)   #país com mais vitórias  (chave com maior valor)

  paises=[]                  #Lista com todos os países que tiveram pelo menos uma nomeação
  for k in dic_nom.keys():
    paises.append(k)

  v=[0]*len(paises)  #Lista com número de vitórias de cada país (mesmo tamanho que lista países e n)
  n=[0]*len(paises)  #Lista com número de nomeações de cada país (mesmo tamanho que lista países e v) (já inclui número de vitórias)
  i=0
  for pais in paises:
    n[i]=dic_nom[pais]
    if pais not in dic_win:
      pass
    else:
      v[i]=dic_win[pais]
    i+=1

  # Tamanho da figura
  plt.figure(figsize=(20, 10))

  # Eixo x
  x = np.arange(len(paises))

  # Desenhar barras para nomeações por país
  plt.bar(x, n, label='Nomeações', color='blue')

  # Desenhar barras para vitórias por país
  plt.bar(x, v, label='Vitórias', color='gold')

  # Adicionar legendas e titulo
  plt.xlabel('Países')
  plt.ylabel('Nº de nomeações + vitórias')
  plt.title('Nº de nomeações e vitórias por país')
  plt.xticks(x, paises, rotation='vertical', fontsize=8)
  plt.legend()

  # Ajustar formato do gráfico
  plt.tight_layout()
  plt.savefig('grafico_vitórias_e_nomeações_por_país.pdf', format='pdf')
  plt.show()

  #Retornar tuple com países com maior número de nomeações (França) e de vitórias (Itália)
  return (max_nom,max_vit)

print(ex2_6('the_oscar_award.csv'))

#Resposta: Pela análise do gráfico o país mais nomeado foi a França e o que mais venceu foi a Itália


#7
def ex2_7(nome_ficheiro:str):
  data_yea_win=pd.read_csv(nome_ficheiro,usecols=(1,6)) #lê a 2ª e 7ª colunas (ano da cerimónia e indicação se venceu ou não) e converte-os num dataframe

  d=dict()   #dicionário com anos da cerimónia como chaves e nº de oscar atribuídos como valor

  anos=[]    #lista com chaves do dicionário d
  n_vit=[]   #lista com valores do dicionário d

  for i,j in data_yea_win.iterrows(): #percorrer dados para criar dicionário d
    ano=j['year_ceremony']
    win=j['winner']
    if win == True:
      if ano not in d:
        d[ano]=1
      else:
        d[ano]+=1

  for year in d.keys():    #criar listas das chaves e dos valores do dicionário d para criar gráfico
    anos.append(year)
    n_vit.append(d[year])

  # Tamanho da figura
  fig=plt.figure(figsize=(20, 10))

  # Eixo x (ano das cerimónias)
  x = np.arange(len(anos))

  # Linhas para nº de Oscars atribuídos em cada ano
  plt.plot(x, n_vit, label='Nº Oscars atribuídos', color='blue')

  # Adicionar legendas e titulo
  plt.xlabel('Anos')
  plt.ylabel('Nº de Oscars atribuídos')
  plt.title('Nº de Oscars atribuídos por ano')
  plt.xticks(x, anos, rotation='vertical', fontsize=8)
  plt.legend()

  # Ajustar formato do gráfico
  plt.tight_layout()
  plt.grid()
  plt.show()
  return fig

print(ex2_7('the_oscar_award.csv'))

#Resposta: Até aos anos 50 teve uma tendência crescente e a partir dessa altura tem mantido uma tendência relativamente constante