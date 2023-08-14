import pyshorteners

original_url = input("Ingresa la url: ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(original_url)

print ("La url acortada es: " + short_url)

# guardar archivo 
f = open ("url.txt", "w")
f.write(short_url)
f.close