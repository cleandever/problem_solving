"""
https://programmers.co.kr/learn/courses/30/lessons/17686
"""
def solution(files):
    split_files = []
    for i, filename in enumerate(files):
        head, number, tail = get_head_num_tail(filename)
        split_files.append([head.lower(), number.zfill(5), tail, i, filename])

    return [file[4] for file in sorted(split_files, key=lambda x: (x[0], x[1], x[3], x[2]))]


def get_head_num_tail(filename):
    first_num_idx = -1
    for i, c in enumerate(filename):
        if c.isdigit():
            first_num_idx = i
            break

    head = filename[:first_num_idx]
    number_and_tail = filename[first_num_idx:]

    # tail에 영문자가 없는 경우
    # tail에 영문자가 있는 경우
    # tail이 아무것도 없는 경우
    last_num_idx = -1
    for i, c in enumerate(number_and_tail):
        if not c.isdigit():
            last_num_idx = i
            break

    if last_num_idx == -1:
        number = number_and_tail
        tail = ''
    else:
        number = number_and_tail[:last_num_idx]
        tail = number_and_tail[last_num_idx:]

    return [head, number, tail]


assert get_head_num_tail('foo9.txt') == ['foo', '9', '.txt']
assert get_head_num_tail('foo010bar020.zip') == ['foo', '010', 'bar020.zip']
assert get_head_num_tail('F-15') == ['F-', '15', '']

assert solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
assert solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
assert solution(['img1.png']) == ['img1.png']
assert solution(['img1.png', 'IMG1.png']) == ['img1.png', 'IMG1.png']
assert solution(['aMG1.png', 'img1.png', 'IMG1.png']) == ['aMG1.png', 'img1.png', 'IMG1.png']