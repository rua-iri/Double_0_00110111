

XML_START = "".join(format(ord(c), "08b") for c in "<msg>")

XML_END = "".join(format(ord(c), "08b") for c in "</msg>")

LOREM_MESSAGE = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Aliquam sapien est, vulputate at pulvinar non, accumsan id sem.
Nunc vel rutrum sapien.
Suspendisse potenti.
Sed ac eros sit amet nisl imperdiet semper quis a tellus.
In non scelerisque lacus.
In vel pulvinar metus.
Vivamus ultricies nibh eu aliquet imperdiet.
Cras a tempus nunc.
Nullam et orci lectus.
Vestibulum rhoncus dui ut felis laoreet ultrices et a enim.
Sed quis urna sit amet metus volutpat sodales sit amet quis risus.
Vivamus vehicula tempus mauris, a mollis arcu tincidunt nec.
In vehicula massa feugiat arcu commodo ornare in quis nisi.
Phasellus at purus vitae tellus pharetra cursus.
Mauris sed erat felis.
Vestibulum maximus venenatis nunc.
Etiam efficitur interdum augue.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac
turpis egestas.
Donec suscipit non nisl id dapibus.
Proin feugiat at felis id faucibus.
Curabitur dictum urna vitae rhoncus pretium.
Praesent egestas turpis in libero egestas, et porta quam finibus.
Sed ante nisi, semper ornare ullamcorper quis, facilisis in lectus.
Aliquam ultrices imperdiet ipsum vel finibus."""

TEN_MB = 10000000
