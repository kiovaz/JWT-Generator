


import secrets
import base64

def gerar_chave_jwt_segura():

    # Gera 32 bytes aleatórios seguros
    bytes_aleatorios = secrets.token_bytes(32)
    
    # Converte para Base64 e remove caracteres problemáticos
    chave_base64 = base64.urlsafe_b64encode(bytes_aleatorios).decode('utf-8')
    chave_limpa = chave_base64.rstrip('=')
    
    return chave_limpa

def criar_arquivo_chaves(nomes_chaves, nome_arquivo='chaves_jwt.txt'):

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for nome in nomes_chaves:
                chave = gerar_chave_jwt_segura()
                linha = f"{nome}: {chave}\n"
                arquivo.write(linha)
                
        print(f"✔ Sucesso: {len(nomes_chaves)} chaves salvas em '{nome_arquivo}'")
        
    except IOError as erro:
        print(f"✖ Erro ao salvar arquivo: {erro}")

def main():
    nomes_chaves = [
        'ALFA',    # A
        'BRAVO',    # B
        'CHARLIE',  # C
        'DELTA',    # D
        'ECHO'      # E
    ]
    
    criar_arquivo_chaves(nomes_chaves)

if __name__ == "__main__":
    main()
