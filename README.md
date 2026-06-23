# Microserviço de Notificação (notificacao-ms)

## Instalação e Execução

Siga os passos abaixo para configurar o projeto:

### 1. Clonar o Repositório
Abra o terminal na pasta onde deseja salvar o projeto e execute o comando abaixo:
```bash
git clone https://github.com/jhonathanemanuel/notificacoes_ms.git
```

### 2. Acessar a Pasta do Projeto
Navegue para dentro do diretório que o Git acabou de criar:
```bash
cd notificacoes_ms
```

### 3. Ambiente Virtual
```bash
python -m venv venv
```

### 4. Ativação 

Windows:
```bash 
.\venv\Scripts\activate
```
Linux/Mac:
```bash 
source venv/bin/activate
```

### 5. Dependências
```bash 
pip install django djangorestframework django-cors-headers
pip freeze > requirements.txt
```

### 6. Banco de Dados e Superusuário
O projeto usa PostgreSQL por padrão. Caso queira usar SQLite, altere o DATABASES no settings.py.
```bash 
python manage.py makemigrations notificacoes
python manage.py migrate
python manage.py createsuperuser
```

### 7. Execução (Porta Isolada)
#### Como o Portfólio já roda na porta 8000, o microserviço deve ser executado obrigatoriamente na porta 8001:
```bash 
python manage.py runserver 8001
```

## Fluxo de Integração e Testes

Para fazer o ecossistema funcionar com o seu Portfólio, siga este roteiro:

### 1. Obter a Chave de Acesso (API Key)
1. Acesse o painel administrativo do Microserviço em uma **Janela Anônima**: `http://127.0.0.1:8001/admin/`
2. Vá em **Empresas** e clique em **Adicionar Empresa**.
3. Cadastre com o nome `Portfolio` e salve. Copie o **hash de 16 caracteres** gerado automaticamente.

### 2. Configurar o Portfólio (Porta 8000)
1. No final do arquivo `settings.py` do seu Portfólio, cole as credenciais:
   ```python
   NOTIFICACAO_MS_URL = '[http://127.0.0.1:8001](http://127.0.0.1:8001)'
   NOTIFICACAO_MS_API_KEY = 'COLE_O_HASH_COPIADO_AQUI'
   
Certifique-se de que o arquivo context_processors.py foi criado no app do seu portfólio e está devidamente registrado na lista TEMPLATES -> OPTIONS -> context_processors.

### 3. Simular uma Notificação Real

1. No Admin do Microserviço (8001), vá em Targets e adicione um novo alvo vinculando a empresa Portfolio ao ID numérico do usuário logado no seu portfólio (ex: 1).
2. Vá em Notifications, adicione uma nova mensagem para este Target e mantenha a opção Is read desmarcada.
3. Olhe para a página do seu Portfólio. Em até 5 segundos, o sino mudará o badge de X para 1 (vermelho) de forma assíncrona.

## Recomendações e Diretrizes Críticas

* Isolamento de Cookies (Aba Anônima): O Django substitui os cookies de login se você acessar os dois painéis /admin/ no mesmo navegador convencional. Sempre gerencie o Admin do Microserviço (8001) por uma Janela Anônima.
* Segurança por Headers (CORS): Garanta que as diretivas CORS_ALLOWED_ORIGINS, CORS_ALLOW_METHODS e CORS_ALLOW_HEADERS (contendo "x-api-key" e "x-user-id") estão salvas explicitamente no settings.py do Microserviço para evitar o bloqueio de requisições pelo navegador.
* Independência de Bancos: O Microserviço nunca consulta o banco de dados do Portfólio. O user_id é apenas um número abstrato recebido via cabeçalho HTTP para controle interno.