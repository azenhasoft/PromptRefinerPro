import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Cria cliente da OpenAI com a chave de API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Função que processa o prompt
def refinar_prompt(prompt, estilo):
    if estilo == "Técnico":
        instrucao = "Melhore este prompt com foco técnico, clareza e precisão."
    elif estilo == "Criativo":
        instrucao = "Reescreva este prompt com mais criatividade, emoção e estilo narrativo."
    elif estilo == "Persuasivo":
        instrucao = "Otimize este prompt para ser mais persuasivo, atraente e com foco em conversão."
    else:
        instrucao = "Melhore este prompt."

    # Chamada correta da API com client.chat.completions
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo", # ou gpt-4 se tiver acesso
        messages=[
            {"role": "system", "content": instrucao},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return resposta.choices[0].message.content.strip()

# Interface Gradio
interface = gr.Interface(
    fn=refinar_prompt,
    inputs=[
        gr.Textbox(lines=4, label="Digite seu Prompt Original"),
        gr.Radio(["Técnico", "Criativo", "Persuasivo"], label="Estilo de Refinamento")
    ],
    outputs=gr.Textbox(label="Prompt Refinado"),
    title="PromptRefiner Pro",
    description="Otimize seus prompts com foco técnico, criativo ou persuasivo usando IA."
)

# Inicia a interface
interface.launch()