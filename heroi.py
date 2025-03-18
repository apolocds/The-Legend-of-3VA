from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)

    def cura(self):
        """
        O herói usa uma magia de cura, restaurando parte de sua vida.
        """
        if "Cura" in self.habilidades:
            self.status['vida'] += 8
            print(f"\n{self.nome} usou uma magia de cura e restaurou 8 de vida!\n")
        else:
            print(f"\n{self.nome} não está com a habilidade de cura disponível!\n")

    def bloquear(self):
        """
        O herói usa seu escudo para aumentar sua defesa ainda mais, (uso único).
        """
        if "Escudo" in self.itens:
            self.itens.remove("Escudo")
            self.status['defesa'] += 5
            print(f"\n{self.nome} usou seu escudo para aumentar sua defesa em 15!\n")
        else:
            print(f"\n{self.nome} não está com a habilidade de cura disponível!\n")

    def provocarh(self, vilao):
        """
        O herói provoca o vilão.
        """
        print(f"\n{self.nome} diz: 'Você não vai me impeir de salvar minhha princesa, {vilao.nome}!'\n")
        vilao.status['defesa'] -= 2
        print(f"\n{self.nome} provocou {vilao.nome}! A defesa de {vilao.nome} caiu para {vilao.status['defesa']}.\n")

    def __str__(self):
        return f'\nHerói: {self.nome}, Vida: {self.status["vida"]}, Ataque: {self.status["ataque"]}, Defesa: {self.status["defesa"]}, Habilidades: {self.habilidades}, Itens: {self.itens}\n'
