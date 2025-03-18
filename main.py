from heroi import Heroi
from vilao import Vilao

# função para exibir barras de vida
def exibir_barra_vida(nome, vida, vida_max):
    barra = "█" * (vida * 20 // vida_max)
    barra_completa = barra.ljust(20, "░")
    print(f"\n{nome}: [{barra_completa}] {vida}/{vida_max} HP")

# função para registrar ações no histórico
historico = []

def registrar_acao(acao):
    historico.append(acao)

def batalha(heroi, vilao):
    print(f"\n- A batalha entre {heroi.nome} e {vilao.nome} começou! -")

    while heroi.status['vida'] > 0 and vilao.status['vida'] > 0: #o loop se mantem enquanto os dois tiverem hp
        print("\n- Estado Atual:")
        exibir_barra_vida(heroi.nome, heroi.status['vida'], 100)
        exibir_barra_vida(vilao.nome, vilao.status['vida'], 120)

        print("\nEscolha uma ação:")
        print("[1] Atacar")
        print("[2] Defender")
        print("[3] Curar")
        print("[4] Escudo (Uso único)")
        print("[5] Provocar")

        escolha = input("Digite a opção: ")

        if escolha == "1":
            heroi.atacar(vilao)
            registrar_acao(f"{heroi.nome} atacou {vilao.nome}.")
        elif escolha == "2":
            heroi.defender()
            registrar_acao(f"{heroi.nome} se defendeu.")
        elif escolha == "3":
            heroi.cura()
            registrar_acao(f"{heroi.nome} usou uma magia de cura.")
        elif escolha == "4":
            heroi.bloquear()
            registrar_acao(f"{heroi.nome} usou o escudo contra {vilao.nome}.")
        elif escolha == "5":
            heroi.provocarh(vilao)
            registrar_acao(f"{heroi.nome} provocou {vilao.nome}.")
        else:
            print("Opção inválida! Você perdeu o turno.\n")

        if vilao.status['vida'] <= 0:
            print(f"\n{heroi.nome} derrotou {vilao.nome}!\n")
            break

        # turno do vilão
        vilao.decidir_acao(heroi)

        if heroi.status['vida'] <= 0:
            print(f"\n💀 {vilao.nome} derrotou {heroi.nome}!\n")

    print("\n📝 Histórico de Ações:")
    for acao in historico:
        print(f"- {acao}")

def main():
    # aqui da pra mudar os atributos dos personagens, adicionar itens e habilidades pro heroi e etc
    heroi = Heroi("Link", 100, 20, 10)
    vilao = Vilao("Ganon", 120, 25, 8)

    heroi.habilidades.append("Cura")
    heroi.itens.append("Escudo")
    batalha(heroi, vilao)

if __name__ == "__main__":
    main()
