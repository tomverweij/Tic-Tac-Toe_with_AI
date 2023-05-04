iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {'species': species,
                  'petal_length': petal_length,
                  'petal_width': petal_width,
                  **kwargs}

# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')

# print(iris)