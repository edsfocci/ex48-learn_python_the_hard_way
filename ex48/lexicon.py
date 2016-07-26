GRAMMAR = {
    'direction':    {'north', 'south', 'east', 'west',
                    'down', 'up', 'left', 'right', 'back'},
    'verb':         {'go', 'stop', 'kill', 'eat'},
    'stop':         {'the', 'in', 'of', 'from', 'at', 'it'},
    'noun':         {'door', 'bear', 'princess', 'cabinet'}
}

def scan(words):
    words = words.split()

    def map_grammar(word):
        for key in GRAMMAR:
            if word in GRAMMAR[key]:
                return (key, word)

        try:
            return ('number', int(word))
        except ValueError:
            return ('error', word)

    return list(map(map_grammar, words))
