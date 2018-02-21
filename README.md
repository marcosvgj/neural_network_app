
## Modelo Preditivo de Séries Temporais Financeiras utilizando Redes Neurais

* Projeto que tem como objetivo a construção de um sistema capaz de realizar transações no Mercado Financeiro, 
especialmente no Mercado de criptomoedas ou moedas virtuais, no qual, utiliza-se modelos preditivos como uma das 
atividades essênciais e diferenciais do sistema de trading, implementados utilizando Redes Neurais Artificiais.

Data  | Status | Versão
------------- | ------------- |
08/01/2018 | Teste do protótipo Scraping() para coleta de dados | Scraping 1.0
10/01/2018 | Melhoria do job Scraping() para coleta de dados | Scraping 1.1 
15/01/2018 | Inicio da coleta de dados através da primeira versão do Scraping | Scraping 1.1
16/01/2018 | Início da implementação das funções de Pré-processamento de dados
25/01/2018 | Início da construção da classe Parser | Parser 1.0
21/02/2018 | Brainstorm de quais estratégias de investimento podem ser adotadas junto ao ambiente de Arbitragem*


# Observações

Data  | Versão 
------------- | -------------
15/01/2018 | Scraping 1.1 
27/01/2018 | Parser 1.1




Necessário tratar dados no qual o tipo primitivo se encontra como texto (*string*)  
Versão necessita de um mecanismo multi-thread para captação de dados de diferentes fontes

As estratégias de investimentos variam entre duas opções (swing trade - utiliza tanto os gráfico quanto as previsões das ações 
em âmbito diário) e (scalper - que utiliza dos dados a cada minuto). 


* * * 

# Table of contents
* Introdução
* [Parser](# Parser)
* Requerimentos 
* Módulos
* Configuração 

# Introdução

## Implementação do Scraping(): 
* Na etapa atual, é realizado uma classe Scraping no qual faz uso dos dados real-time de diversos brokers, 
que fornecem serviços para compra e venda de ativos financeiros e moedas virtuais como o Bitcoin.
O objetivo do Scraping() é coletar os dados minuto à minuto das corretoras para que se possa realizar o que é
denominado na economia de arbitragem.  

Referências: https://pt.wikipedia.org/wiki/Arbitragem_(economia)

# Módulos 

## Módulos necessários: 

* Pymongo
* JSON
* Datetime
* Thread 
* Requests
* Schedule 
* time 
* Abc ( Abstract Base Classes )
* Functools

# Parser

## Módulos necessários

- import DatabaseConnection
- import numpy as np
- import pandas as pd
- import json 
- from pandas import DataFrame
- from matplotlib import pyplot
- from keras.layers import LSTM
- from pymongo import errors, MongoClient
- import json

- %matplotlib inline  