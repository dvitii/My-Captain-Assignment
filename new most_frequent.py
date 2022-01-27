def most_frequent(st1):
    # declare variables
    st1 = st1.lower()
    nl = []
    # n2 = []
    cnt = []
    tup1 = ()
    max = 0
    j = 0
    idx = 0

    srt_lst = []
    # tmp_lst = []

    # loop to count occurence of a letter in string
    for i in st1:
        # print(nl,"and cnt is", cnt)
        if i not in nl:
            x = st1.count(i)
            nl.append(i)
            # n2.append(x)
            tup1 = (i, x)
            cnt.append(tup1)

    cnt_cp = cnt.copy()  # duplicate copy
    idx = 0
    cnt_idx = 0
    #print('list after 1st loop', cnt)

    # loop for sorting in decreasing order
    for i in cnt_cp:
        # print('in sec loop')

        max = 0
        j = 0
        idx = 0

        if len(cnt) > 1:
            for i in cnt:
                # print(i,max)
                if j == 0:
                    max = i[1]
                    cnt_idx = idx

                elif max < i[1]:
                    max = i[1]
                    cnt_idx = idx

                else:
                    if max > i[1]:
                        pass
                j += 1
                idx += 1

            # print(cnt_idx)
            srt_lst.append(cnt[cnt_idx])
            # print('sorted list',srt_lst)

            cnt.pop(cnt_idx)
            # print('popped list',cnt)
    srt_lst.append(cnt[0])  # append the last element
    #print('final sorted list', srt_lst)

    # loop for Printing

    for i in srt_lst:
        print(i[0], " = ", i[1])


statement = str(input("Enter a string: "))
most_frequent(statement)