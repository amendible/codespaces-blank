
class f:
    def read(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:  # iterar linea linea (eficiente)
                print(línea.strip())
    
    def write(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Encabezado\n")
            f.write.lines(["linea 1\n", "linea 2\n", "linea 3\n", "linea 4\n"])

f = f()
f.read("notes.txt")
f.write("notes.txt")