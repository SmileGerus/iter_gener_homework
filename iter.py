class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = 0
        self.lists_in_one = [] 

    def __iter__(self):
        for list in self.list_of_list:
            self.lists_in_one.extend(list)
        self.len_lists = len(self.lists_in_one)
        return self

    def __next__(self):
        if self.count < self.len_lists:
            item = self.lists_in_one[self.count]
            self.count += 1
            return item
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()