from module1 import read_extract
from module2 import tokenize
from module3 import make_lowercase
from module4 import porter_stemmer
from module5 import remove_stop_words


def main():
    """
    main function which implements loop to running the pipeline for the first five documents of the reuters21578
    collection
    """
    prefix_reuters = 'reuters21578/reut2-00'
    for number in range(0, 5):
        num = str(number)
        read_extract(prefix_reuters + num + '.sgm', 'output_module1_document' + num)
        tokenize('output_module1_document' + num, 'output_module2_document' + num, True)
        make_lowercase('output_module2_document' + num, 'output_module3_document' + num)
        porter_stemmer('output_module3_document' + num, 'output_module4_document' + num)
        remove_stop_words(input_filepath='output_module4_document' + num,
                          output_filename='output_module5_document' + num)


def testing():
    if test1() and test2() and test3() and test4() and test5():
        print('Passed all tests. ')
    else:
        print('Failed tests.')


def test1():
    test_passed = True
    read_extract('reuters21578/reut2-013.sgm', 'output_module1_testcase1')
    if read_extract('testcases/testcase2_module1.txt', 'output_module1_testcase2') != '':
        test_passed = False
    return test_passed


def test2():
    test_passed = True
    if tokenize('testcases/testcase1_module2.txt', 'output_module2_testcase1') != ['Test-word']:
        test_passed = False
    if tokenize('testcases/testcase2_module2.txt', 'output_module2_testcase2') != ['Test', 'sentence']:
        test_passed = False
    if tokenize('testcases/testcase3_module2.txt', 'output_module2_testcase3') != ['672', 'number', 'token']:
        test_passed = False
    return test_passed


def test3():
    test_passed = True
    if make_lowercase('testcases/testcase1_module3.txt', 'output_module3_testcase1') != ['word\n', 'word']:
        test_passed = False  # string
    if make_lowercase('testcases/testcase2_module3.txt', 'output_module3_testcase2') != ['5678\n', 'test\n']:
        test_passed = False  # number
    if make_lowercase('testcases/testcase3_module3.txt', 'output_module3_testcase3') != ['spec!l\n', 'w0rd\n', 'wo,rd']:
        print(make_lowercase('testcases/testcase3_module3.txt', 'output_module3_testcase3'))
    return test_passed


def test4():
    test_passed = True
    if porter_stemmer('testcases/testcase1_module4.txt', 'output_module4_testcase1') != ['play', 'liefen', 'laufen']:
        print(porter_stemmer('testcases/testcase1_module4.txt', 'output_module4_testcase1'))
        test_passed = False
    if porter_stemmer('testcases/testcase2_module4.txt', 'output_module4_testcase2') != ['5679', 'test']:
        test_passed = False
    if porter_stemmer('testcases/testcase3_module4.txt', 'output_module4_testcase3') != ['playing playing play']:
        test_passed = False
    return test_passed


def test5():
    test_passed = True
    if remove_stop_words(input_filepath='testcases/testcase1_module5.txt',
                         output_filename='output_module5_testcase1') != ['if if if']:
        test_passed = False
    if remove_stop_words(input_filepath='testcases/testcase2_module5.txt',
                         output_filename='output_module5_testcase2') != ['remove', '7395']:
        test_passed = False
    return test_passed


if __name__ == "__main__":
    testing()
    main()
