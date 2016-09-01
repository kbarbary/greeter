"""what this module contains"""


def get_greeting(add_space=False):
    """Construct a greeting.

    Parameters
    ----------
    add_space : bool, optional
        Add a space after output.

    Returns
    -------
    s : str
        The greeting.
    """
    s = "hello"
    if add_space:
        s += " "

    return s


def get_audience(end="!"):
    """Construct an audience.

    Parameters
    ----------
    end : str
        Ending punctuation.

    Returns
    -------
    Target audience.
    """

    return "world" + end

