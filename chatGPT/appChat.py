import openai
import config
import typer 
from rich import print
from rich.table import Table
from rich.progress import track
from time import sleep
import webbrowser

"""
APi Reference: https://platform.openai.com/docs/api-reference 
APi Python: https://github.com/openai/openai-python
"""

def process_data():
    sleep(0.02)

def main():
    # APi Key de OpenIa
    openai.api_key = config.api_key

    for _ in track(range(100), description='[green]Empezando'):
        process_data()
    
    print("********* [bold red]ChatGPT con Python[/bold red]**********")
    print("Hola, estas hablando con ChatGPT, empecemos!")

    table = Table("Comando", "Descripción")
    table.add_row("Exit", "Salir del asistente")
    table.add_row("New", "Nueva conversación")
    table.add_row("Rol", "Establecer un rol inicial del asistente")
    table.add_row("Menu", "Mostrar el menú")
    print(table)

    # Role Sytem:  Se declara un rol inicial del modelo --> Ver documentación "role": "system", "content": "You are a helpful assistant." 
    context = {"role":"system", "content": "Eres un asistente virtual experto en programación" }
    messages_context = [context]

    

    while True:

        # input inicial
        #content = input("¿Hola, estas hablando con ChatGPT, cúal es tu pregunta? \n")
        content = __prompt()
        
        if content == "new":
            print("[bold red]Nueva conversación con el asistente virtual, datos anteriores liberados[/ bold red]")
            messages_context = [context]
            content = __prompt()

        if content == "rol":
            print("""Le puedes dar una habilidad o rol inicial a chat GPT por ejemplo:
                - Eres un asistente virtual util
                - Eres un asistente virtual experto en programación
                - Eres un asistente virtual experto en deportes
                - Eres un asistente virtual que solo responde en ingles
                - Eres un asistente virtual que traduce al español
                - entre otros
                Nota: Asegurate de dar un contexto claro al asistente.
            """)
            rol = input("¿Que rol le quieres dar al asistente?")
            context = {"role":"system", "content": rol }
            messages_context = [context]
            content = __prompt()

        if content == "menu":
            print("********* [bold red]ChatGPT con Python[/bold red]**********")
            table = Table("Comando", "Descripción")
            table.add_row("Exit", "Salir del asistente")
            table.add_row("New", "Nueva conversación")
            table.add_row("Rol", "Establecer un rol inicial del asistente")
            table.add_row("Menu", "Mostrar el menú")
            print(table)
            print("\n")
            image_resp = openai.Image.create(prompt="a book standing up on the bus", n=4, size="512x512")
            print(image_resp.data[0].url)

            url = image_resp.data[0].url
            url1 = image_resp.data[1].url
            url2= image_resp.data[2].url
            url3 = image_resp.data[3].url
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(url)
            webbrowser.get('chrome').open(url1)
            webbrowser.get('chrome').open(url2)
            webbrowser.get('chrome').open(url3)
            content = __prompt()





        # Agregamos el contenido de la pregunta inicial sin perder el contexto 
        messages_context.append({"role":"user", "content":content})

        # model: Modelo de chatGPT que se va usar
        # Role: Usuario que realiza la pregunta
        # content: Pregunta que realiza
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages_context)

        # Guado el mensaje para no perder el contexto con el asistente virtual
        response_content = response.choices[0].message.content

        messages_context.append({"role":"assistant", "content": response_content})
        print (f"[bold green]> [/bold green] [bold green]{response_content}[/ bold green]")

        # print(response) Respuesta con todos sus valores
        # print (response.choices[0].message.content)
        
def __prompt():
    prompt = typer.prompt("\n ¿Cúal es tu pregunta? ")

    if prompt == "exit":
        exit = typer.confirm("¿Estas seguro de salir?")
        if exit:
            print("Adios!")
            raise typer.Abort()
        return __prompt() 
    
    return prompt

if __name__ == "__main__":
    typer.run(main)





