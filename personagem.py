class Personagem:
    """
    Classe base para personagens do jogo.
    """

    def __init__(self, nome, idade, vida_maxima):
        self.nome = nome
        self.idade = idade
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.status = {
            "ataque": 10,
            "defesa": 5
        }

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.status["defesa"])
        self.vida = max(0, self.vida - dano_final)
        print(f"{self.nome} recebeu {dano_final} de dano. Vida restante: {self.vida}")

    def curar(self, quantidade):
        if not self.esta_vivo():
            print(f"{self.nome} está inconsciente e não pode ser curado.")
            return
        self.vida = min(self.vida_maxima, self.vida + quantidade)
        print(f"{self.nome} foi curado. Vida atual: {self.vida}")

    def exibir_status(self):
        print(f"\n[{self.nome}]")
        print(f"Idade: {self.idade}")
        print(f"Vida: {self.vida}/{self.vida_maxima}")
        print(f"Ataque: {self.status['ataque']} | Defesa: {self.status['defesa']}\n")

    def dialogar(self, situacao="normal"):
        print(f"{self.nome} não tem falas definidas para esta situação.")

    def __str__(self):
        return f'{self.nome} (Idade: {self.idade} | Vida: {self.vida}/{self.vida_maxima})'
