from personagem import Personagem
import random

class Heroi(Personagem):
    def __init__(self, nome, idade, vida_maxima, classe='Guerreiro'):
        super().__init__(nome, idade, vida_maxima)
        self.classe = classe
        self.itens = {"poção": 2, "kit médico": 1}
        self.refens_salvos = 0
        self.status["ataque"] += self._bonus_classe()

    def _bonus_classe(self):
        return {"Guerreiro": 5, "Arqueiro": 3, "Mago": 2}.get(self.classe, 0)

    def atacar(self, alvo):
        if not self.esta_vivo():
            print(f"{self.nome} está inconsciente e não pode atacar.")
            return
        dano_base = self.status["ataque"]
        critico = random.random() < 0.2
        dano_total = dano_base * 2 if critico else dano_base + random.randint(1, 5)
        crit_msg = " (Crítico!)" if critico else ""
        print(f"⚔️ {self.nome} ataca {alvo.nome} com {dano_total} de dano{crit_msg}")
        alvo.receber_dano(dano_total)

    def usar_pocao(self):
        if self.itens.get("poção", 0) > 0:
            self.itens["poção"] -= 1
            print(f"🌿 {self.nome} usou uma poção!")
            self.curar(30)
            self.dialogar("curar")
        else:
            print(f"❌ {self.nome} não tem mais poções!")

    def salvar_refem(self):
        chance = random.random()
        if chance > 0.3:
            self.refens_salvos += 1
            print(f"🕊️ {self.nome} salvou um refém! Total: {self.refens_salvos}")
            self.dialogar("refem")
        else:
            print(f"❌ {self.nome} falhou ao tentar salvar o refém...")
            self.dialogar("refem")

    def dialogar(self, situacao="normal"):
        falas = {
            "normal": [
                "Eu lutarei pela justiça!",
                "Não deixarei ninguém para trás!",
                "Com coragem, vamos vencer!",
                "Você não está sozinho!"
            ],
            "ataque": [
                "Toma essa!",
                "Você não vai passar!",
                "Sentirá meu poder!",
                "Ataque certeiro!"
            ],
            "defesa": [
                "Não será fácil me derrotar!",
                "Estou preparado para isso!",
                "Minha defesa é firme!",
                "Você terá que fazer melhor!"
            ],
            "vitoria": [
                "A justiça prevaleceu!",
                "O mal foi derrotado!",
                "Vitória garantida!",
                "O bem sempre triunfa!"
            ],
            "derrota": [
                "Não... Ainda posso lutar...",
                "Não é o fim para mim!",
                "Eu... falhei...",
                "Voltar-ei mais forte!"
            ],
            "curar": [
                "Essa poção vai me fortalecer!",
                "Vamos recuperar as forças!",
                "Hora de me curar!",
                "Uma chance para continuar!"
            ],
            "refem": [
                "Vou salvar esse inocente!",
                "Ninguém ficará para trás!",
                "A liberdade é meu dever!",
                "Refém salvo, missão cumprida!"
            ]
        }
        import random
        if situacao not in falas:
            situacao = "normal"
        print(f"💬 {self.nome} diz: \"{random.choice(falas[situacao])}\"")

    def exibir_inventario(self):
        print(f"\nInventário de {self.nome}:")
        for item, qtd in self.itens.items():
            print(f"- {item}: {qtd}")
        print()
