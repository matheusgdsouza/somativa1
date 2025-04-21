def saudacao(nome):
    """Esta função cumprimenta a pessoa passada como parâmetro."""
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

def verificar_idade(idade):
    """Verifica a idade e imprime uma mensagem."""
    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você é maior de idade.")

if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ")
    saudacao(nome_usuario)

    try:
        idade_usuario = int(input("Digite sua idade: "))
        verificar_idade(idade_usuario)
    except ValueError:
        print("Por favor, digite um número inteiro para a idade.")