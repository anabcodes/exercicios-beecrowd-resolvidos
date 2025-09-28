def monotonosMaximaisNaoTriviais(trecho, n):
    i = 0
    contador = 0

    while i < n:
        j = i + 1

        while j < n and trecho[j] == trecho[i]:
            j += 1

        comprimento_monotono = j - i
        if comprimento_monotono >= 2 and trecho[i] == 'a':
            contador += comprimento_monotono

        i = j

    return contador


n = int(input())
trecho = input()
print(monotonosMaximaisNaoTriviais(trecho, n))
