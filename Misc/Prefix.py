prefixDict = {
    "P": 1e15,
    "T": 1e12,
    "G": 1e9,
    "M": 1e6,
    "k": 1e3,
    "":  1,
    "m": 1e-3,
    "u": 1e-6,
    "n": 1e-9,
    "p": 1e-12,
    "f": 1e-15
}

def formatPrefix(n, unit, precision = -1):
    for prefix in prefixDict:
        if n >= prefixDict[prefix]:
            prefixStr = prefix
            n /= prefixDict[prefix]
            break

    if precision == -1:
        rounded = round(n)
    else:
        rounded = round(n, ndigits = precision)

    return f"{rounded} {prefixStr}{unit}"

def formatTime(seconds):
    hours = seconds // 3600
    h = '' if hours == 0 else f'{round(hours)}h '
    seconds %= 3600

    minutes = seconds // 60
    m = '' if minutes == 0 else f'{round(minutes)}m '
    seconds %= 60

    s = '' if seconds == 0 else f'{round(seconds)}s'

    time = h + m + s

    if time == '':
        return '0s'
    else:
        return time
