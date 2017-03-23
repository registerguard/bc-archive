Downloading videos from Brightcove for our archive.

To use:

1. Fork repo as new project
1. `mkvirtualenv project`
1. `pip install -e .` >>> See: [pytest docs on error](http://doc.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules)
1. `pytest` should return one successful test
1. Change the package name, update setup.py, etc.

# Notes

This script is very rudimentary and has had little development. The script works but more thinking is needed regarding how and where these files will be downloaded to. How do we iterate over different pages of results (default 25, max 100, we have 800+ videos). Should we store on in-house server? How to get files there? How to keep updated?