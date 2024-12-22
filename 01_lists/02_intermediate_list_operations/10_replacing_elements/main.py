text = "hello world"
replaced_text = ''.join(['*' if char in 'aeiouAEIOU' else char for char in text])

print(replaced_text)  #output: h*ll* w*rld