def tallest_people(**people):
    output = {'nobody': 0}
    for name, height in people.items():
        if height > output.values()