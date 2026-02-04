import requests
from datetime import datetime

def buscar_precos():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        precos = {
            "Dólar": float(dados['USDBRL']['bid']),
            "Euro": float(dados['EURBRL']['bid']),
            "Bitcoin": float(dados['BTCBRL']['bid'])
        }
        return precos
    except Exception as e:
        print(f"Erro: {e}")
        return None

# --- Início do fluxo principal ---
while True:
    precos_atuais = buscar_precos()
    
    if not precos_atuais:
        print("Erro ao buscar cotações. Tente novamente mais tarde.")
        break

    print("\n" + "="*50)
    # Pergunta o valor. Se digitar 0, encerra o programa.
    entrada = input("Quanto você tem em R$ para converter? (ou 0 para sair): ")
    
    # Tratamento para não dar erro se o usuário não digitar nada ou texto
    if not entrada.replace('.', '', 1).isdigit():
        print("❌ Por favor, digite um número válido.")
        continue
    
    reais = float(entrada)

    if reais == 0:
        break

    # --- 1. MOSTRAR RESULTADOS NO TERMINAL ---
    print(f"\n--- 📈 RESULTADO DA CONVERSÃO (REAL -> MUNDO) ---")
    for moeda, valor in precos_atuais.items():
        resultado = reais / valor
        print(f"Com R$ {reais:.2f}, você compra {resultado:.6f} em {moeda}")
    print("-" * 50)

    # --- 2. GERANDO O ARQUIVO DE RELATÓRIO ---
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("relatorio_conversoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n=== CONSULTA EM: {agora} ===\n")
        arquivo.write(f"Conversão base: R$ {reais:.2f}\n")
        for moeda, valor in precos_atuais.items():
            res = reais / valor
            arquivo.write(f"{moeda}: {res:.6f}\n")
        arquivo.write("-" * 40 + "\n")

    print("✅ Resultados salvos no histórico!")

    # --- 3. OPÇÃO DE CONVERSÃO INVERSA ---
    print("\n🔄 Deseja converter alguma moeda de volta para Real?")
    print("0. Não, fazer nova consulta em R$")
    print("1. Dólar para Real")
    print("2. Euro para Real")
    print("3. Bitcoin para Real")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao in ["1", "2", "3"]:
        nomes = ["", "Dólar", "Euro", "Bitcoin"]
        moeda_nome = nomes[int(opcao)]
        val_est = float(input(f"Quanto você tem em {moeda_nome}? "))
        res_brl = val_est * precos_atuais[moeda_nome]
        print(f"✅ {moeda_nome} {val_est:.2f} equivalem a R$ {res_brl:.2f}")
    elif opcao == "0":
        print("Retornando ao menu principal...")
    else:
        print("❌ Opção inválida.")

# --- Encerramento (Fora do while) ---
print("\n" + "="*30)
print("✨ Programa encerrado. Até logo!")
