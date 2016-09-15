greeter
=======

_Hello World Python package_ by kbarbary & drphilmarshall

![badge-img](https://img.shields.io/badge/Made%20at-%23AstroHackWeek-8063d5.svg?
style=flat)
[![build status](https://api.travis-ci.org/kbarbary/greeter.svg)](https://travis-ci.org/kbarbary/greeter)

This repository does the least it can to illustrate a few
components of packaging in Python:

- Repository layout and Python package layout
- A `setup.py` file
- Generating documentation with Sphinx
- Testing with py.test
- Continuous integration with Travis

We've tried to get all these working with minimal content and
configuration to make it easier to understand how all the pieces fit
together. This is meant as a teaching tool rather than a complete
package template. For a very nice package template aimed at scientific
Python, see https://github.com/uwescience/shablona. It also has much
more complete explanations!

To run things
-------------

**Install the package:** `./setup.py install`. Run `./setup.py --help`
for more options.

**Build docs:** Run `make html` from the `docs` directory. Build HTML
  pages will be in `docs/_build/html` which you can view locally in
  your browser.

**Run tests:** Install [pytest](http://pytest.org) and run `py.test`
  in the root of the repository. It discovers tests in `tests` and
  runs them.


License
-------

This package is licensed under the MIT license.