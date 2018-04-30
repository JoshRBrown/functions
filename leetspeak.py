text = "hello world"
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [ 4,   3,   6,   1,   0,   5,   7]


def leet(text):
  translation = ""
  uppercased_text = text.upper()
  for letter in uppercased_text:
    counter = 0
    letter_to_add_to_translation = ""
    for letter_to_convert in letters_to_convert:
      if letter == letter_to_convert:
        letter_to_add_to_translation = str(numbers[counter])
        break
      else:
        letter_to_add_to_translation = letter
  
      counter = counter + 1
    translation = translation + letter_to_add_to_translation
  return translation
