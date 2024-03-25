import numpy as np

def gerar_matriz():
    try:
        #escolhe a ordem da matriz no formato NumeroXNumero, parte a string no x e pega o primeiro elemento
        ordem = input("Digite a ordem da matriz (ex:2x2):").split('x')
        #transforma a ordem em inteiro para caber nos paramentos de np.zeros
        linhas =int(ordem[0])
        colunas = int(ordem[1])
        #faz uma matriz com a ordem requerida 
        matriz = np.zeros((linhas,colunas))
        #esse looping eh o looping das linhas
       
        for i in range(linhas):
            #ja esse vai passar pelos elementos de cada linha
        
            for j in range(colunas):
                #e com essa notacao vai substituindo os elementos nos respectivos lugares
                #looping infinito ate que o valor seja valido
                while True:
                    try:
                         matriz[i][j] = (eval(input(f"Digite o {j+1} elemento da {i+1} linha: ")))
                         break
                    #exceção para divisão por 0
                    except ZeroDivisionError:
                        print("Divisão por 0 não é aceita.")
                    #exceção para digito inválido
                    except (SyntaxError, NameError, TypeError):
                        print("Entrada inválida, digite novamente.")

        print(f"A matriz gerada de ordem {linhas}x{colunas} é:  \n{matriz}\n ") 
            #verifica se a matriz eh quadratica
        if linhas == colunas:
            #calcula o determinante
            det = np.linalg.det(matriz)
            #mostra o valor do determinante
            print(f"O determinante da matriz é {det}")
            #verifica se o determinante difere de 0
            try:
                matriz_inversa = np.linalg.inv(matriz)
                print(f"O inverso da matriz é : \n{matriz_inversa}")

            except np.linalg.LinAlgError:
                print(f"A matriz é singular, não possui inversa, pois o determinante é igual a 0.")
        else:
            print("Matriz não quadratica, não possui determinante e nem inversa.")
    except ValueError:
        print("Valor não aceito, por favor inserir um válido.")
gerar_matriz()
