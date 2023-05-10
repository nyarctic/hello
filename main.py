import sys

def print_hello(n):
    for i in range(n):
        print(f'hello: {i}')

if __name__ == "__main__":
    print_hello(sys.argv[1])
