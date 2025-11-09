def reverse_strings(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse_strings(s[1:]) + s[0]

test_string = "python"
print("Реверс строки:", reverse_strings(test_string))

