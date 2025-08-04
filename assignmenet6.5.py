text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(':')
number_str = text[colon_pos+1:].strip()
print(number_str)