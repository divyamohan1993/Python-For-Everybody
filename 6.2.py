# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# DO NOT COPY THE SOLUTION. ACTIONS MIGHT BE TAKEN ON YOUR ACCOUNT.

text = "X-DSPAM-Confidence:    0.8475"
x = text.find('    ')
print(float(text[x:]))