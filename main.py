def main():
    r = open(u'data/out.txt', 'w')
    l = open(u'data/inp.txt', 'r').read().lower().split()

    new_l = []

    for i in range(len(l)):
        if l[i][0] == 'а' and l[i][-1] == 'я':
            new_l.append(l[i])

    r.write(','.join(map(str, new_l)))
if __name__ == '__main__':
    main()