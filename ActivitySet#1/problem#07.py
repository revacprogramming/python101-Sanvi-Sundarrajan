# Strings

text = "X-DSPAM-Confidence:    0.8475";
Pos = text.find(':')
last = text[Pos+1:]
end = float(last)
print(end)
