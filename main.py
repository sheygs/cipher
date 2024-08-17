text = 'Hello Zaira'
shift = 3

def caesar():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  count = len(alphabet)
  encrypted_text = ''

  for char in text.lower():
      if char == ' ':
        encrypted_text += char
      else:
        index = alphabet.find(char)
        new_index = (index + shift) % count
        encrypted_text += alphabet[new_index]

  print('plain text:', text)

  print('encrypted_text:', encrypted_text)

caesar()