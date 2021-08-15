from re import sub
from re import compile as re_compile


def string_to_float(value: str) -> str:
    pattern = re_compile(
        "([0-9]{1,4})([,.])?([0-9]{1,2})?(.*)"
    )
    no_alpha_with_just_dot = sub(
        "^([^0-9]*)|([^0-9,.]*)|([^0-9,.]*)$", "", value
    )
    just_one_dot = sub("[,.]{2,}", ".", no_alpha_with_just_dot)
    match = pattern.match(just_one_dot)
    result = ""
    if match:
        before_dot = match.groups()[0] or ""
        after_dot = match.groups()[2] or ""
        len_ = len(before_dot+after_dot)
        dot = "." if len_ > 4 else (match.groups()[1] or "")
        result = f"{before_dot}{dot}{after_dot}"

    return result
