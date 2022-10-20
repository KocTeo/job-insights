from src.counter import count_ocurrences


def test_counter():
    count_js = count_ocurrences('src/jobs.csv', 'javascript')
    count_py = count_ocurrences('src/jobs.csv', 'python')
    assert count_js == 122
    assert count_py == 1639
