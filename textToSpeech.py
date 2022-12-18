from gtts import gTTS

def textToSpeech(textFile):
  try:
    text= ''
    with open(textFile) as f:
      lines = f.readlines()
      for x in lines:
        text += ' ' + x.strip()
    language = 'en'
    converter = gTTS(text=text, lang=language, slow=False)
    converter.save(textFile.rsplit('.',1)[0] + ".mp3")

  except Exception as err:
    print(err)
    print("Error encountered during conversion.")
  else:
    print("Successfully converted " + textFile)

if __name__ == '__main__':
  textFile = input("Enter text file to convert: ")
  textToSpeech(textFile)