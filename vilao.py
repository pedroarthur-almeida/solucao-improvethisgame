from personagem import Personagem
import random

class Vilao(Personagem):
    def __init__(self, nome, idade, vida_maxima, maldade):
        super().__init__(nome, idade, vida_maxima)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.status["ataque"] += self._bonus_maldade()

    def _bonus_maldade(self):
        return {
            "Baixa": 0,
            "Média": 5,
            "Alta": 10
        }[self.maldade]

    def atacar(self, alvo):
        if not self.esta_vivo():
            print(f"{self.nome} está derrotado e não pode atacar.")
            return
        dano = self.status["ataque"] + random.randint(0, 5)
        print(f"⚔️ {self.nome} (Vilão) ataca {alvo.nome} com {dano} de dano!")
        alvo.receber_dano(dano)

    def dialogar(self, situacao="normal"):
        falas = {
            "normal": [
                "Você jamais me vencerá!",
                "O mundo será meu!",
                "Desista enquanto pode, herói!",
                "Sua resistência é inútil!"
            ],
            "ataque": [
                "Sinta a minha fúria!",
                "Destruição total!",
                "Você está acabado!",
                "Vou acabar com você!"
            ],
            "defesa": [
                "Não vou cair tão fácil!",
                "Minha armadura é inquebrável!",
                "Você não passará!",
                "Prepare-se para o contra-ataque!"
            ],
            "vitoria": [
                "Mais um fracasso do herói!",
                "O mal sempre vence!",
                "Você é fraco demais!",
                "O mundo é meu playground!"
            ],
            "derrota": [
                "Isso não pode estar acontecendo...",
                "Eu voltarei... mais forte...",
                "Você pode ter ganhado hoje...",
                "Mas a guerra não acabou!"
            ],
            "curar": [
                "Vou me recuperar para te destruir!",
                "Nada como uma pausa para melhorar!",
                "A luta ainda não acabou!",
                "Prepare-se para a próxima!"
            ],
            "refem": [
                "Você nunca salvará ninguém!",
                "Reféns são fraquezas!",
                "Esse jogo não é para os fracos!",
                "Tentativa inútil!"
            ]
        }
        import random
        if situacao not in falas:
            situacao = "normal"
        print(f"💬 {self.nome} diz: \"{random.choice(falas[situacao])}\"")

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
