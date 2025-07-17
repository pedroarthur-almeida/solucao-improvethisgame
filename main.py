from heroi import Heroi
from vilao import Vilao
from utils import digitar, pausar, registrar_evento, exibir_historico, separador

OPCOES = {
    "ATACAR": "1",
    "USAR_POCAO": "2",
    "SALVAR_REFEM": "3",
    "DIALOGAR": "4",
    "STATUS": "5",
    "INVENTARIO": "6",
    "HISTORICO": "7",
    "SAIR": "0"
}

def mostrar_campo_batalha(heroi):
    separador("Campo de Batalha")
    print("1. Atacar o Vilão")
    print("2. Usar Poção")
    print("3. Salvar Refém")
    print("4. Dialogar")
    print("5. Ver Status")
    print("6. Ver Inventário")
    print("7. Ver Histórico")
    print("0. Sair")
    return input("\nEscolha sua ação: ")

def turno_heroi(heroi, vilao):
    escolha = mostrar_campo_batalha(heroi)
    if escolha == OPCOES["ATACAR"]:
        heroi.dialogar("ataque")
        vilao.dialogar("defesa")
        heroi.atacar(vilao)
        registrar_evento(f"{heroi.nome} atacou {vilao.nome}")
        pausar()
        return True
    elif escolha == OPCOES["USAR_POCAO"]:
        heroi.usar_pocao()
        registrar_evento(f"{heroi.nome} usou uma poção")
        pausar()
        return False
    elif escolha == OPCOES["SALVAR_REFEM"]:
        heroi.salvar_refem()
        registrar_evento(f"{heroi.nome} tentou salvar um refém")
        pausar()
        return False
    elif escolha == OPCOES["DIALOGAR"]:
        heroi.dialogar()
        vilao.dialogar()
        registrar_evento("Diálogo entre herói e vilão")
        pausar()
        return False
    elif escolha == OPCOES["STATUS"]:
        heroi.exibir_status()
        vilao.exibir_status()
        pausar()
        return False
    elif escolha == OPCOES["INVENTARIO"]:
        heroi.exibir_inventario()
        pausar()
        return False
    elif escolha == OPCOES["HISTORICO"]:
        exibir_historico()
        pausar()
        return False
    elif escolha == OPCOES["SAIR"]:
        digitar("Encerrando a aventura...")
        exit()
    else:
        digitar("❌ Escolha inválida. Tente novamente.")
        pausar()
        return False

def turno_vilao(vilao, heroi):
    if vilao.esta_vivo():
        vilao.dialogar("ataque")
        vilao.atacar(heroi)
        registrar_evento(f"{vilao.nome} contra-atacou {heroi.nome}")
        pausar()

def iniciar_jogo():
    separador("Início do Jogo")
    heroi = Heroi("Artemis", 25, 100, classe="Arqueiro")
    vilao = Vilao("Krull", 40, 120, maldade="Alta")

    digitar(f"⚔️ Um novo herói surge: {heroi.nome}, um(a) {heroi.classe} destemido(a)!")
    digitar(f"🦹‍♂️ Um vilão ameaça o mundo: {vilao.nome}, com maldade {vilao.maldade}.")
    pausar()

    while heroi.esta_vivo() and vilao.esta_vivo():
        turno_do_vilao = turno_heroi(heroi, vilao)
        if turno_do_vilao:
            turno_vilao(vilao, heroi)

    separador("Resultado Final")
    if not heroi.esta_vivo():
        heroi.dialogar("derrota")
        vilao.dialogar("vitoria")
        digitar(f"💀 {heroi.nome} foi derrotado por {vilao.nome}...")
    else:
        heroi.dialogar("vitoria")
        vilao.dialogar("derrota")
        digitar(f"🏆 {heroi.nome} derrotou {vilao.nome} e salvou o mundo!")

    exibir_historico()

if __name__ == "__main__":
    iniciar_jogo()
