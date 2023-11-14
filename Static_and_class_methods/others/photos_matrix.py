
line = '-----------'
photos = int(input('Photos: '))
ph_per_page = 4
label = '[]'
page_counter = 0
counter = 0  # photos end
n = [[] for t in range(1)]
while True:
    n[page_counter].append(label)
    counter += 1
    if counter == photos or photos <= 0:
        break

    if len(n[page_counter]) == ph_per_page:
        page_counter += 1
        n.append([])

if photos <= 0:
    print("You need at least 1 picture to create an album")
else:
    for j in n:
        print(f'{line}\n{' '.join(map(str, j))}')
    print(line)
