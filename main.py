import PySimpleGUI as gui

def CountLetters(text):
  return len(text)

def CountWords(text):
  arr=text.split()
  arr=list(filter(None,arr))
  return len(arr)

def CountVowels(text):
  counter=0
  vowels=["a", "ą", "e", "ę", "i", "o", "u", "ó", "y"]
  for letter in text:
    if letter in vowels:
      counter+=1
  return counter

gui.theme("Dark")

layout = [
  [
    gui.Text("Characters: "), gui.Text("0",key="letters"),
    gui.Text("Words: "), gui.Text("0",key="words"),
    gui.Text("Vowels: "), gui.Text("0",key="vowels")
  ],
  [gui.Multiline(size=(50,20),enable_events=True, key="input")]
]

okno = gui.Window("  WordCounter",layout, size=(600,400), element_justification="center", font="Helvetica 14")

while True:
  event, values = okno.read()
  text = values["input"]
  if event == "input":
    #gui.popup("Working")
    okno["letters"].update(CountLetters(text))
    okno["words"].update(CountWords(text))
    okno["vowels"].update(CountVowels(text))