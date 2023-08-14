"""
pyttsx3 is a text-to-speech conversion library in Python. 
Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
"""
import PyPDF2
import pyttsx3

# abrir el archivo pdf en la ruta especifica
archivo_pdf = PyPDF2.PdfFileReader(open('C:/Users/Luis/Desktop/Pyton/Python_Coding/doc.pdf', 'rb'))

voz = pyttsx3.init()

# Velocidad del audio 
rate = voz.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
voz.setProperty('rate', 200)     # setting up new voice rate

for num_pag in range(archivo_pdf.numPages):
    texto = archivo_pdf.getPage(num_pag).extract_text()
    voz.say(texto)
    voz.runAndWait()

voz.stop()

voz.save_to_file(texto, 'audio.mp3')
voz.runAndWait() # para guardar el archivo 