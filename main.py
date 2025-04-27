from fastapi import FastAPI

def saudacao(nome):
    """Este função cumprimenta a pessoa passada como parâmetro"""
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
    return {"mensagem": f"Olá, {nome}! Seja bem-vindo(a)!"}

def verificar_idade(idade):
    """Verifica a idade e imprime uma mensagem"""
    if idade < 18:
        print("Você é menor de idade.")
        return {"mensagem": "Você é menor de idade."}
    else:
        print("Você é maior de idade.")
        return {"mensagem": "Você é maior de idade."}

app = FastAPI()

@app.get("/saudacao/{nome}")
async def rota_saudacao(nome: str):
    return saudacao(nome)

@app.get("/verificar_idade/{idade}")
async def rota_verificar_idade(idade: int):
    return verificar_idade(idade)

@app.get("/")
async def root():
    return {"message": "API com suas funções!"}

if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ")
    saudacao(nome_usuario)
    try:
        idade_usuario = int(input("Digite sua idade: "))
        verificar_idade(idade_usuario)
    except ValueError:
        print("Por favor, digite um número inteiro para a idade.")