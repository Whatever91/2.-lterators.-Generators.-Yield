class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_len = len(list_of_list)
        self.inner_counter = 0
        self.outer_counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.outer_counter == self.list_len:
            raise StopIteration
        if self.inner_counter < len(self.list_of_list[self.outer_counter]) - 1:
            item = self.list_of_list[self.outer_counter][self.inner_counter]
            self.inner_counter += 1
            return item
        elif self.inner_counter == len(self.list_of_list[self.outer_counter]) - 1:
            item = self.list_of_list[self.outer_counter][self.inner_counter]
            self.inner_counter = 0
            self.outer_counter += 1
            return item


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