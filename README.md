## Clashgap

![AppVeyor tests](https://img.shields.io/appveyor/tests/NioGreek/Clashgap)
![PyPI - Downloads](https://img.shields.io/pypi/dm/clashgap)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ad33454aad9d4847ba0a8d1ca3ae2500)](https://app.codacy.com/gh/NioGreek/Clashgap?utm_source=github.com&utm_medium=referral&utm_content=NioGreek/Clashgap&utm_campaign=Badge_Grade_Settings)

A per-charecter diff/compression algorithm implementation in python

### How it works
In case if you have two strings:
> "This is a sentence..." and "This is a word..."

you could "clash" both of them together and find their gap, to get an array loking something like:
> \["This is a", \["sentence", "word"\], "..."\]

As you can the clashgap algorithm looks for collisions in the two strings to find the gap

The clashgaped string maybe used for compression or as the diff of the input strings

