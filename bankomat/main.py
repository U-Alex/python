if __name__ == '__main__':
    from view import View
    from sys import argv

    debug = None
    if len(argv) > 1 and argv[1] == 'debug':
        debug = True
    v = View(debug)
    v.auth()
