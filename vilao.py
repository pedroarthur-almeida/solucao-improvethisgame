# arquivo: vilao.py

from personagem import Personagem # type: ignore

class Vilao(Personagem):
    """
    A class Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade):
        super().__init__(nome, idade, vida)
        self.maldade = maldade

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()  # Chama o método downgrade_vida do personagem passado
    
    def imprimir_vilao(self):
        print(f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}')
    
def main():
    # Criando um vilão e um personagem
    vilao = Vilao('Ganon', 45, 120, 'Alta')
    p5 = Personagem('Link', 30, 100)

    # Vilão ataca o personagem
    vilao.ataque(p5)  # Ganondorf ataca Link
    vilao.imprimir_vilao()
    p5.imprimir_personagem()

if __name__ == "__main__":
    main()
