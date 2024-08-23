text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
  #key_index = 0
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  count = len(alphabet)
  encrypted_text = ''

  for char in message.lower():
      # append space to the message
      if char == ' ':
        encrypted_text += char
      else:
        index = alphabet.find(char)
        new_index = (index + key) % count
        encrypted_text += alphabet[new_index]

  print('plain text:', message)

  print('encrypted_text:', encrypted_text)

