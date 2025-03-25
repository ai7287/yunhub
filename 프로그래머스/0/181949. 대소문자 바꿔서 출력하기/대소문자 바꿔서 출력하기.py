def convert_case(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

input_text = input()
print(convert_case(input_text))
