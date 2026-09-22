
# Pesquisa de Satisfação - Empresa TudoWeb
# Curso Técnico em Desenvolvimento de Sistemas - Agenda 08

# Número de entrevistados definido.
# NOTA: Para realizar os testes de validação solicitados, altera temporariamente este valor para 10.
TOTAL_ENTREVISTADOS = 50

# Contadores para acumular as respostas
total_excelente = 0
total_ruim = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

# Estrutura 'for' indicada quando se sabe previamente a quantidade de repetições
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    # Coleta de dados
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade do entrevistado: "))
    
    print("Opções de opinião:")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = int(input("Digite a sua opinião (1, 2 ou 3): "))
    
    # Validação de entrada com 'while' e operador 'or' (conforme exemplificado na Agenda 08)
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Escolha 1 para EXCELENTE, 2 para BOM ou 3 para RUIM.")
        opiniao = int(input("Digite novamente a sua opinião (1, 2 ou 3): "))
    
    # Estrutura de decisão para contabilizar as respostas pretendidas
    if opiniao == 1:
        total_excelente += 1
    elif opiniao == 3:
        total_ruim += 1

# Exibição dos resultados finais
print("\n================ RESULTADOS FINAIS ================")
print(f"a) Quantidade de respostas 'EXCELENTE': {total_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {total_ruim}")
print("==================================================")