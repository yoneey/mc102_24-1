# RA 222807 Yago Eizo Yonemura
# Se necessario importe suas bibliotecas aqui


class Data:
    
    # Aqui em baixo ficam as variaveis de Data
    # Nao se esqueca de proteger as variaveis com @property e @field.setter
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    # .
    # .
    # .

    # Aqui em baixo ficam as funcoes de Data
    # .
    # .
    # .  
    @property
    def dia(self):
        return self._dia
    
    @property
    def mes(self):
        return self._mes
    
    @property
    def ano(self):
        return self._ano
    
    @dia.setter
    def dia(self, dia):
        self._dia = dia
    
    @mes.setter
    def dia(self, dia):
        self.mes = mes
    @ano.setter
    def dia(self, dia):
        self.ano = ano

class Voo:

    # Aqui em baixo ficam as variaveis de Voo
    # Nao se esqueca de proteger as variaveis com @property e @field.setter
    def __init__(self, codigo, origem, destino, data, valor):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.data = data
        self._valor = valor
    # .
    # .
    # .

    # Aqui em baixo ficam as funcoes de Voo
    # .
    # .
    # .
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def origem(self):
        return self._origem
    
    @property
    def destino(self):
        return self._destino 
    
    @property
    def data(self):
        return self._data 
    
    @property
    def valor(self):
        return self._valor
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    
    @origem.setter    
    def origem(self, origem):    
        self._origem = origem
        
    @destino.setter
    def destino(self, destino):
        self._destino = destino
    
    @data.setter
    def data(self, data):    
        self._data = data
    
    @valor.setter    
    def valor(self, valor):
        self._valor = valor
    


# Aqui em baixo fica a sua solucao

#algoritmo de solução
def algoritmo(origem, comeco, fim):
    #lista com os voo dentro do periodo especificado
    listafin = []
    
    #remove voos fora do periodo
    for passagem in dicionario:
        if dicionario[passagem].data.ano < comeco.ano or dicionario[passagem].data.ano > fim.ano:
            return dicionario.pop[passagem]
        elif dicionario[passagem].data.mes < comeco.mes or dicionario[passagem].data.mes > fim.mes:
            return dicionario.pop[passagem]
        elif dicionario[passagem].data.dia < comeco.dia or dicionario[passagem].data.dia > fim.dia:
            return dicionario.pop[passagem]
    
    #remove voos que não funcionariam (nosso amigo nn voltaria pra casa ou nem conseguiria estar no local do voo)
    for passagem in dicionario:
        if dicionario[passagem].origem == origem:
            for i in dicionario:
                if dicionario[i].origem != dicionario[passagem].destino and dicionario[i].origem != dicionario[passagem].origem:
                    dicionario.pop[i]
                listafin.append(dicionario[i])
                
    melhororigem = 0
    melhordestino = 0
    melhor = listafin[0].valor + listafin[1].valor
    #comparando a soma dos valores do voo de origem e o voo de volta, de forma a encontrar o mais barato
    for voo in listafin:
        if voo.origem != origem:
            continue
        for i in listafin:
            if i.origem == voo.destino and voo.valor + i.valor <= melhor:
                melhor = voo.valor + i.valor
                melhororigem = voo.codigo
                melhordestino = i.codigo
    print(melhororigem)
    print(melhordestino)

dicionario = {}

while True:
    operacao = input()
    match operacao:
        
        case "registrar":
            #Pega os atributos do voo
            codigo = int(input())
            origem, destino = input().split()
            dia, mes, ano = input().split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            data = Data(dia, mes, ano)
            valor = float(input())
            
            #Registra o voo como objeto
            v = Voo(
             codigo = codigo,
             origem = origem,
             destino = destino,
             data = data,
             valor = valor    
            )
            
            #Adiciona o voo para o dicionario
            dicionario[codigo] = v
            
        case "alterar":
            #pega o codigo e valor novo
            codigo, novo = input().split()
            codigo = int(codigo)
            novo = float(novo)
            
            #define o valor antigo para o print
            antigo = dicionario[codigo].valor
            
            #redefine o valor do voo
            dicionario[codigo].valor = novo
            print(f"{codigo} valor alterado de {antigo:.2f} para {novo:.2f}")
            
        case "cancelar":
            #Pega o 
            codigo = int(input())
            dicionario.pop(codigo)
            
        
        case "planejar":
            origem = input()
            com, fim = input().split()
            dia1, mes1, ano1 = com.split("/")
            dia2 , mes2, ano2 = fim.split("/")
            dataCom = Data(int(dia1), int(mes1), int(ano1))
            dataFim = Data(int(dia2), int(mes2), int(ano2))
            # comeco, fim = map(int, Data(map(int, input().split("/"))).split())
            algoritmo(origem, dataCom, dataFim)
            break
            