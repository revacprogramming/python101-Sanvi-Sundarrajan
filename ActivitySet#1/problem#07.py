# Strings
def myinput():
    text = "X-DSPAM-Confidence:    0.8475"
    return text


def convert(text):
    Pos = text.find(':')
    last = text[Pos+1:]
    end = float(last)
	return end


def output(end):	
    print(end)


def main():
    text=myinput()
    end=convert(text)
		output(end)


main()