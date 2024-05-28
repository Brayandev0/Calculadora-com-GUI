# Criador         : Brayan silva 
# função          : Calculadora com GUI
# versão          : 1.2
# data da criação : 28/05/2024


from PySide6.QtWidgets import QPushButton, QApplication, QVBoxLayout, QWidget, QMainWindow, QLabel, QLineEdit, QGridLayout, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QKeyEvent, QIcon
import sys
import math

# Iniciando a minha aplicação 

class Minha_aplicacao(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

#   definindo icones e titulo da calculadora 
        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QIcon("_internal/logo_para_o_icone_da_janela.ico"))

#   chamando funções importantes para o funcionamento do codigo 
        self.Widget_e_Layout()
        self.definindo_codigos_de_erros()
        self.definindo_menu_bar()
        self.definindo_fontes()

#   variaveis padrão 
        self.numeros_1ate9 = "1234567890"
        self.calculo_direito = ""

#   configurando o display
        self.minha_tela = QLineEdit()
        self.minha_tela.setReadOnly(True)
        self.minha_tela.setFont(self.fonte_grande)
        self.layout_central.addWidget(self.minha_tela, alignment=Qt.AlignTop)

#   definindo a grid de botões 
        self.grid = QGridLayout()
        self.layout_central.addLayout(self.grid)
        self.configurando_numeros()
#   definindo erros padrões 

    def definindo_codigos_de_erros(self):
        self.erro_305 =  "Esta conta irá ultrapassar limites do seu computador"
        self.erro_307 = "Potenciação inválida"
        self.erro_301 = "Não é possível dividir por 0"
        self.erro_303 = "Calculo invalido"
        self.erro_300 = "Digite algum número"

# definindo o menu bar (atalho,saida)
    def definindo_menu_bar(self):
        self.menu__bar = self.menuBar()
        menu = self.menu__bar.addMenu("Menu de interação")
        modo_sair = menu.addAction("Sair")
        ver_atalho = menu.addAction("Atalhos")
        modo_sair.triggered.connect(lambda: exit())
        ver_atalho.triggered.connect(lambda: self.tela_de_informacao())

#   definindo fontes padrões 
    def definindo_fontes(self):
        self.fonte_grande = QFont()
        self.fonte_grande.setPointSize(20)

#   configurando widget e layout 
    def Widget_e_Layout(self):
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        self.layout_central = QVBoxLayout()
        self.setCentralWidget(self.widget_central)
        self.widget_central.setLayout(self.layout_central)

#   realizando a potenciação com tratamento de erros 
    def potenciacao(self):
        if self.calculo_direito:
                try:
                    calculo_esquerdo = float(self.minha_tela.text())
                    resultado = math.pow(self.calculo_direito, calculo_esquerdo)
                    self.minha_tela.setText(str(resultado))
                    self.calculo_direito = ""
                    return True
                except OverflowError:
                    self.calculo_direito = ""
                    self.tela_de_erro(self.erro_305, 305)
                except ValueError:
                    self.calculo_direito = ""
                    self.tela_de_erro(self.erro_307, 307)

#   realizando o calculo e tratando a saida 
    def calcular(self):
            try:
                self.minha_tela.setText(str(eval(self.minha_tela.text())))
            except ZeroDivisionError:
                self.tela_de_erro(self.erro_301,301)
            except SyntaxError:
                self.tela_de_erro(self.erro_303, 303)
            except NameError:
                self.tela_de_erro(self.erro_303, 303)

#   verificando se existe valores inseridos
    def verificar(self):
        if not self.minha_tela.text():
            self.tela_de_erro(self.erro_300, 300)
            return False
        else:
            return True
        
#   configurando teclas inseridas e tratando 
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.text() in self.numeros_1ate9:
            self.minha_tela.insert(event.text())
        match event.text().lower():
            case "c":
                self.minha_tela.setText("")
            case "q":
                exit()
            case "d":
                self.minha_tela.backspace()
            case "-":
                self.add_a_tela("-")
            case "+":
                self.add_a_tela("+")
            case _:
                event.ignore()
