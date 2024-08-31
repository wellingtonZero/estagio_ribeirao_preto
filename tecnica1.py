def fibonacci_bool(num):
    if num < 0:
        return False

    # caso o num seja 0 ou 1 já será retornado como verdadeiro
    if num == 0 or num == 1:
        return True

    # caso o número seja superior a 0 e 1 vamos gerar uma sequência
    # Inicia os dois primeiros números da sequência e segue usando o restante com o while
    a, b = 0, 1

    # Gera a sequência até encontrar o número ou ultrapassá-lo
    while b < num:
        a, b = b, a + b

    # Verifica se o número pertence à sequência retornando ou verdadeiro ou falso
    return b == num


# Exemplo de uso: Verificar se um número pertence à sequência de Fibonacci
numero = int(input("Digite um número: "))
if fibonacci_bool(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
