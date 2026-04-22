# 🌍 ETL Pipeline | World Happiness Report

## 🚀 Visão Geral
Este projeto implementa um pipeline de dados completo (ETL) utilizando Python, com foco em um dos principais desafios do mundo real: **dados inconsistentes entre diferentes fontes ao longo do tempo**.

A solução realiza a extração automatizada, padronização, transformação e carregamento dos dados do *World Happiness Report*, consolidando múltiplos arquivos em um dataset único e confiável para análise.

---

## 🎯 Objetivo
Construir um pipeline robusto capaz de:

- Integrar dados com estruturas diferentes
- Tratar inconsistências reais (colunas variáveis entre anos)
- Gerar um dataset padronizado e reutilizável
- Permitir análises temporais confiáveis

---

## 🧠 Problema de Negócio
Dados reais raramente chegam prontos para análise. Neste projeto, cada ano do dataset apresenta diferenças estruturais (nomes de colunas, formatos e padrões), exigindo um processo de transformação consistente para garantir integridade e comparabilidade.

---

## 🛠️ Tecnologias Utilizadas
- Python  
- Pandas  
- SQLite  
- Matplotlib  
- KaggleHub  

---

## ⚙️ Arquitetura do Pipeline
### 🔹 Extract
- Download automático dos dados via Kaggle
- Leitura de múltiplos arquivos CSV

### 🔹 Transform
- Padronização de nomes de colunas
- Tratamento de inconsistências entre anos
- Remoção de valores nulos
- Criação de estrutura unificada (`country`, `happiness_score`, `year`)

### 🔹 Load
- Armazenamento em banco de dados SQLite
- Estrutura pronta para consultas e análises

---

## 📊 Resultados

- Dataset consolidado com múltiplos anos
- Análise da evolução média da felicidade global
- Pipeline reutilizável para novos datasets

---

## 📈 Exemplo de Insight

A análise temporal mostra que, apesar de variações regionais, a média global de felicidade apresenta mudanças sutis ao longo dos anos — reforçando a importância de análises mais granulares (por país/região).

---
