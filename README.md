# Projeto Flask de Cotação do Dólar

Este é um projeto Flask que retorna a cotação atual do dólar através de uma integração com o Slack. O bot do Slack responde a certos comandos e exibe o preço atual do dólar em resposta.

## Configuração

Antes de executar o projeto, você precisará configurar algumas variáveis de ambiente. Certifique-se de ter um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
SLACK_SIGNING_SECRET=<seu_slack_signing_secret> 
SLACK_BOT_TOKEN=<seu_slack_bot_token> 
VERIFICATION_TOKEN=<seu_verification_token> 
```

## Instalação
Siga as etapas abaixo para configurar e executar o projeto:

Clone o repositório para o seu ambiente local.
Crie um ambiente virtual: python -m venv venv
Ative o ambiente virtual:
Para Windows: venv\Scripts\activate
Para macOS/Linux: source venv/bin/activate
Instale as dependências: pip install -r requirements.txt
Execute o aplicativo: python app.py
Uso
Depois de configurar e executar o aplicativo, você pode se comunicar com o bot do Slack enviando mensagens contendo os comandos "dolar agora" ou "dollar now". O bot responderá com o preço atual do dólar.

## Contribuição
Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou melhorias, sinta-se à vontade para abrir uma issue ou enviar uma pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações. ```

Lembre-se de personalizar as seções do arquivo README.md com informações específicas sobre o seu projeto.