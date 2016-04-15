import class_test

class Example():

    def run(self):
        print "Hello, world!"
        t = class_test.Employee("Bob B", 23000)
        print t.test_func()

if __name__ == '__main__':
    Example().run()