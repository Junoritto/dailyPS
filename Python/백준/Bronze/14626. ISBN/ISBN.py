isbn = input()
checksum = 0
for i in range(13):
    if isbn[i] != '*':
        if i % 2 == 0:
            checksum += int(isbn[i])
        else:
            checksum += int(isbn[i])*3
    else:
        star_position = i
ans = 10 - (checksum % 10)

if ans != 10:
    if star_position % 2 == 0:
        print(ans)
    else:
        print((ans * 7) % 10)
else:
    print(0)
