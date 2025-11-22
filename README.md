# 🤖 Blockpixel Studios Bot

Bot oficial do servidor Discord da **Blockpixel Studios** ♥️

## 📋 Funcionalidades

### ℹ️ Informações
- `/informações` - Mostra informações sobre a Blockpixel Studios
- `/site` - Link do site oficial
- `/ajuda` - Lista todos os comandos

### 🎫 Sistema de Tickets
- `/ticket` - Abre um novo ticket de suporte
- `/fechar` - Fecha o ticket atual
- `/adicionar @usuário` - Adiciona alguém ao ticket
- `/remover @usuário` - Remove alguém do ticket

### 🛡️ Sistema de Moderação
- `/ban @usuário [razão]` - Bane um usuário
- `/kick @usuário [razão]` - Expulsa um usuário
- `/timeout @usuário [tempo] [razão]` - Silencia temporariamente
- `/warn @usuário [razão]` - Avisa um usuário
- `/limpar [quantidade]` - Limpa mensagens
- `/lock` - Bloqueia o canal
- `/unlock` - Desbloqueia o canal

### 🎉 Sistema de Sorteios
- `/sorteio [tempo] [vencedores] [prêmio]` - Cria sorteio
- `/reroll [id_mensagem]` - Sorteia novos vencedores
- `/finalizar [id_mensagem]` - Finaliza sorteio antecipadamente

### 🎊 Sistema de Eventos
- `/evento criar [nome] [data] [descrição]` - Cria evento
- `/evento lista` - Lista eventos ativos
- `/evento participar [id]` - Participa de evento
- `/evento sair [id]` - Sai de evento
- `/evento cancelar [id]` - Cancela evento
- `/evento info [id]` - Informações do evento

### 🔐 Sistema de Verificação
- `/verificar` - Inicia verificação
- `/confirmar [código]` - Confirma verificação
- `/setup_verificacao` - Configura sistema (Admin)

## 🚀 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/blockpixel-bot.git
cd blockpixel-bot
```

2. **Crie ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. **Instale dependências:**
```bash
pip install -r requirements.txt
```

5. **Configure o token:**
- Copie `.env.example` para `.env`
- Adicione seu token do Discord no `.env`

6. **Execute o bot:**
```bash
python main.py
```

## 📁 Estrutura do Projeto
```
blockpixel-bot/
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── .env                   # Token (NÃO commitar!)
├── .env.example          # Template
├── .gitignore            # Arquivos ignorados
├── README.md             # Documentação
├── cogs/                 # Módulos
│   ├── info.py          # Informações
│   ├── tickets.py       # Tickets
│   ├── moderation.py    # Moderação
│   ├── giveaways.py     # Sorteios
│   ├── events.py        # Eventos
│   └── verification.py  # Verificação
└── data/                # Dados
    ├── tickets.json
    ├── giveaways.json
    └── events.json
```

## 🔧 Configuração Inicial

Após adicionar o bot ao servidor, execute:
```
/setup_verificacao
```

Isso irá configurar automaticamente:
- Cargos necessários
- Canais de verificação
- Permissões corretas

## 🌐 Links

- **Site:** https://blockpixel.vercel.app/
- **Discord:** [Link do convite]

## 📝 Licença

Este projeto pertence à **Blockpixel Studios** ♥️

---

Desenvolvido com ❤️ pela Blockpixel Studios
