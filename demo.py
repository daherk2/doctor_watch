import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Dados fictícios de pacientes
dados_pacientes = {
    "Nome": ["João Silva", "Maria Oliveira", "Pedro Rocha"],
    "Idade": [34, 45, 29],
    "Data da Última Consulta": [datetime(2023, 12, 10), datetime(2023, 11, 25), datetime(2023, 10, 15)],
    "Peso": [80, 65, 77],
    "Altura": [1.75, 1.60, 1.82],
    "Tipo Sanguíneo": ["O+", "A-", "B+"],
    "Uso de Álcool": ["Não", "Sim", "Ocasionalmente"],
    "Problema Renal": ["Não", "Não", "Sim"],
    "Problema Cardíaco": ["Não", "Sim", "Não"],
    "Anemia": ["Não", "Não", "Sim"],
    "Comorbidades": ["Hipertensão", "", "Hipertensão, Diabetes"],
    "Fuma": ["Não", "Não", "Sim"],
    "Diabetes": ["Não", "Sim", "Sim"],
    "Já Fez Cirurgia": ["Sim", "Não", "Não"],
    "Usou Drogas": ["Não", "Não", "Sim"]
}

# Convertendo os dados para um DataFrame do pandas
df_pacientes = pd.DataFrame(dados_pacientes)

# Dados fictícios de consultas
dados_consultas = {
    "Nome": ["João Silva", "João Silva", "Maria Oliveira"],
    "Data": [datetime(2023, 12, 1), datetime(2023, 11, 20), datetime(2023, 11, 25)],
    "Histórico de Anamneses": [
        "Paciente reclamou de dor nos olhos, boca seca, dor nas juntas. Apos avaliacao inicial constatou-se febre de 40 graus C, saturacao sanguinea de 85, e pressao arterial de 9 por 7",
        "Consulta de rotina, sem queixas específicas. Realizado exames de sangue.",
        "Paciente apresentou sintomas de gripe. Diagnosticado com gripe H1N1."
    ],
    "Diagnósticos com CIDs": ["H10.9, E86, M25.5", "", "J09"]
}

df_consultas = pd.DataFrame(dados_consultas)


# Interface da Aplicação
st.title('Dados dos Pacientes')

# Seleção do paciente
paciente_selecionado = st.selectbox("Selecione um paciente", df_pacientes["Nome"].unique())

# Exibir a tabela com os dados do paciente selecionado
st.write("Detalhes do Paciente Selecionado:")
st.table(df_pacientes[df_pacientes["Nome"] == paciente_selecionado])

# Exibir detalhes das últimas consultas do paciente selecionado
st.write("Detalhes das Últimas Consultas:")
df_consultas_filtradas = df_consultas[df_consultas["Nome"] == paciente_selecionado]
st.table(df_consultas_filtradas)

if st.button("Gerar Relatório"):
    time.sleep(7)
    # Análise simplificada dos dados para gerar o relatório
    # Essa parte do código deve ser adaptada para refletir a lógica específica de análise de dados
    sintomas = "Principais sintomas relatados: Dor nos olhos, boca seca, dor nas juntas."
    possiveis_doenças = "Possíveis outras doenças: Devido aos sintomas e histórico, risco aumentado para condições relacionadas a desidratação e infecções virais."
    resumo_saude = "Resumo do histórico de saúde: Paciente com histórico de consultas por sintomas variados, indicando necessidade de monitoramento contínuo para condições crônicas e infecções."

    st.subheader("Relatório Gerado")
    st.write(sintomas)
    st.write(possiveis_doenças)
    st.write(resumo_saude)
