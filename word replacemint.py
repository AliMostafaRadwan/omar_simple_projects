def word_repalce():
    str = "Hello <<UserName>>, How are you?"
    word_to_replace = input("Enter the word to replace: ")
    word_repalcement = input("Enter the word to replace with: ")  
    print(str.replace(word_to_replace, word_repalcement))

word_repalce()
