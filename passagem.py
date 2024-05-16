# RA 222807 Yago Eizo Yonemura
#TODO como fazer os calculos com as datas?
#TODO como fazer o cancelar voo
#TODO fazer o algoritmo final
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
    def data(self):
        return self._dia+"/"+self._mes+"/"+self._ano
    
    @data.setter
    def data(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    pass


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
    def caminho(self):
        return self._origem+" "+self._destino 
    
    @property
    def data(self):
        return self._data 
    
    @property
    def valor(self):
        return self._valor
    
    @codigo.setter
    def codigo(self, codigo, data, valor):
        self._codigo = codigo
    
    @caminho.setter    
    def caminho(self, origem, destino):    
        self._origem = origem
        self._destino = destino
    
    @data.setter
    def data(self, data):    
        self._data = data
    
    @valor.setter    
    def valor(self, valor):
        self._valor = valor
    


# Aqui em baixo fica a sua solucao
dicionario = {}

for i in range():
    operacao = input()
    match operacao:
        
        case "registrar":
            #Pega os atributos do voo
            codigo = int(input())
            origem, destino = input().split()
            data = Data(map(int, input().split("/")))
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
            codigo, novo = input().split
            
            #define o valor antigo para o print
            antigo = dicionario[codigo].valor
            
            #redefine o valor do voo
            dicionario[codigo].valor = novo
            print(f"{codigo} valor alterado de {antigo} para {novo}")
            
        case "cancelar":
            #usar pop
            pass
        
        case "planejar":
            pass

    