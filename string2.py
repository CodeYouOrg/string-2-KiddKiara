def verbing(s):
    if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    return s

def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    if not_index != -1 and bad_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index + 3:]
    return s

def front_back(a, b):
    def split_half(s):
        mid = (len(s) + 1) // 2
        return s[:mid], s[mid:]

    a_front, a_back = split_half(a)
    b_front, b_back = split_half(b)

    return a_front + b_front + a_back + b_back

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
    
