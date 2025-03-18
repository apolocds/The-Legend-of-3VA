from personagem import Personagem
import random

class Vilao(Personagem):
    """
    A classe Vilao representa o vilão do jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, heroi):
        """
        O vilão ataca o herói.
        """
        dano = self.status['ataque'] - heroi.status['defesa']
        if dano > 0:
            heroi.status['vida'] -= dano
            print(f"\n{self.nome} atacou {heroi.nome} e causou {dano} de dano!\n")
        else:
            print(f"\n{self.nome} atacou {heroi.nome}, mas não causou dano!\n")

    def provocar(self, heroi):
        """
        O vilão provoca o herói, fazendo com que sua defesa caia.
        """
        heroi.status['defesa'] -= 3
        print(f"\n{self.nome} provocou {heroi.nome}! A defesa de {heroi.nome} caiu para {heroi.status['defesa']}.\n")

    def growl(self, heroi): # minha poke referencia ai pro senhor :D
        """
        O vilão rosna, diminuindo o ataque do herói.
        """
        heroi.status['ataque'] -= 1
        print(f"\n{self.nome} rosnou para {heroi.nome}! O ataque de {heroi.nome} caiu para {heroi.status['ataque']}.\n")

    def decidir_acao(self, heroi):
        """
        O vilão decide uma ação aleatória durante a batalha.
        """
        acao = random.choice(["atacar", "provocar", "rosnar"])
        print(f"\n{self.nome} decidiu: {acao}\n")
        if acao == "atacar":
            self.atacar(heroi)
        elif acao == "provocar":
            self.provocar(heroi)
        elif acao == "rosnar":
            self.growl(heroi)    

    def __str__(self):
        return f'\nVilão: {self.nome}, Vida: {self.status["vida"]}, Ataque: {self.status["ataque"]}, Defesa: {self.status["defesa"]}\n'
