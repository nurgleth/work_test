# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если пароль содержить только цифры, столько строчные, только заглавные то вернуть Weak
# - если пароль содержить любых 3 наборов вернуть Good
# - если пароль содержить симолы любых 3 наборов, вернуть Very Good

def password_stream(value: str) -> str:
    if len(value) < 8:
        return "Too Weak"
    return ""


if __name__ == "__main__":
    assert password_stream("") == "Too Weak"
    assert password_stream("1234567") == "Too Weak"
    assert password_stream("qwert") == "Too Weak"
    assert password_stream("12678t") == "Weak"
    assert password_stream("123qwer1") == "Good"
