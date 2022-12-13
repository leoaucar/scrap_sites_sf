import pandas as pd
import re

df_conteudos = pd.read_csv("./conteudos.csv")
df_conteudos.columns

textos_limpos = []
datas_limpas = []

for i in df_conteudos['CONT']:
    texto = i
    texto = texto.strip()
    texto = texto.replace("\n", "")
    texto = re.sub("(Comente com Facebo).*","",texto)
    textos_limpos.append(texto)

for i in df_conteudos['DATA']:
    data = i[:-1]
    data = re.sub("Matéria publicada em ","",data)
    datas_limpas.append(data)


df_conteudos["CONT_LIMPO"] = textos_limpos
df_conteudos["DATA_LIMPO"] = datas_limpas
df_conteudos.to_csv("conteudos_limpos.csv")