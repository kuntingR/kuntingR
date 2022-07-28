import time


class HelloWorld():
    def __init__(self):
        pass

    def print_hello(self, input_time):
        for t in range(input_time):
            print("the {} time for hello world !".format(t+1))
            time.sleep(1)


hello = HelloWorld()
hello.print_hello(10)
