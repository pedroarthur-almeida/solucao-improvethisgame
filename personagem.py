# arquivo: personagem.py

class Personagem:
    """
    A class Personagem representa as características de uma identidade personagem em um jogo
    """
    def __init__(self, nome, idade, vida):
        """
        Inicializa as propriedades de um personagem
        """
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def upgrade_vida(self):
        self.vida += 10

    def downgrade_vida(self):
        if self.vida >= 10:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        self.nome = nome_editado
    
    def imprimir_personagem(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Vida: {self.vida}')


def main():
    p5 = Personagem('Fighter', 30, 100)  # Criação do objeto p5
    p5.update_nome("Link")
    p5.imprimir_personagem()  # Nome: Link, Idade: 30, Vida: 100

if __name__ == "__main__":
    main()
