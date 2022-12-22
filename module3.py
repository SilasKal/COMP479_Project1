def make_lowercase(input_filepath='output_module2.txt', output_filename='output_module3.txt'):
    """
    makes given text lowercase and returns it in a txt file and as a List
    the text should be in a txt file
    """
    tokens = []
    try:
        with open(input_filepath) as file:
            line = file.readline()
            tokens.append(line)
            while line:
                line = file.readline()
                tokens.append(line)
        tokens_lowercase = [token.lower() for token in tokens if token != '']
        output(tokens_lowercase, output_filename)
        return tokens_lowercase
    except FileNotFoundError:
        print('File at that filepath does not exist. An empty output file will be created.')
        output([], output_filename)
        return []


def output(input_list, filepath):
    with open(filepath, 'w') as f:
        for item in input_list:
            f.write(item)
    f.close()
