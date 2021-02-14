from gendiff.cli import run
from gendiff import generate_diff

def main():
    args = run()
    generate_diff.output(args)

if __name__ == '__main__':
    main()
