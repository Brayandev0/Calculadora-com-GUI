]![Calculadora principal](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/a8288e92-7efe-4793-88a1-e25b07d2a85c)

Utilizei a biblioteca PyQt6 para criar a minha calculadora
coloquei diversos tipos de operações como : potenciação, divisão,multiplicação,soma,subtração,operações com numeros decimais 

coloquei também funções para remover totalmente os dados na tela ( C ) 
e função para remover o ultimo numero digitado ( D )

coloquei também um menu de opções para facilitar o uso 

![menu ](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/ad24544e-2059-46a7-afa7-a24c6396014a)

coloquei diversos atalhos no teclado para facilitar a interação do usuario 

![atalho de teclas](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/0e22c90e-c511-4acc-9254-318bd54e364a)

configurei pop ups de erros na calculadora para informar ao usuario erros no calculo 

erros :


Caso o usuario tente realizar uma divisão por zero :

![erro_divisao_0](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/452c42ac-d190-40e9-99e1-69da5b6db025)

Caso o usuario tente realizar uma potenciação muita grande, para evitar danos ao computador o python retorna um erro por padrão 
eu criei um pop up para este erro :

![erro potenciação](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/fde04e75-bf85-4acd-b2c0-f761deac5131)

Caso o usuario tente inserir operados sem ter nenhum numero inserido retornara um erro :
( menos o operador - )

![erro_insira_um_numero](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/11a3c6f6-0f0d-4f10-b7c7-ea3245b94114)

Caso o úsuario insira algum calculo invalido será retornado um erro especifico :

![calculo_invalido](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/39df4db9-a55d-4cde-8bf9-930e772fbb91)


limitei também a adição de operadores, para impedir o usuario de inserir varios operadores seguidos ex : ++++

limitei também a entrada de teclas do teclado, impossibilitando injeções de código 
apenas as teclas do atalho serão adicionadas

limitei o display para somente leitura de dados 
