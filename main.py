def saudacao(nome):
    """Esta função cumprimenta a pessoa passada como parâmetro."""
    print(f"Olá, {nome}!")

    if __name__ == "__main__":
        nome_usuario = input("Digite seu nome: ")
        saudacao(nome_usuario)