import os
import shutil

ITEM_PER_PAGE = 8
PAGE_OFFSET = 1

DATE, MEDIA, URL, TITLE = 0, 1, 2, 3

try:
    shutil.rmtree('press/')
except FileNotFoundError:
    pass

data = []

with open('_data/press.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data.append(line.replace('\n', '').split(',', maxsplit=3))

data.reverse()

number_of_total_pages = len(data) // ITEM_PER_PAGE + PAGE_OFFSET
for i in range(PAGE_OFFSET, number_of_total_pages + PAGE_OFFSET):
    outputs = [
        '---',
        'layout: press',
        'title: 보도자료',
        '---',
        '<ul class="release-list">',
    ]

    for output in data[(i - PAGE_OFFSET) * ITEM_PER_PAGE : i * ITEM_PER_PAGE]:
        outputs.extend([
            '\t<li class="release-item">',
            '\t\t<span class="release-media">%s</span>' % output[MEDIA],
            '\t\t<span class="release-date">%s</span>' % output[DATE],
            '\t\t<a target="_blank" href="%s" class="release-link">%s</a>' % (output[URL], output[TITLE]),
            '\t</li>'
        ])

    outputs.extend([
        '</ul>',
        '<ul class="press__paginator">'
    ])

    if i != PAGE_OFFSET:
        url = '/press/' + str(i - 1)
        url = url if i - 1 != PAGE_OFFSET else '/press'
        outputs.append('\t<li class="press__paginator__previous"><a href="%s"><span aria-hidden="true">&lt;</span> 이전</a></li>' % url)

    if i != number_of_total_pages:
        url = '/press/' + str(i + 1)
        outputs.append('\t<li class="press__paginator__next"><a href="%s">다음 <span aria-hidden="true">&gt;</span></a></li>' % url)

    outputs.extend(['</ul>', ''])

    file_name = 'press/' + str(i) + '/index.html'
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as f:
        f.write('\n'.join(outputs))

    if i == PAGE_OFFSET:
        with open('press/index.html', 'w') as f:
            f.write('\n'.join(outputs))
