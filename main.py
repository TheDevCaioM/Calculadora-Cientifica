import math
import os


class CalculadoraCientifica:
    def __init__(self):
        self.historico = []
        self.memoria = 0
        self.radianos = True  # True para radianos, False para graus

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def exibir_logo(self):
        print(
            """

  ╔══════════════════════════════════════════╗
  ║                 CALCULADORA              ║
  ║                                          ║
  ║        ██████╗ █████╗ ██╗ ██████╗        ║
  ║       ██╔════╝██╔══██╗██║██╔═══██╗       ║
  ║       ██║     ███████║██║██║   ██║       ║
  ║       ██║     ██╔══██║██║██║   ██║       ║
  ║       ╚██████╗██║  ██║██║╚██████╔╝       ║
  ║        ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝        ║
  ╚══════════════════════════════════════════╝
                                                          
        """
        )

    def exibir_menu(self):
        print("=" * 50)
        print("           OPERAÇÕES DISPONÍVEIS")
        print("=" * 50)
        print(" [1]  Adição (+)")
        print(" [2]  Subtração (-)")
        print(" [3]  Multiplicação (*)")
        print(" [4]  Divisão (/)")
        print(" [5]  Potência (x^y)")
        print(" [6]  Raiz Quadrada (√)")
        print(" [7]  Exponencial (e^x)")
        print(" [8]  Logaritmo Natural (ln)")
        print(" [9]  Logaritmo Base 10 (log)")
        print(" [10] Seno (sin)")
        print(" [11] Cosseno (cos)")
        print(" [12] Tangente (tan)")
        print(" [13] Fatorial (!)")
        print(" [14] Porcentagem (%)")
        print(" [15] Valor Absoluto (|x|)")
        print("-" * 50)
        print(" [H]  Ver Histórico")
        print(" [C]  Limpar Histórico")
        print(" [M]  Memória")
        print(" [R]  Alternar Radianos/Graus")
        print(" [X]  Sair")
        print("=" * 50)

    def obter_numero(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Erro: Digite um número válido!")

    def obter_opcao(self):
        return input("\nDigite a opção desejada: ").upper().strip()

    def adicionar_historico(self, operacao, resultado):
        entrada = f"{operacao} = {resultado}"
        self.historico.append(entrada)
        if len(self.historico) > 10:
            self.historico.pop(0)

    def exibir_historico(self):
        print("\n" + "=" * 50)
        print("              HISTÓRICO")
        print("=" * 50)
        if not self.historico:
            print(" Nenhuma operação realizada")
        else:
            for i, item in enumerate(self.historico, 1):
                print(f" {i:2d}. {item}")
        print("=" * 50)

    def menu_memoria(self):
        while True:
            print("\n" + "-" * 30)
            print("          MEMÓRIA")
            print("-" * 30)
            print(f" Valor atual: {self.memoria}")
            print(" [1] Armazenar valor")
            print(" [2] Recuperar valor")
            print(" [3] Limpar memória")
            print(" [4] Adicionar à memória")
            print(" [5] Voltar")
            print("-" * 30)

            opcao = input("Escolha: ")

            if opcao == "1":
                self.memoria = self.obter_numero("Digite o valor para armazenar: ")
                print(f"Valor {self.memoria} armazenado na memória")
            elif opcao == "2":
                print(f"Valor recuperado: {self.memoria}")
                return self.memoria
            elif opcao == "3":
                self.memoria = 0
                print("Memória limpa")
            elif opcao == "4":
                valor = self.obter_numero("Digite o valor para adicionar: ")
                self.memoria += valor
                print(f"Memória atualizada: {self.memoria}")
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

    def alternar_modo_angular(self):
        self.radianos = not self.radianos
        modo = "Radianos" if self.radianos else "Graus"
        print(f"Modo angular alterado para: {modo}")

    def converter_angulo(self, angulo):
        if not self.radianos:
            return math.radians(angulo)
        return angulo

    def adicao(self):
        print("\n--- ADIÇÃO ---")
        a = self.obter_numero("Digite o primeiro número: ")
        b = self.obter_numero("Digite o segundo número: ")
        resultado = a + b
        self.adicionar_historico(f"{a} + {b}", resultado)
        return resultado

    def subtracao(self):
        print("\n--- SUBTRAÇÃO ---")
        a = self.obter_numero("Digite o primeiro número: ")
        b = self.obter_numero("Digite o segundo número: ")
        resultado = a - b
        self.adicionar_historico(f"{a} - {b}", resultado)
        return resultado

    def multiplicacao(self):
        print("\n--- MULTIPLICAÇÃO ---")
        a = self.obter_numero("Digite o primeiro número: ")
        b = self.obter_numero("Digite o segundo número: ")
        resultado = a * b
        self.adicionar_historico(f"{a} × {b}", resultado)
        return resultado

    def divisao(self):
        print("\n--- DIVISÃO ---")
        a = self.obter_numero("Digite o numerador: ")
        b = self.obter_numero("Digite o denominador: ")
        if b == 0:
            print("Erro: Divisão por zero!")
            return None
        resultado = a / b
        self.adicionar_historico(f"{a} ÷ {b}", resultado)
        return resultado

    def potencia(self):
        print("\n--- POTÊNCIA ---")
        base = self.obter_numero("Digite a base: ")
        expoente = self.obter_numero("Digite o expoente: ")
        resultado = math.pow(base, expoente)
        self.adicionar_historico(f"{base}^{expoente}", resultado)
        return resultado

    def raiz_quadrada(self):
        print("\n--- RAIZ QUADRADA ---")
        numero = self.obter_numero("Digite o número: ")
        if numero < 0:
            print("Erro: Não é possível calcular raiz de número negativo!")
            return None
        resultado = math.sqrt(numero)
        self.adicionar_historico(f"√{numero}", resultado)
        return resultado

    def exponencial(self):
        print("\n--- EXPONENCIAL ---")
        numero = self.obter_numero("Digite o expoente: ")
        resultado = math.exp(numero)
        self.adicionar_historico(f"e^{numero}", resultado)
        return resultado

    def logaritmo_natural(self):
        print("\n--- LOGARITMO NATURAL ---")
        numero = self.obter_numero("Digite o número: ")
        if numero <= 0:
            print("Erro: Logaritmo indefinido para números ≤ 0!")
            return None
        resultado = math.log(numero)
        self.adicionar_historico(f"ln({numero})", resultado)
        return resultado

    def logaritmo_base10(self):
        print("\n--- LOGARITMO BASE 10 ---")
        numero = self.obter_numero("Digite o número: ")
        if numero <= 0:
            print("Erro: Logaritmo indefinido para números ≤ 0!")
            return None
        resultado = math.log10(numero)
        self.adicionar_historico(f"log10({numero})", resultado)
        return resultado

    def seno(self):
        print("\n--- SENO ---")
        angulo = self.obter_numero("Digite o ângulo: ")
        angulo_conv = self.converter_angulo(angulo)
        resultado = math.sin(angulo_conv)
        modo = "rad" if self.radianos else "°"
        self.adicionar_historico(f"sin({angulo}{modo})", resultado)
        return resultado

    def cosseno(self):
        print("\n--- COSSENO ---")
        angulo = self.obter_numero("Digite o ângulo: ")
        angulo_conv = self.converter_angulo(angulo)
        resultado = math.cos(angulo_conv)
        modo = "rad" if self.radianos else "°"
        self.adicionar_historico(f"cos({angulo}{modo})", resultado)
        return resultado

    def tangente(self):
        print("\n--- TANGENTE ---")
        angulo = self.obter_numero("Digite o ângulo: ")
        angulo_conv = self.converter_angulo(angulo)

        # Verificar se o cosseno é zero (tangente indefinida)
        if math.cos(angulo_conv) == 0:
            print("Erro: Tangente indefinida para este ângulo!")
            return None

        resultado = math.tan(angulo_conv)
        modo = "rad" if self.radianos else "°"
        self.adicionar_historico(f"tan({angulo}{modo})", resultado)
        return resultado

    def fatorial(self):
        print("\n--- FATORIAL ---")
        numero = self.obter_numero("Digite o número: ")

        if numero < 0 or numero != int(numero):
            print("Erro: Fatorial definido apenas para inteiros não negativos!")
            return None

        numero = int(numero)
        resultado = math.factorial(numero)
        self.adicionar_historico(f"{numero}!", resultado)
        return resultado

    def porcentagem(self):
        print("\n--- PORCENTAGEM ---")
        valor = self.obter_numero("Digite o valor: ")
        percentual = self.obter_numero("Digite a porcentagem: ")
        resultado = (valor * percentual) / 100
        self.adicionar_historico(f"{percentual}% de {valor}", resultado)
        return resultado

    def valor_absoluto(self):
        print("\n--- VALOR ABSOLUTO ---")
        numero = self.obter_numero("Digite o número: ")
        resultado = abs(numero)
        self.adicionar_historico(f"|{numero}|", resultado)
        return resultado

    def executar(self):
        while True:
            self.limpar_tela()
            self.exibir_logo()

            # Exibir modo angular atual
            modo_angular = "Radianos" if self.radianos else "Graus"
            print(f"Modo angular: {modo_angular}")
            print(f"Memória: {self.memoria}")

            self.exibir_menu()

            opcao = self.obter_opcao()

            if opcao == "X":
                print("\nObrigado por usar a Calculadora Científica!")
                print("\nDesenvolvido por: https://github.com/TheDevCaioM")
                print(
                    """

              ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗
             ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
             ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
             ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
             ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
              ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

                            TheDevCaioM
                """
                )
                break
            elif opcao == "H":
                self.exibir_historico()
                input("\nPressione Enter para continuar...")
            elif opcao == "C":
                self.historico.clear()
                print("Histórico limpo!")
                input("\nPressione Enter para continuar...")
            elif opcao == "M":
                self.menu_memoria()
                input("\nPressione Enter para continuar...")
            elif opcao == "R":
                self.alternar_modo_angular()
                input("\nPressione Enter para continuar...")
            else:
                try:
                    opcao_num = int(opcao)
                    resultado = None

                    if opcao_num == 1:
                        resultado = self.adicao()
                    elif opcao_num == 2:
                        resultado = self.subtracao()
                    elif opcao_num == 3:
                        resultado = self.multiplicacao()
                    elif opcao_num == 4:
                        resultado = self.divisao()
                    elif opcao_num == 5:
                        resultado = self.potencia()
                    elif opcao_num == 6:
                        resultado = self.raiz_quadrada()
                    elif opcao_num == 7:
                        resultado = self.exponencial()
                    elif opcao_num == 8:
                        resultado = self.logaritmo_natural()
                    elif opcao_num == 9:
                        resultado = self.logaritmo_base10()
                    elif opcao_num == 10:
                        resultado = self.seno()
                    elif opcao_num == 11:
                        resultado = self.cosseno()
                    elif opcao_num == 12:
                        resultado = self.tangente()
                    elif opcao_num == 13:
                        resultado = self.fatorial()
                    elif opcao_num == 14:
                        resultado = self.porcentagem()
                    elif opcao_num == 15:
                        resultado = self.valor_absoluto()
                    else:
                        print("Opção inválida!")
                        input("\nPressione Enter para continuar...")
                        continue

                    if resultado is not None:
                        print(f"\nResultado: {resultado}")

                    input("\nPressione Enter para continuar...")

                except ValueError:
                    print("Opção inválida!")
                    input("\nPressione Enter para continuar...")


def main():
    calculadora = CalculadoraCientifica()
    calculadora.executar()


if __name__ == "__main__":
    main()
