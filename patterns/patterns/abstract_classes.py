from abc import abstractmethod, ABC

"""
Python doesn't provide abstract classes. It only comes
with a module which provides the infrastructure for defining
Abstract Base Classes (ABCs)
"""


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        # Invoke the abstract base class
        super().__init__()

    # An abstract method can have an implementation in
    # the base class i.e. (1 + 2). This makes ABC's different
    # from interfaces
    @abstractmethod
    def do_something(self):
        return 1 + 2


# Example which incorrectly implements the ABC
class BrokenABC(AbstractClassExample):
    pass


# Example which correctly implements the ABC
class CorrectABC(AbstractClassExample):
    def do_something(self):
        return self.value + 42


"""
A class that is drived from an abstract class CANNOT be
instantiated unless all of its abstract methods are overridden
"""

correct = CorrectABC(10).do_something()
print(f"Correct answer: {correct}")
