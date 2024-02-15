import streamlit as st
import pandas as pd
from datetime import datetime
import time
import random as rd

html_temp = """
<div style="background-color:rgb(14, 17, 23); padding:10px; border-radius:10px">
<h2 style="color:white; text-align:center;">Desenvolvido por:</h2>
<img src="https://i.ibb.co/5jkmBWP/Untitled-presentation-1.png" alt="Logo" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

# Dados fictícios de pacientes
from datetime import datetime, timedelta
import random

# Função para gerar nomes fictícios
def gerar_nomes(n):
    nomes = ["João Silva", "Maria Oliveira", "Pedro Rocha", "Ana Costa", "Lucas Santos", "Carla Dias", "Roberto Lima", "Fernanda Gomes", "Márcio Souza", "Juliana Martins"]
    return random.sample(nomes, n)

# Função para gerar datas de última consulta
def gerar_datas_ultima_consulta(n, start_date):
    return [start_date - timedelta(days=random.randint(0, 365)) for _ in range(n)]

# Função para gerar dados numéricos aleatórios dentro de um intervalo
def gerar_dados_numericos(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função para gerar tipos sanguíneos aleatórios
def gerar_tipos_sanguineos(n):
    tipos_sanguineos = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    return [random.choice(tipos_sanguineos) for _ in range(n)]

# Função para gerar respostas sim/não/ocasionalmente
def gerar_respostas_binarias(n, opcoes=["Sim", "Não"]):
    return [random.choice(opcoes) for _ in range(n)]

# Função para gerar comorbidades
def gerar_comorbidades(n):
    comorbidades_opcoes = ["", "Hipertensão", "Diabetes", "Hipertensão, Diabetes", "Doença Cardíaca", "Asma"]
    return [random.choice(comorbidades_opcoes) for _ in range(n)]

# Definir o número de pacientes a gerar
n_pacientes = 7  # Incluindo os 3 originais, totalizando 10

# Gerar dados fictícios adicionais
dados_pacientes = {
    "Nome": gerar_nomes(n_pacientes),
    "Idade": gerar_dados_numericos(n_pacientes, 18, 65),
    "Data da Última Consulta": gerar_datas_ultima_consulta(n_pacientes, datetime.now()),
    "Peso": gerar_dados_numericos(n_pacientes, 50, 100),
    "Altura": [round(random.uniform(1.5, 2.0), 2) for _ in range(n_pacientes)],
    "Tipo Sanguíneo": gerar_tipos_sanguineos(n_pacientes),
    "Uso de Álcool": gerar_respostas_binarias(n_pacientes, ["Não", "Sim", "Ocasionalmente"]),
    "Problema Renal": gerar_respostas_binarias(n_pacientes),
    "Problema Cardíaco": gerar_respostas_binarias(n_pacientes),
    "Anemia": gerar_respostas_binarias(n_pacientes),
    "Comorbidades": gerar_comorbidades(n_pacientes),
    "Fuma": gerar_respostas_binarias(n_pacientes),
    "Diabetes": gerar_respostas_binarias(n_pacientes),
    "Já Fez Cirurgia": gerar_respostas_binarias(n_pacientes),
    "Usou Drogas": gerar_respostas_binarias(n_pacientes),
}


df_pacientes = pd.DataFrame(dados_pacientes)

# Dados fictícios de consultas
# Função para gerar históricos de anamneses fictícios
def gerar_historico_anamneses(n):
    historicos = [
        "Paciente reclamou de dor de cabeça persistente. Possível enxaqueca.",
        "Consulta de acompanhamento para controle de diabetes.",
        "Paciente relata dificuldade para dormir e ansiedade.",
        "Exame de rotina, sem queixas específicas.",
        "Consulta de acompanhamento para controle de pressao arterial.",
        "Exame de rotina, sem queixas específicas.",
        "Paciente reclamou de dor de cabeça persistente. Possível enxaqueca.",
        "Paciente relata dificuldade para dormir e ansiedade.",
        "Consulta de acompanhamento para controle de pressao arterial.",
        "Exame de rotina, sem queixas específicas.",
        "Paciente relata dificuldade para dormir e ansiedade.",
	"Consulta de acompanhamento para controle de pressao arterial.",
        "Paciente apresentou sintomas de alergia sazonal.",
        "Paciente relata dificuldade para dormir e ansiedade.",
        "Paciente reclamou de dor de cabeça persistente. Possível enxaqueca.",
        "Dor no peito relatada, necessitando de avaliação cardiológica.",
	"Ansiedade",
        "Paciente com asma",
        "Paciente com tumor na pele",
        "Paciente com pancreatite aguda",
        "Lesão no joelho durante atividade física, requer reabilitação."
    ]
    return [random.choice(historicos) for _ in range(n)]

# Função para gerar diagnósticos com CIDs fictícios
def gerar_diagnosticos_cids(n):
    cids = ["", "E11.9", "F41.9", "Z00.00", "J30.9", "I20.9","I20.9", "I20.9", "S83.5"]
    return [random.choice(cids) for _ in range(n)]

# Função para gerar tags para as consultas
def gerar_tags_consultas(n):
    tags = ["Urgente", "Rotina", "Febre", "Acompanhamento","Acompanhamento", "Acompanhamento", "Ansiedade", "Rotina", "Lesão"]
    return [random.choice(tags) for _ in range(n)]

nomes = ["João Silva","João Silva","João Silva", "Maria Oliveira","Maria Oliveira","Maria Oliveira", "Pedro Rocha","Pedro Rocha","Pedro Rocha","Pedro Rocha", "Ana Costa","Ana Costa","Ana Costa", "Lucas Santos","Lucas Santos","Lucas Santos","Lucas Santos","Lucas Santos", "Carla Dias","Carla Dias","Carla Dias","Carla Dias", "Roberto Lima","Roberto Lima","Roberto Lima","Roberto Lima","Roberto Lima", "Fernanda Gomes","Fernanda Gomes","Fernanda Gomes","Fernanda Gomes", "Márcio Souza","Márcio Souza","Márcio Souza","Márcio Souza","Márcio Souza", "Juliana Martins","Juliana Martins","Juliana Martins","Juliana Martins","Juliana Martins"]

dados_consultas = {
    "Nome": nomes,
    "Data": [ datetime(day=rd.randint(1,28), month=rd.randint(1,12), year=2023) for i in nomes],
    "Histórico de Anamneses": gerar_historico_anamneses(len(nomes)),
    "Diagnósticos com CIDs": gerar_diagnosticos_cids(len(nomes)),
    "Tags": gerar_tags_consultas(len(nomes)),
}

df_consultas = pd.DataFrame(dados_consultas)

st.markdown("""
<style>
.centered-title {
    text-align: center;
}
</style>
<h1 class="centered-title">Formulário Exemplo - Consulta com Inteligência Artificial Generativa de Dados dos Pacientes</h1>
""", unsafe_allow_html=True)

paciente_selecionado = st.selectbox("Selecione um paciente", df_pacientes["Nome"].unique())

st.write("Detalhes do Paciente Selecionado:")
st.table(df_pacientes[df_pacientes["Nome"] == paciente_selecionado])

#st.table(dados_consultas)

# Campo de busca para tags
tag_buscada = st.text_input("Buscar consultas por tag:")

# Filtrar consultas pelo paciente selecionado E pela tag, se tag_buscada não estiver vazia
if tag_buscada:
    df_consultas_filtradas = df_consultas[(df_consultas["Nome"] == paciente_selecionado) & (df_consultas["Tags"].str.contains(tag_buscada, case=False))]
else:
    df_consultas_filtradas = df_consultas[df_consultas["Nome"] == paciente_selecionado]

st.write("Detalhes das Últimas Consultas:")
st.table(df_consultas_filtradas)

if st.button("Gerar Relatório"):
    time.sleep(7)
    sintomas = "Principais sintomas relatados: Dor nos olhos, boca seca, dor nas juntas."
    possiveis_doenças = "Possíveis outras doenças: Devido aos sintomas e histórico, risco aumentado para condições relacionadas a desidratação e infecções virais."
    resumo_saude = "Resumo do histórico de saúde: Paciente com histórico de consultas por sintomas variados, indicando necessidade de monitoramento contínuo para condições crônicas e infecções."

    st.subheader("Relatório Gerado")
    st.write(sintomas)
    st.write(possiveis_doenças)
    st.write(resumo_saude)
