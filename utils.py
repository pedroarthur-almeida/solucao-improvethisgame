import time
import sys

registro_de_eventos = []

def digitar(texto, delay=0.03):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pausar(segundos=1.5):
    time.sleep(segundos)

def registrar_evento(evento):
    timestamp = time.strftime("%H:%M:%S")
    registro_de_eventos.append(f"[{timestamp}] {evento}")

def exibir_historico():
    print("\n📜 Histórico de Eventos:")
    if not registro_de_eventos:
        print("Nenhum evento registrado ainda.")
        return
    for evento in registro_de_eventos:
        print(f"- {evento}")
    print()

def separador(titulo=""):
    linha = "=" * 50
    if titulo:
        print(f"\n{linha}\n🧭 {titulo}\n{linha}")
    else:
        print(f"\n{linha}")