#   definindo o pop up de atalho  
    def tela_de_informacao(self):
        caixa_De_dialogos = QMessageBox()
        caixa_De_dialogos.setWindowTitle("Atalhos")
        caixa_De_dialogos.setIcon
        caixa_De_dialogos.setStandardButtons(QMessageBox.StandardButton.Close)
        caixa_De_dialogos.setInformativeText("Atalhos Principais:\n\nPressione 'C' para Limpar a Tela.\n\nPressione 'Q' para Sair.\n\nPressione 'D' para excluir o ultimo número digitado \n \n")
        caixa_De_dialogos.exec()

#   função para adicionar os valores digitados a tela 
    def add_a_tela(self,texto : str):
            self.operadores = ["+","-","/","*","X","^","=","/"]
            if texto in self.numeros_1ate9:
                self.minha_tela.insert(texto)
            elif texto == "-" and not self.minha_tela.text():
                    self.minha_tela.insert("-")
            if self.verificar():
                
                self.meutexto.setText("")
                match texto:
                    case ".":
                        if self.minha_tela.text()[-1] != ".":
                            self.minha_tela.insert(".")
                    case "X":
                        if self.minha_tela.text()[-1] in self.operadores:
                                return False
                        self.minha_tela.insert("*")
                    case "+":
                        if self.minha_tela.text()[-1] in self.operadores:
                                return False
                        self.minha_tela.insert("+")
                    case "D":
                        return self.minha_tela.backspace()
                    case "/":
                        if self.minha_tela.text()[-1] in self.numeros_1ate9:
                            return self.minha_tela.insert("/")
                        return False
                    case "=":
                            if isinstance(self.calculo_direito,float):
                                return self.potenciacao()
                            return self.calcular()
                    case "-":
                        if self.minha_tela.text()[-1] not in self.operadores:
                            self.minha_tela.insert("-")
                    case "^":
                        self.calculo_direito = float(self.minha_tela.text())
                        self.minha_tela.setText("")
                        self.meutexto.setText(f"Digite o outro número da potenciação")
                    case "C":
                        return self.minha_tela.setText("")

#   definindo a tela dos pop up de erros 
    def tela_de_erro(Self,texto: str, erro : int):
        caixa = QMessageBox()
        Self.minha_tela.setText("")
        caixa.setStandardButtons(QMessageBox.Ok)
        caixa.button(QMessageBox.Ok).setText("Sair")
        caixa.setText(texto)
        caixa.setIcon(QMessageBox.Icon.Critical)
        caixa.setWindowTitle(f"Erro {erro}")
        caixa.exec()
#   configurando a função para adiar a execução
    def adiando_exec(self,funcao, texto: str):
        def executando():
            funcao(texto)
        return executando
#   definindo a grid de botões e configurando o clique dos botões 
    def configurando_numeros(self):
        executa_botao = self.adiando_exec
        self.botoes_layout = [
            ["C","D","/","^"],
            ["1","2","3","+"],
            ["4","5","6","-"],
            ["7","8","9","X"],
            ["","0",".","="]
        ]
        for num_coluna,coluna in enumerate(self.botoes_layout):
            for num,self.texto in enumerate(coluna):
                botao = QPushButton(self.texto)
                self.grid.addWidget(botao, num_coluna,num)
                botao.clicked.connect(executa_botao(self.add_a_tela, self.texto))
                botao.setFont(self.fonte_grande)
                if self.texto in self.numeros_1ate9 or self.texto == ".":
                    botao.setStyleSheet("Color: #ADD8E6")
                if self.texto not in self.numeros_1ate9 and self.texto != ".":
                    botao.setStyleSheet("background-color: #1E90FF; color: black")
#   definindo o QMessageBox dos pop up
    def Definindo_message_box(self):
        return QMessageBox()
    
#   Iniciando a aplicação e realizando configurações de estilo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("_internal/logo_para_o_icone_da_janela.ico"))
    window = Minha_aplicacao()
    window.resize(290,290)
    window.show()
    app.exec() 
