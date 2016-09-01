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
        self.outputs = None

    def greet(self):
        """Print greeting.

        Notes
        -----
        See the seminal paper on this topic.
        """

        end = "" if not self.enthusiastic else "!"
        self.message = core.get_greeting(add_space=True) + \
                       core.get_audience(end=end)

        print(self.message)
