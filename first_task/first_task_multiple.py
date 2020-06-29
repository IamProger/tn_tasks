"""This variant is suitable in case of multiple input"""

RESULT = {'a': 0, 'b': 0, 'c': 0}
COUNTER = 0

while True:
    try:
        for character in input():
            COUNTER += 1
            if character in RESULT:
                RESULT[character] += 1
            if not COUNTER % 1000:
                print('a: {}, b: {}, c: {}'.format(*RESULT.values()))
    except (KeyboardInterrupt, EOFError):
        print('a: {}, b: {}, c: {}'.format(*RESULT.values()))
        break
