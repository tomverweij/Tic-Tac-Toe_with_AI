import operator

# find the shortest book and print its title
print(sorted(books.items(), key=operator.itemgetter(1))[0][0])
# find the longest book and print its title
print(sorted(books.items(), key=operator.itemgetter(1))[-1][0])
