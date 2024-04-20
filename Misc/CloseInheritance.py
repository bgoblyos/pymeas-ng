import logging

# Class to close the dependency graph.
# There must be a class that has a __setup__() method
# but does not call super().__setup__()

# This seems like an extrmely hacky solution,
# but it works for the time being

class CloseInheritance():
    def __setup__(self):
        logging.debug("CloseInheritance reached")
