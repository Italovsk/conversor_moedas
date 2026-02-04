# 🏦 Conversor de Moedas Pro (Real-Time)

Este é um conversor de moedas dinâmico desenvolvido em Python que utiliza a **AwesomeAPI** para buscar cotações atualizadas em tempo real.

## ✨ Funcionalidades
- **Cotações em Tempo Real:** Conecta-se à API para obter valores exatos de Dólar, Euro e Bitcoin.
- **Conversão em Lote:** Mostra quanto seus Reais valem nas 3 moedas simultaneamente.
- **Conversão Inversa:** Opção para converter moedas estrangeiras de volta para o Real (BRL).
- **Relatórios Automáticos:** Cada consulta gera um registro no arquivo `relatorio_conversoes.txt`.
- **Carimbo de Tempo:** Registra data e hora exata de cada operação usando a biblioteca `datetime`.
- **Interface Inteligente:** Utiliza um loop `while True` para permitir múltiplas consultas sem reiniciar o programa.

## 🛠️ Tecnologias
- **Python 3**
- **Biblioteca Requests** (Consumo de API)
- **Biblioteca Datetime** (Formatação de data/hora)

## 📂 Como Usar
1. Instale a biblioteca necessária: `pip install requests`
2. Execute o script: `python conversor.py`
3. Digite o valor em BRL e acompanhe os resultados no console e no arquivo de texto.