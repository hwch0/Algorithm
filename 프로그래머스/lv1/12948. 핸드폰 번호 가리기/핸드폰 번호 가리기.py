def solution(phone_number):
    string = list(phone_number)

    string = ['*' for i in string[:len(string)-4]]+string[-4:]
    answer = ''.join(string)
    return answer