![Calculadora principal](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/a8288e92-7efe-4793-88a1-e25b07d2a85c)

Criei uma calculadora com a biblioteca PyQt6, incluindo várias operações como potenciação, divisão, multiplicação, soma, subtração e cálculos com números decimais.

Além das funções básicas, adicionei:

Botão "C": Limpa todos os dados da tela.
Botão "D": Remove o último dígito digitado, facilitando correções.
Menu de opções: Para tornar o uso mais fácil e intuitivo.
Minha calculadora tem uma interface amigável e prática, ideal para várias necessidades de cálculo.

![menu ](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/ad24544e-2059-46a7-afa7-a24c6396014a)

coloquei diversos atalhos no teclado para facilitar a interação do usuario 

![atalho de teclas](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/0e22c90e-c511-4acc-9254-318bd54e364a)

Configurei pop-ups de erros na calculadora para informar ao usuário sobre problemas no cálculo.

Erros tratados:

Divisão por zero:
Se o usuário tentar dividir por zero, aparece um pop-up de erro.


![erro_divisao_0](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/452c42ac-d190-40e9-99e1-69da5b6db025)

Potenciação muito grande:
Para evitar danos ao computador, o Python retorna um erro por padrão. Criei um pop-up específico para este caso.

![erro potenciação](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/fde04e75-bf85-4acd-b2c0-f761deac5131)

Operadores sem número:
Se o usuário tentar inserir operadores sem números (exceto o operador "-"), um erro é retornado.

![erro_insira_um_numero](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/11a3c6f6-0f0d-4f10-b7c7-ea3245b94114)

Cálculo inválido:
Qualquer cálculo inválido retorna um erro específico.

![calculo_invalido](https://github.com/Brayandev0/Calculadora-com-GUI/assets/84828739/39df4db9-a55d-4cde-8bf9-930e772fbb91)


Outras melhorias:

Limitei a adição de operadores para impedir inserções como "++++".
Restrição de teclas do teclado para evitar injeções de código, permitindo apenas atalhos específicos.
O display foi configurado para ser somente leitura.
