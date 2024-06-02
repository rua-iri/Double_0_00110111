

XML_START = "".join(format(ord(c), "08b") for c in "<msg>")

XML_END = "".join(format(ord(c), "08b") for c in "</msg>")