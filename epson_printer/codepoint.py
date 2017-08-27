class CodePoint:
    def __init__(self, codepage, encoding):
        self.codepage = codepage
        self.encoding = encoding

    def encode(self, utfString):
        return utfString.decode("utf-8").encode(self.encoding)


CODEPOINT_USA_EU = CodePoint(codepage=0, encoding="cp437")
CODEPOINT_MULTILINGUAL = CodePoint(codepage=2, encoding="cp850")
CODEPOINT_PORTUGAL = CodePoint(codepage=3, encoding="cp860")
CODEPOINT_CANAFRENCH = CodePoint(codepage=4, encoding="cp863")
CODEPOINT_NORDIC = CodePoint(codepage=4, encoding="cp865")
CODEPOINT_EURO = CodePoint(codepage=19, encoding="cp858")
