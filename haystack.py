import re


def strstr(needle, haystack):
    """Return part of haystack string starting from and including the first occurrence
     of needle to the end of haystack."""

    search_length = len(needle)
    haystack_length = len(haystack)

    # checks if needle is in haystack using regular expressions
    # alternatively, you could just say "if needle in haystack", or "if haystack.find(needle) != -1:"
    if re.search(needle, haystack):
        # if needle is in there, looks at all letter combinations in haystack that are
            # the same length as the needle, until reaching the actual needle
        x = 0
        while x + search_length <= haystack_length:
            # once you find the needle in the haystack, print the needle --
                # along with the rest of the haystack
            if haystack[x: x + search_length] == needle:
                print haystack[x:]
                # by returning here, you exit the function, thus preventing
                    # unnecessary work & output
                return
            x += 1
    else:
        # returns None if the needle isn't present
        return None


def strstr2(needle, haystack):
    # this is the same exact function as above, only without regular expressions.
    # with this function, you don't need a separate check for the presence of a needle,
        # since the while loop both checks for the presence of the needle and handles the print output
    # although if the needle isn't present in the first place then it is a lot of extra work

    search_length = len(needle)
    haystack_length = len(haystack)

    x = 0
    while x + search_length <= haystack_length:
        if haystack[x: x + search_length] == needle:
            print haystack[x:]
            return
        x += 1

    return None


def strstr3(needle, haystack):
    # nearly the same as above, except uses a for loop instead of a while loop

    search_length = len(needle)
    haystack_length = len(haystack)

    for i in range(haystack_length):
        search_end = i + search_length

        # if python gets too far along in the haystack so that the number of
            # chars left is less than the length of the needle, then you know
            # the needle doesn't exist in the haystack
        if search_end > haystack_length:
            return None

        if haystack[i: search_end] == needle:
            print haystack[i:]
            return


def strstr4(needle, haystack):

    search_length = len(needle)

    # this function is similar to the others, but first compares each char of the haystack
        # to the first char of the needle
    # if the two chars match, then compare the entire needle with a group of chars in the haystack
    # this prevents comparing entire groups of chars unless there is a better chance of a match
    # enumerate is a built in python function that takes a list or str and returns each char and its index

    for i, c in enumerate(haystack):
        if c == needle[0]:
            if haystack[i: i + search_length] == needle:
                print haystack[i:]
                return
    return None
