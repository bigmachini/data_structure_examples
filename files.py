f = open('wastland.txt', mode='wt', encoding='utf=8')

f.write('What are the roos that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stong rubbish? ')
f.close()


f = open('wastland.txt', mode='rt', encoding='utf-8')


import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])