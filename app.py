import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODELO = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

INSTRUCOES = {
    "Técnico": (
        "Refine o prompt do usuário com foco em clareza, precisão e contexto técnico. "
        "Preserve a intenção original e não invente requisitos que não foram pedidos. "
        "Retorne apenas o prompt refinado."
    ),
    "Criativo": (
        "Refine o prompt do usuário para deixá-lo mais criativo e expressivo, sem mudar "
        "a ideia principal. Acrescente contexto útil quando isso ajudar o modelo a entender "
        "melhor o pedido. Retorne apenas o prompt refinado."
    ),
    "Persuasivo": (
        "Refine o prompt do usuário com foco em comunicação persuasiva e objetivo claro. "
        "Preserve a intenção original e evite exageros ou promessas que não estejam no texto. "
        "Retorne apenas o prompt refinado."
    ),
}


def criar_cliente():
    """Cria o cliente somente quando há uma chave configurada."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "A variável OPENAI_API_KEY não foi encontrada. "
            "Crie um arquivo .env e adicione sua chave antes de usar o programa."
        )

    return OpenAI(api_key=api_key)


def refinar_prompt(prompt, estilo):
    """Envia o prompt para o modelo usando a instrução do estilo escolhido."""
    prompt = (prompt or "").strip()

    if not prompt:
        return "Digite um prompt antes de iniciar o refinamento."

    instrucao = INSTRUCOES.get(estilo)

    if not instrucao:
        return "Escolha um estilo de refinamento."

    try:
        client = criar_cliente()

        resposta = client.chat.completions.create(
            model=MODELO,
            messages=[
                {"role": "system", "content": instrucao},
                {"role": "user", "content": prompt},
            ],
        )

        conteudo = resposta.choices[0].message.content

        if not conteudo:
            return "O modelo não retornou um texto. Tente novamente."

        return conteudo.strip()

    except ValueError as erro:
        return str(erro)
    except Exception as erro:
        # A interface mostra uma mensagem curta, mas o terminal mantém o erro para diagnóstico.
        print(f"Erro ao chamar a API da OpenAI: {erro}")
        return (
            "Não consegui refinar o prompt. Verifique sua conexão, a chave da API "
            "e o modelo configurado e tente novamente."
        )


interface = gr.Interface(
    fn=refinar_prompt,
    inputs=[
        gr.Textbox(
            lines=6,
            label="Prompt original",
            placeholder="Escreva aqui o prompt que você quer melhorar...",
        ),
        gr.Radio(
            ["Técnico", "Criativo", "Persuasivo"],
            value="Técnico",
            label="Estilo de refinamento",
        ),
    ],
    outputs=gr.Textbox(label="Prompt refinado", lines=10),
    title="PromptRefinerPro",
    description=(
        "Escreva um prompt, escolha o estilo e gere uma versão refinada "
        "mantendo a intenção original."
    ),
    submit_btn="Refinar prompt",
    clear_btn="Limpar",
)


if __name__ == "__main__":
    interface.launch()
