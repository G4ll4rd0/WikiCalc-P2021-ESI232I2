from pylatexenc.latex2text import LatexNodes2Text
latex = r"x = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a}"
text = LatexNodes2Text().latex_to_text(latex)

print(text)