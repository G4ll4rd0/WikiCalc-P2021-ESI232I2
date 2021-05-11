string = r"\frac {((-1)*('b) \pm \sqrt({('b)^2 - 4*('a)*('c)}))}{2*('a)}"

print(string.find(r"\pm"))
print(string.replace(r"\pm", "+"))