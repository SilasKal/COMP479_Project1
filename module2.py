import nltk


def tokenize(input_filepath='output_module1.txt', output_filename='output_module2.txt', remove_non_alphanumeric=True):
    """
    tokenizes given text and returns list of tokens as a txt file and as a String
    """
    try:
        with open(input_filepath, 'r') as f:
            text = f.read()
        tokens = nltk.word_tokenize(text)
        if remove_non_alphanumeric:
            tokens = [token for token in tokens if any(charac.isalnum() for charac in token) and token != '']
        output(tokens, output_filename)
        return tokens
    except FileNotFoundError:
        print('File at that filepath does not exist. An empty output file will be created.')
        output([], output_filename)
        return []


def output(input_list, filepath):
    with open(filepath, 'w') as f:
        for item in input_list:
            f.write(item + '\n')
    f.close()
