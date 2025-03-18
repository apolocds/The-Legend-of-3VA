class Personagem:
    """
    A classe Personagem representa um personagem genérico no jogo.
    """
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        # usando dicionário para armazenar status
        self.status = {
            'vida': vida,
            'ataque': ataque,
            'defesa': defesa
        }
        self.habilidades = []  # lista para armazenar habilidades
        self.itens = []  # lista para armazenar itens

    def atacar(self, inimigo):
        """
        Realiza um ataque em um inimigo. O dano é calculado com base no ataque do personagem e defesa do inimigo.
        """
        dano = self.status['ataque'] - inimigo.status['defesa']
        if dano > 0:
            inimigo.status['vida'] -= dano
            print(f"\n{self.nome} atacou {inimigo.nome} e causou {dano} de dano!\n")
        else:
            print(f"\n{self.nome} atacou {inimigo.nome}, mas não causou dano!\n")

    def defender(self):
        """
        O personagem aumenta sua defesa.
        """
        self.status['defesa'] += 5
        print(f"\n{self.nome} se defendeu! A defesa aumentou para {self.status['defesa']}.\n")

    def __str__(self):
        return f'{self.nome}: Vida: {self.status["vida"]}, Ataque: {self.status["ataque"]}, Defesa: {self.status["defesa"]}, Habilidades: {self.habilidades}, Itens: {self.itens}'
