class _Car():
    pass


class _Bike():
    pass


def factory_method(product_type):
    if product_type == 'car':
        return _Car()
    elif product_type == 'bike':
        return _Bike()
    else:
        raise ValueError(f'Cannot make: {product_type}')


for product_type in ('car', 'bike'):
    product = factory_method(product_type)
    print(str(product))
