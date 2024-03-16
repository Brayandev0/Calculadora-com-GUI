# Criador         : Brayan vieira 
# função          : Uma simples com interface gráfica 
# versão          : 1.1
# data da criação : 16/3/2024
# Notas versão 1.1: Correção de Falha de segurança

import flet as ft
import time 

contas_totais = ""  # Inicializa a variável contas_totais

def main(pagina: ft.Page):
    pagina.title = "Minha Calculadora"
    pagina.vertical_alignment = ft.MainAxisAlignment.START
    pagina.window_width = 310
    pagina.window_height = 350
    
    # Campo de texto para exibir os resultados
    resultado = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=200)

    # Funções para realizar operações matemáticas e atualizar contas_totais
    def add_num(numero):
        global contas_totais 
        resultado.value += numero
        contas_totais += numero
        pagina.update()

    def remover_um_numero(e):
        global contas_totais 
        resultado.value = resultado.value[:-1]
        contas_totais = contas_totais[:-1]
        pagina.update()

    def realizar_soma(e):
        if resultado.value and resultado.value[-1] != "+":
            global contas_totais 
            resultado.value += "+"
            contas_totais += "+"
            pagina.update()

    def multiplicar(e):
        global contas_totais 
        if resultado.value and resultado.value[-1] != "*":
            resultado.value += "*"
            contas_totais += "*"
            pagina.update()

    def realizar_subtração(e):
        global contas_totais 
        if resultado.value and resultado.value[-1] != "-":
            resultado.value += "-"
            contas_totais += "-"
            pagina.update()

    def limpar(e):
        global contas_totais 
        resultado.value = ""
        contas_totais = ""
        pagina.update()

    def divisao(e):
        global contas_totais 
        if resultado.value and resultado.value[-1] != "/":
            resultado.value += "/"
            contas_totais += "/"
        pagina.update()

    def calcular_soma(e):
        global contas_totais 
        if resultado.value and contas_totais:
            try:
                contas_totais = str(eval(contas_totais))
                resultado.value = contas_totais
                pagina.update()
            except SyntaxError:
                resultado.value = "equação inválida"
                contas_totais = ""
                pagina.update()
                time.sleep(2)
                limpar(None)
            except NameError:
                resultado.value = "equação inválida"
                contas_totais = ""
                pagina.update()
                time.sleep(2)
                limpar(None)
            except ZeroDivisionError:
                resultado.value = "equação inválida"
                contas_totais = ""
                pagina.update()
                time.sleep(2)
                limpar(None)
        pagina.update()

    # Adicionando os widgets à página
    pagina.add(
        ft.Row([resultado, ft.ElevatedButton(text="D", width=60, on_click=remover_um_numero)]),
        ft.Row([
            ft.ElevatedButton("1", on_click=lambda e: add_num("1")),
            ft.ElevatedButton("2", on_click=lambda e: add_num("2")),
            ft.ElevatedButton("3", on_click=lambda e: add_num("3")),
            ft.IconButton(ft.icons.REMOVE, on_click=realizar_subtração)
        ]),
        ft.Row([
            ft.ElevatedButton("4", on_click=lambda e: add_num("4")),
            ft.ElevatedButton("5", on_click=lambda e: add_num("5")),
            ft.ElevatedButton("6", on_click=lambda e: add_num("6")),
            ft.IconButton(ft.icons.ADD, on_click=realizar_soma)
        ]),
        ft.Row([
            ft.ElevatedButton("7", on_click=lambda e: add_num("7")),
            ft.ElevatedButton("8", on_click=lambda e: add_num("8")),
            ft.ElevatedButton("9", on_click=lambda e: add_num("9")),
            ft.IconButton(ft.icons.AC_UNIT, on_click=limpar)

        ]),
        ft.Row([
            ft.ElevatedButton("0", on_click=lambda e: add_num("0")),
            ft.TextButton(text="*", width=50, on_click=multiplicar),
            ft.TextButton(text="=", width=50, on_click=calcular_soma),
            ft.TextButton(text="/", width=50, on_click=lambda e: divisao(None))
        ])
    )

# Inicia a aplicação
ft.app(target=main)
