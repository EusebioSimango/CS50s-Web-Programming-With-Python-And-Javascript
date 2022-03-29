from time import pthread_getcpuclockid


def announce(f):
    def wraper():
        print("About to run funcion...")
        f()
        print("Done with the function.")
    return wraper

@announce
def hello():
    print("Hello, World!")

hello()