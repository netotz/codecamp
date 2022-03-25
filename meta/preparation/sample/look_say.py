'''
https://www.facebook.com/careers/life/sample_interview_questions
'''


def print_sequence(first: str, n: int) -> None:
    if first == '' or n <= 0:
        return

    print(first)
    digits = list(first)

    # O(n)
    for _ in range(n - 1):
        current = str(digits[0])
        count = 1

        next_seq = []
        # O(d)
        for j in range(1, len(digits)):
            if current == digits[j]:
                count += 1
                continue
            
            next_seq.append(str(count))
            next_seq.append(current)

            current = digits[j]
            count = 1
        
        if current != '':
            next_seq.append(str(count))
            next_seq.append(current)

        digits = next_seq
        # O(d)
        print(''.join(digits))
