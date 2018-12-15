class InvalidTag(Exception):
    """If the tag is not valid"""


class DecoratedFunctionError(Exception):
    """If wrapped function returns anything other than str"""


def tag(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(name, str) or name.isdigit():
                raise InvalidTag('Error: tag does not exist')
            result = func(*args, **kwargs)
            if not isinstance(result, str):
                raise DecoratedFunctionError('Error: Wrapped function should return string value')
            tag_name = name.lower()
            result = rf'<{tag_name}>{result}</{tag_name}>'
            return result
        return wrapper
    return decorator


TEST_CASES = [
        ({'name': 'span'}, 'lorem ipsum', '<span>LOREM IPSUM</span>'),
        ({'name': 'div'}, 'lorem ipsum', '<div>LOREM IPSUM</div>'),
        ({'name': 'STRONG'}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
        ({'name': '123'}, 'lorem ipsum', 'Error: tag does not exist'),
        ]


for case in TEST_CASES:
    @tag(**case[0])
    def foo(text):
        return text.upper()
    print(foo(case[1]))
    assert foo(case[1]) == case[2]