# 🔐 Gerador Seguro de Chaves JWT

Este repositório contém um script Python simples e seguro para gerar chaves JWT (JSON Web Token) em formato Base64 seguro para URLs. As chaves são ideais para uso em aplicações backend que utilizam autenticação baseada em JWT.

## ✨ Funcionalidades

- Geração de chaves criptograficamente seguras com `secrets`
- Codificação em Base64 segura para URLs (`urlsafe_b64encode`)
- Remoção de caracteres problemáticos (`=` no final)
- Salva várias chaves nomeadas em um arquivo `.txt`

---

## 📦 Requisitos

- Python 3.6 ou superior

---

## ▶ Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Execute o script:
```bash
python gerar_chaves_jwt.py
```

3. As chaves serão geradas e salvas no arquivo chaves_jwt.txt no mesmo diretório.

📝 Exemplo de Saída
```bash
ALFA: uvY7QzMbZ8Hj0MPHtEw4x9cQJz1VFb7LGtvEMypVxl8
BRAVO: 8PijKga0YQfZtGqjMZw6iyJ1uTNN1SGZhmF_6R1Z4mM
CHARLIE: FduoCvNS5-FUKjQ2a7dl5iEtn-G4sZWTWTSaZDdaXxk
DELTA: oA-FeEmX2MSEMTUMHwWf7cEtV9rbmEmTCNGOwUJYAdM
ECHO: fxUZ9OlFJdzIMy89uD0AUVPllk-6CFV7sH8wF5bnxEM
```

⚙ Estrutura do Código
```bash
gerar_chave_jwt_segura(): Gera uma chave JWT com 32 bytes aleatórios.

criar_arquivo_chaves(lista_de_nomes): Cria um arquivo .txt com chaves associadas a nomes definidos.

main(): Define os nomes das chaves e inicia a geração.
```

📁 Personalização  
Você pode modificar a lista nomes_chaves na função main() para gerar chaves personalizadas com os nomes desejados:
```bash
nomes_chaves = ['PRODUCAO', 'DESENVOLVIMENTO', 'TESTE']
```

✅ Segurança  
Este script utiliza a biblioteca `secrets`, recomendada para geração de dados criptograficamente seguros. A codificação é feita com `base64.urlsafe_b64encode`, ideal para ambientes web e APIs REST.

📄 Licença  
Este projeto está licenciado sob a MIT License.
