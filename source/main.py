
def generate_data():
    return True

def get_object_name(objectWords,sentence):
    objectName = ""
    if len(objectWords) == 0:
        print('Error: cannot extract object name from empty string in sentence:'
              ,sentence)
    else:
        match objectWords[0]:
            case "":
                print('Error: cannot extract object name from empty string in sentence:'
                ,sentence,"\nMake sure you don't have any starting whitespace at the beginning of your sentence")
            case "a" | "A" | "an" | "AN" | "An" | "aN":
                objectName = (' ').join(objectWords[1:])
            case _:
                objectName = (' ').join(objectWords)
    return objectName

def add_sentence_to_app(sentence,app,parseContext):
    words = sentence.split(' ')
    sentenceContext = {}
    if len(words) == 0:
        pass
    elif words[-1] == "has:\n":
        parseContext["currentSubjectObject"] = get_object_name(words[:-1],sentence)
        print(parseContext["currentSubjectObject"])
    else:
        for idx, word in enumerate(words):
            match word.lower():
                case "has":
                    sentenceContext["currentSubjectObject"] = get_object_name(words[:idx],sentence)
                    sentenceContext["currentTargetObject"] = get_object_name(words[idx+1:],sentence)
                    print(sentenceContext["currentSubjectObject"])
                    print(sentenceContext["currentTargetObject"])
                case "is":
                    pass
                    # handle is between case
                case "are":
                    pass
                case "of":
                    pass
                case "between":
                    pass
                case "either":
                    pass
                case "and":
                    pass
                case "or":
                    pass
                case _:
                    pass
    return app,parseContext

def add_line_to_app(line,app,parseContext):
    sentences = line.split('. ') #Deliberately does not catch floats formats
    if len(sentences) >= 3:
        print("Error: A line can only have 1 or 2 sentences but",len(sentences),
              "are present in:",('.').join(sentences),
              "\nMake sure you don't have trailing spaces at the end of your sentence")
    else:
        for sentence in sentences:
            app,parseContext = add_sentence_to_app(sentence,app,parseContext)
    return app,parseContext

def parse_file(path):
    app = {}
    parseContext = {}
    with open(path,'r') as fileContent:
        for line in fileContent:
            app,parseContext = add_line_to_app(line,app,parseContext)
    return app

if __name__ == '__main__':
    print('Parsing Fraz file')
    parse_file('../examples/models/Airlines.fraz')
    print('Parsing Ended')

