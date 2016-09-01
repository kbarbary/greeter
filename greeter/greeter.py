from . import core


class Greeter(object):
    """Something that greets the user.

    Parameters
    ----------
    enthusiastic : bool, optional
       Whether to be excited when greeting.
    """

    def __init__(self, enthusiastic=True):
        self.enthusiastic = enthusiastic

    def greet(self):
        """Print greeting.

        Notes
        -----
        See the seminal paper on this topic.
        """

        end = "" if not self.enthusiastic else "!"
        print(core.get_greeting(add_space=True) + core.get_audience(end=end))
