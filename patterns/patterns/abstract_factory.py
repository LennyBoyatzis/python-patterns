import random
import inspect
from abc import ABC, abstractmethod

# https://www.giacomodebidda.com/factory-method-and-abstract-factory-in-python/


class PolygonFactory(ABC):
    """Basic Abstract Factory class for making polygons (products).
    This class has to be subclassed by a factory class that MUST implement
    and override the products method.

    A factory class can create many different polygon objects (products)
    without exposing the instantiation logic to the client. Infact, since all
    methods of this class are abstract, this class can't be instantiated at
    all. Also, each subclass of PolygonFactory should implement the "products"
    method and keep it abstract so even the subclass can't be instantiated
    """
    @classmethod
    @abstractmethod
    def products(cls):
        """Products that the factory can manufacture. Implement in subclass."""
        pass

    @classmethod
    @abstractmethod
    def make_polygon(cls, colour=None):
        """Instantiate a random polygon from all the ones that are available.
        This method creates an instances of a product randomly chosen from all
        products that the factory class can manufacture. The 'colour' property
        of the manufactured object is reassigned here. Then the object is
        returned.
        Parameters
        ----------
        colour: str
            colour to assign to the manufactured object. It replaces the colour
            assigned by the factory class.
        Returns
        -------
        polygon: an instance of a class in cls.products()
            polygon is the product manufactured by the factory class. It's one
            of the products that the factory class can make.
        """
        product_name = random.choice(cls.products())
        this_module = __import__(__name__)
        polygon_class = getattr(this_module, product_name)
        polygon = polygon_class(factory_name=cls.__name__)
        if colour is not None:
            polygon.colour = colour
        return polygon

    @classmethod
    @abstractmethod
    def color(cls):
        return 'black'


class TriangleFactory(PolygonFactory):
    """Abstract Factory class for making triangles."""
    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(
            ['_TriangleEquilateral', '_TriangleIsosceles', '_TriangleScalene'])


class QuadrilateralFactory(PolygonFactory):
    """Abstract Factory class for making quadrilaterals."""
    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(['_Square', '_Rectangle', '_ConvexQuadrilateral'])


def give_me_some_polygons(factories, colour=None):
    """Interface between the client and a Factory class.
    Parameters
    ----------
    factories: list, or abc.ABCMeta
        list of factory classes, or a factory class
    colour: str
        colour to pass to the manufacturing method of the factory class.
    Returns
    -------
    products: list
        a list of objects manufactured by the Factory classes specified
    """
    if not hasattr(factories, '__len__'):
        factories = [factories]

    products = list()
    for factory in factories:
        num = random.randint(5, 10)
        for i in range(num):
            product = factory.make_polygon(colour)
            products.append(product)
    return products


def print_polygon(polygon, show_repr=False, show_hierarchy=False):
    print(str(polygon))
    if show_repr:
        print(repr(polygon))
    if show_hierarchy:
        print(inspect.getmro(polygon.__class__))
        print('\n')


class _Polygon(ABC):
    """Basic abstract class for polygons.

    This class is private because the client should not try to instantiate it.
    The instantiation process should be carried out by a Factory class.
    A _Polygon subclass MUST override ALL _Polygon's abstract methods, otherwise
    a TypeError will be raised as soon as we try to instantiate that subclass.
    """
    def __init__(self, factory_name=None):
        self._color = 'black'
        self._manufactured = factory_name

    def __str__(self):
        return '{} {} manufactured by {} (perimeter: {}; area: {})'\
            .format(self.color, self.__class__.__name__, self.manufactured,
                    self.perimeter, self.area)

    @property
    @abstractmethod
    def family(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def manufactured(self):
        return self._manufactured

    @manufactured.setter
    def manufactured(self, factory_name):
        self._manufactured = factory_name


class _Triangle(_Polygon):
    """Basic concrete class for triangles."""

    @property
    def family(self):
        return 'Triangles'

    @property
    def perimeter(self):
        return 'a+b+c'

    @property
    def area(self):
        return 'base*height/2'


class _TriangleEquilateral(_Triangle):

    @property
    def perimeter(self):
        return '3a'


class _TriangleIsosceles(_Triangle):

    @property
    def perimeter(self):
        return '2a+b'


class _TriangleScalene(_Triangle):
    pass


class _Quadrilateral(_Polygon):
    """Basic concrete class for quadrilaterals."""

    @property
    def family(self):
        return 'Quadrilaterals'

    @property
    def perimeter(self):
        return 'a+b+c+d'

    @property
    def area(self):
        return 'Bretschneider\'s formula'


class _Square(_Quadrilateral):

    @property
    def perimeter(self):
        return '4a'

    @property
    def area(self):
        return 'a*a'


class _Rectangle(_Quadrilateral):

    @property
    def perimeter(self):
        return '2a+2b'

    @property
    def area(self):
        return 'base*height'


class _ConvexQuadrilateral(_Quadrilateral):
    pass


def main():
    # Client is loosely coupled with the products (can easily swap out product
    # families)
    triangles = give_me_some_polygons(TriangleFactory)
    for triangle in triangles:
        print_polygon(triangle)


if __name__ == '__main__':
    main()
