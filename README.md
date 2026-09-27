# PromptRefinerPro

O PromptRefinerPro nasceu de uma ideia simples: pegar um prompt que ainda está meio cru e usar um modelo de linguagem para criar uma versão mais clara e direcionada.

É um projeto pequeno, mas está ligado a um assunto que estudo há bastante tempo: engenharia de prompts.

A versão atual foi feita em Python, usa Gradio para a interface e a API da OpenAI para o refinamento.

## O que ele faz

Você escreve um prompt, escolhe o tipo de refinamento e recebe uma nova versão.

Hoje existem três opções:

- **Técnico** — tenta deixar o pedido mais claro e preciso;
- **Criativo** — dá mais espaço para criatividade, emoção e narrativa;
- **Persuasivo** — trabalha o texto com foco em persuasão e conversão.

O programa envia uma instrução diferente ao modelo de acordo com a opção escolhida.

## Como executar

Requer Python 3.11 ou superior.

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/azenhasoft/PromptRefinerPro.git
cd PromptRefinerPro
pip install -r requirements.txt
```

Crie um arquivo `.env` na pasta do projeto:

```text
OPENAI_API_KEY=sua-chave
```

O modelo padrão fica definido no código, mas também pode ser alterado pelo `.env` sem editar o programa:

```text
OPENAI_MODEL=nome-do-modelo
```

Depois execute:

```bash
python app.py
```

O Gradio abrirá a interface da aplicação no navegador.

## Tecnologias

- Python
- Gradio
- OpenAI Python SDK
- python-dotenv

## Como está hoje

A aplicação ainda é simples, mas já valida prompt vazio, verifica a configuração da chave e trata erros da chamada à API sem derrubar a interface.

Os três estilos usam instruções próprias e ficam separados da lógica principal em um dicionário. O modelo pode ser alterado pela variável `OPENAI_MODEL`, embora ainda não exista um seletor na interface.

A versão atual usa a API da OpenAI. Embora eu tenha pensado em experimentar outros provedores, como OpenRouter, isso ainda não está implementado neste código.

Também ainda não há histórico de prompts, comparação entre versões ou testes automatizados.

## O que quero melhorar

- [x] validar quando o prompt estiver vazio
- [x] tratar erros da API de forma mais amigável
- [ ] permitir escolher o modelo pela interface
- [x] separar as instruções de refinamento do restante do código
- [ ] criar novos estilos de refinamento
- [ ] permitir comparar o prompt original com o refinado
- [ ] criar testes para a lógica que não depende da API
- [ ] experimentar suporte a outros provedores

## Por que mantenho este projeto

Tenho bastante interesse em como pequenas mudanças na forma de pedir alguma coisa podem alterar a resposta de um modelo.

O PromptRefinerPro é uma maneira de transformar esse interesse em código em vez de deixar o assunto apenas na teoria.

A versão atual não tenta ser uma plataforma completa de engenharia de prompts. É uma ferramenta simples que quero melhorar enquanto continuo estudando o tema.
