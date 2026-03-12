def main():
    while True:
        permitido = True
        nota = []
        print('\n'*10, '-'*10, 'CALCULADOR DE MÉDIA', '-'*10)
        print('\n', '-'*50, '\n INSTRUÇÕES: \n\n INSIRA UMA NOTA POR VEZ; \n QUANDO TERMINAR, DIGITE: "FIM".\n', '-'*50)
    
        rodando = True
        while rodando:
            entrada = input('\n Insira a nota, ou digite "FIM": ')
            entrada = entrada.replace(',', '.')
            try:
                entrada = float(entrada)
                nota.append(entrada)
            except:
                if len(nota) == 0:
                    rodando = False
                    permitido = False
                    
                if entrada.lower() == 'fim' and permitido == True:
                    media = (sum(nota))/len(nota)
                    print(f'\n\n -- A média é: {media: .2f}\n\n')
                    while rodando:
                        e = input('Deseja fazer novamente? (S/N): ').strip().lower()
                        if e in ['n', 's']:
                            if e == 'n':
                                quit()
                            else:
                                rodando = False
                        else:
                            print('Escolha inválida!')  
                else:
                    print('Insira apena um número por vez, ou digite "FIM".')
main()
