#Gerador de piadas com TRADUTOR

#importacao biblioteca externa pelo 'PIP INSTALL' (pyjokes e deep_tranlator)
import pyjokes
from deep_translator import GoogleTranslator # lembrar que para parte da biblioteca usa o 'from + nome da bibli + import + o que se deseja'

#dimunuir nome de uma funcao da biblioteca
tradutor = GoogleTranslator(source="auto", target='pt') #dentro do parametro designa o idioma traduzido

#loop para usuario escolher se quer ou nao encerrar 
while True:
    piada = pyjokes.get_joke()    #caso quisesse todas as piadas da biblioteca deixaria no plural '.get_jokes()'
    piada_traduzida = tradutor.translate(piada)    # chamar a piada

    print(piada_traduzida) # mostra a piada na tela

    repetir = input('Gerar outra Piada? (s/n)').lower()

    if repetir == 's':
        continue
    else:
        break


