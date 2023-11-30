"""A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over."""

s = int(input('Total amount of sweets: '))
p = int(input('Total number of pupils: '))

total_sweets_distributed = s // p
extra_sweets = s % p

print(f'Each student will receive {total_sweets_distributed} sweets, with {extra_sweets} as extras ')
