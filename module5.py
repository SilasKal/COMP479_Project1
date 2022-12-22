import nltk


def remove_stop_words(stop_words=nltk.corpus.stopwords.words('english'), input_filepath='output_module4.txt',
                      output_filename='output_module5.txt'):
    """
    removes given list of stop words from given text and returns filtered text
    the text should be in a txt file and tokenized, with each written in a separate line
    you should use nltk.download('stopwords') when using the function for the first time
    """
    try:
        tokens = []
        with open(input_filepath) as file:
            line = file.readline().strip()
            tokens.append(line)
            while line:
                line = file.readline()
                tokens.append(line.strip())
        # print(words)
        filtered_words = [token for token in tokens if token not in stop_words and token != '']
        output(filtered_words, output_filename)
        return filtered_words
    except FileNotFoundError:
        print('File at that filepath does not exist. An empty output file will be created.')
        output([], output_filename)
        return []


def output(input_list, filepath):
    with open(filepath, 'w') as f:
        for item in input_list:
            f.write(item + '\n')
    f.close()
