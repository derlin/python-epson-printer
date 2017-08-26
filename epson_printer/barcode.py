import re

# Indicates UPC-A barcode when used with Printer::barcode
BARCODE_UPCA = 0
# Indicates UPC-E barcode when used with Printer::barcode
BARCODE_UPCE = 1
# Indicates JAN13 barcode when used with Printer::barcode
BARCODE_JAN13 = 2
# Indicates JAN8 barcode when used with Printer::barcode
BARCODE_JAN8 = 3
# Indicates CODE39 barcode when used with Printer::barcode
BARCODE_CODE39 = 4
# Indicates ITF barcode when used with Printer::barcode
BARCODE_ITF = 5
# Indicates CODABAR barcode when used with Printer::barcode
BARCODE_CODABAR = 6
# Indicates CODE93 barcode when used with Printer::barcode
BARCODE_CODE93 = 7
# Indicates CODE128 barcode when used with Printer::barcode
BARCODE_CODE128 = 8


def validate_barcode(barcode, type):
    if type == BARCODE_UPCA:
        return __validate(barcode, [(11, 12)], "^[0-9]{11,12}$")
    if type == BARCODE_UPCE:
        return __validate(barcode, [(6, 8), (11, 12)], "^([0-9]{6,8}|[0-9]{11,12})$")
    if type == BARCODE_JAN13:
        return __validate(barcode, [(12, 13)], "^[0-9]{12,13}$")
    if type == BARCODE_JAN8:
        return __validate(barcode, [(7, 8)], "^[0-9]{7,8}$")
    if type == BARCODE_CODE39:
        return __validate(barcode, [(1, 255)], "^([0-9A-Z \$\%\+\-\.\/]+|\*[0-9A-Z \$\%\+\-\.\/]+\*)$")
    if type == BARCODE_ITF:
        return __validate(barcode, [(2, 255)], "^([0-9]{2})+$")
    if type == BARCODE_CODABAR:
        return __validate(barcode, [(1, 255)], "^[A-Da-d][0-9\$\+\-\.\/\:]+[A-Da-d]$")
    if type == BARCODE_CODE93:
        return __validate(barcode, [(1, 255)], "^[\\x00-\\x7F]+$")
    if type == BARCODE_CODE128:
        return __validate(barcode, [(1, 255)], "^\{[A-C][\\x00-\\x7F]+$")


def __validate(barcode, acceptable_lengths, regex):
    return any([t[0] <= len(barcode) <= t[1] for t in acceptable_lengths]) and re.match(regex, barcode)


    # =============================
