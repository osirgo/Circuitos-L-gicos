-Español-

Nombre del proyecto: Compuertas Lógicas - Funciones Lógicas

Descripción:

Este módulo implementa funciones para las compuertas lógicas básicas: Buffer, Not, And, Nand, Or, Nor, Xor y Xnor. También incluye funciones para generar una tabla de condiciones y evaluar una compuerta lógica para una tabla de condiciones dada.

Funcionalidades:

Implementación de las compuertas lógicas básicas.
Generación de una tabla de condiciones.
Evaluación de una compuerta lógica para una tabla de condiciones.
Manejo de errores.

Argumentos:

Las funciones de las compuertas lógicas reciben uno o más valores booleanos como argumentos.
La función tabla recibe un número entero como argumento que indica el número de entradas.
La función evaluar recibe una lista de listas como argumento, donde cada lista interna representa una combinación de valores de entrada.

Retorno:

Las funciones de las compuertas lógicas retornan un valor booleano.
La función tabla retorna una lista de listas que representa la tabla de condiciones.
La función evaluar retorna una lista de valores booleanos, uno por cada combinación de valores de entrada en la tabla de condiciones.

Requisitos: Python 3

Ejemplo de uso: 


import LogicGates

Entradas = LogicGates.tabla(3)
E
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
LogicGates.evaluar(E, 'Xor')
False
True
True
False
True
False
False
True

Contacto: Si tiene alguna pregunta o comentario, no dude en contactarme.

Fecha de última actualización: 2024-02-05

Notas Finales:
Las funciones de las compuertas lógicas también pueden usarse con valores binarios (0 y 1) como argumentos.
La función evaluar puede usarse para evaluar cualquier función lógica que pueda expresarse como una combinación de las compuertas lógicas básicas.


-Inglés-

Project Name: Logic Gates - Logical Functions
Description:

This module implements functions for basic logic gates: Buffer, Not, And, Nand, Or, Nor, Xor, and Xnor. It also includes functions to generate a truth table and evaluate a logic gate for a given truth table.

Features:

Implementation of basic logic gates.
Generation of a truth table.
Evaluation of a logic gate for a truth table.
Error handling.

Arguments:

Logic gate functions receive one or more boolean values as arguments.
The table function receives an integer as an argument indicating the number of inputs.
The evaluate function receives a list of lists as an argument, where each inner list represents a combination of input values.

Return:

Logic gate functions return a boolean value.
The table function returns a list of lists that represents the truth table.
The evaluate function returns a list of boolean values, one for each combination of input values in the truth table.
Requirements: Python 3

Example of use:

import LogicGates

inputs = LogicGates.tabla(3)
inputs
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
LogicGates.evaluar(inputs, 'Xor')
False
True
True
False
True
False
False
True

Final Notes:
Logic gate functions can also be used with binary values (0 and 1) as arguments.
The evaluate function can be used to evaluate any logical function that can be expressed as a combination of basic logic gates.


-Portugués-

Nome do projeto: Portas Lógicas - Funções Lógicas

Descrição:

Este módulo implementa funções para as portas lógicas básicas: Buffer, Not, And, Nand, Or, Nor, Xor e Xnor. Também inclui funções para gerar uma tabela-verdade e avaliar uma porta lógica para uma tabela-verdade dada.

Funcionalidades:

Implementação das portas lógicas básicas.
Geração de uma tabela-verdade.
Avaliação de uma porta lógica para uma tabela-verdade.
Tratamento de erros.

Argumentos:

As funções das portas lógicas recebem um ou mais valores booleanos como argumentos.
A função 'tabela' recebe um número inteiro como argumento que indica o número de entradas.
A função 'avaliar' recebe uma lista de listas como argumento, onde cada lista interna representa uma combinação de valores de entrada.

Retorno:

As funções das portas lógicas retornam um valor booleano.
A função 'tabela' retorna uma lista de listas que representa a tabela-verdade.
A função 'avaliar' retorna uma lista de valores booleanos, um para cada combinação de valores de entrada na tabela-verdade.
Requisitos: Python 3

Exemplo de uso:

import LogicGates

entradas = LogicGates.tabla(3)
entradas
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
LogicGates.evaluar(entradas, 'Xor')
False
True
True
False
True
False
False
True

Observações finais:

As funções das portas lógicas também podem ser usadas com valores binários (0 e 1) como argumentos.
A função 'avaliar' pode ser usada para avaliar qualquer função lógica que possa ser expressa como uma combinação das portas lógicas básicas.
