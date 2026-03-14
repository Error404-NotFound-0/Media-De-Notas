def main():
    while True:
        nota = []
        print('\n'*10, '-'*10, 'CALCULADOR DE MÉDIA', '-'*10)
        print('\n', '-'*50, '\n INSTRUÇÕES: \n\n INSIRA UMA NOTA POR VEZ; \n QUANDO TERMINAR, DIGITE: "FIM".\n', '-'*50)
        while True:
            entrada = input('\n Insira a nota, ou digite "FIM": ')
            entrada = entrada.replace(',', '.')
            try:
                entrada = float(entrada)
                nota.append(entrada)
            except:
                if entrada.lower() == 'fim':
                    if nota:
                        media = (sum(nota))/len(nota)
                        print(f'\n\n -- A média é: {media: .2f}\n\n')
                    recomecar()
                    break

                else:
                    print('Insira apena um número por vez, ou digite "FIM".')


def recomecar():
    while True:
        e = input("\n Você deseja fazer novamente? (S/N)")
        if e.lower() == 's':
            break
        if e.lower() == 'n':
            print('\n Adeus, até a próxima!\n')
            quit()
        else:
            print('Escolha inválida.')

main()
