import random

# --- Jogo da Forca ---
def jogo_da_forca():
    """
    Jogo da Forca: o jogador tenta adivinhar a palavra secreta.
    """
    print("\n--- Jogo da Forca ---")

    palavras = ["python", "programação", "desenvolvedor", "tecnologia", "computador"]
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []

    while tentativas > 0 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'nenhuma'}")

        letra = input("Digite uma letra: ").lower()

        # Validação da entrada do usuário
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Escolha outra.")
            continue

        # Verifica se a letra está na palavra
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_descobertas[i] = letra
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print("Letra incorreta!")

    # Resultado do jogo
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        print(f"\nFim de jogo! A palavra era: {palavra_secreta}")


# --- Pedra, Papel e Tesoura ---
def pedra_papel_tesoura():
    """
    Jogo clássico de Pedra, Papel e Tesoura contra o computador.
    """
    print("\n--- Pedra, Papel e Tesoura ---")

    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        jogador = input("Escolha (pedra, papel, tesoura ou sair): ").lower()

        if jogador == "sair":
            print("Saindo do jogo...")
            break

        if jogador not in opcoes:
            print("Opção inválida. Escolha entre pedra, papel ou tesoura.")
            continue

        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")

        # Lógica do jogo
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "tesoura" and computador == "papel") or \
             (jogador == "papel" and computador == "pedra"):
            print("Você venceu!")
        else:
            print("Você perdeu!")


# --- Menu Principal ---
def main():
    """
    Menu principal para selecionar o jogo.
    """
    while True:
        print("\n===== MENU DE JOGOS =====")
        print("1. Jogo da Forca")
        print("2. Pedra, Papel e Tesoura")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            jogo_da_forca()
        elif escolha == '2':
            pedra_papel_tesoura()
        elif escolha == '3':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()