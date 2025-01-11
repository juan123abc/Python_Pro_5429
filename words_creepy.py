meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'OMG': 'Expresion de asombro',
            'NASHE': 'Algo asombroso o divertido esta pasando',
            'WTF': 'Que carajos?',
            'AESTHETIC': 'Expresion usada para definir cierto estilo',
            'GRWM': 'Expresion usada para: Alistate conmigo',
            'NEA': 'Persona con corte de cabello el 7',
            'BRUH': 'Expresion usada para cualquier cosa',
            'GG': 'Great Game',
            'SHIPPEAR': 'Juntar a dos personas o personajes en un romance en mi imaginacion',
            'PRIME': 'Persona que se encuentra en el mejor punto de su carrera o existencia',
            'HYPE': 'Una emocion muy grande',
            'F': 'Es cuando es malo o lamentable',
    
               }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print('Aqui esta el significado de tu palabra:', meme_dict[word])
else:
    print('Ya que no lo tengo, porque no usas Google?')
