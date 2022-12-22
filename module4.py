import nltk


def porter_stemmer(input_filepath='output_module3.txt', output_filename='output_module4.txt'):
    """
    stems given tokens  using the Porter Stemmer as a txt file and as a List
    the tokens should be in a txt file with each token written in a separate line
    """
    try:
        stemmer = nltk.PorterStemmer()
        tokens = []
        with open(input_filepath) as file:
            line = file.readline().strip()
            tokens.append(line)
            while line:
                line = file.readline()
                tokens.append(line.strip())
        stemmed_tokens = [stemmer.stem(word) for word in tokens if word != '']
        output(stemmed_tokens, output_filename)
        return stemmed_tokens
    except FileNotFoundError:
        print('File at that filepath does not exist. An empty output file will be created.')
        output([], output_filename)
        return []


def output(input_list, filepath):
    with open(filepath, 'w') as f:
        for item in input_list:
            f.write(item + '\n')
    f.close()
