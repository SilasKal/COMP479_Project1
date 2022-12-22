def read_extract(input_filepath, output_filename):
    """
    reads in a given input file and extracts the body of all articles as a txt file and as a String
    this function is made to be used for reuters collection articles and only works for them properly
    """
    article_information = ''
    extract = False
    articles = []
    try:
        with open(input_filepath) as file:
            line = file.readline()
            while line:
                line = file.readline()
                if line.strip().startswith('<REUTERS'):  # extract all text after <REUTERS
                    extract = True
                if line.strip().startswith('</REUTERS>'):  # stop extracting after </REUTERS>
                    articles.append(article_information)
                    article_information = ''
                    extract = False
                if extract:
                    article_information += ' ' + line.strip()
        extract_body = False
        article_bodies = []
        curr_body = ''
        for article in articles:  # extracting the bodies from the whole information of the articles
            for index, letter in enumerate(article):
                if letter == '<':
                    if article[index:index + 6] == '<BODY>':  # start extracting after <BODY>
                        extract_body = True
                if extract_body:
                    curr_body += letter
                    if article[index:index + 7] == '</BODY>':  # stop extracting after </BODY>
                        article_bodies.append(
                            curr_body[6:-5])  # slice article bodies so that only raw text is extracted
                        extract_body = False
                        curr_body = ''
        article_bodies_str = ''
        for i in article_bodies:
            article_bodies_str += ' ' + i
        output(article_bodies_str, output_filename)
        return article_bodies_str
    except FileNotFoundError:
        print('File at that filepath does not exist. An empty output file will be created.')
        output('', output_filename)
        return ''


def output(text, filepath):
    with open(filepath, 'w') as f:
        f.write(text)
    f.close()
