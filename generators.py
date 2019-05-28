def gen123():
    yield 1
    yield 2
    yield 3


def take(count, iterable):
    """Take itmes from the fron of an iterable

    Args:
        count: The maximum number of items to retrieve
        iterable: The source series

    Yeilds:
        At most 'count' items from 'iterable
    """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """Return unique items by elimination duplicates.

    Args:
        iterable: The source series

    Yeilds:
        unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ == "__main__":
    # run_take()
    #run_distinct()
    run_pipeline()
