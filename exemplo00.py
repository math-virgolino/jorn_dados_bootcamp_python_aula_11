import pandas as pd

class ProcessadorCSV:
    
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None
    
    def carregar_csv(self, separador):
        # Carregar o arquivo CSV em um DataFrame
        self.df = pd.read_csv(self.arquivo_csv, sep=separador)
        
    def remover_celular_vazias(self):
        # Verificar e remover celulas vazias
        self.df = self.df.dropna()
        
    def filtrar_por_estado(self, estado):
        #Filtrar as linhas pela coluna estado
        self.df = self.df[self.df['estado'] == estado]
        
    def processar(self, separador, estado):
        # Carregar CSV, remover celular vazias e filtrar estado
        self.carregar_csv(separador)
        self.remover_celular_vazias()
        self.filtrar_por_estado(estado)
        
        return self.df
    
# Exemplo de uso
arquivo_csv = './exemplo.csv'
separador = ';'
estado_filtro ='RN'

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(separador, estado_filtro)

print(df_filtrado)