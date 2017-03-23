A good starting point for a new python project. Uses [pytest](http://doc.pytest.org/en/latest/contents.html) for testing.General idea from [Learn Python the hard way](https://learnpythonthehardway.org/book/ex46.html).

To use:

1. Fork repo as new project
1. `mkvirtualenv project`
1. `pip install -r requirements.txt`
1. `pip install -e .` >>> See: [pytest docs on error](http://doc.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules)
1. `pytest` should return one successful test
1. Change the package name, update setup.py, etc.

