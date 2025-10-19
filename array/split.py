#
# Metodos imporantes
# Metodo SPLIT() sirve para convertir string en un arreglo
# Si no  especifica ningun parametro utiliza el espacio como referencia
stringToArray = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lectus orci, porta sed interdum at, ornare nec lectus. Donec non ex id neque pellentesque elementum. Ut euismod egestas risus, in venenatis leo condimentum dictum. Maecenas eget scelerisque sem. Quisque rhoncus dolor a elit sollicitudin eleifend eu id tellus. Mauris a semper mauris, sit amet sollicitudin est. Quisque erat arcu, commodo a neque sit amet, ultricies scelerisque neque. Duis ex augue, ultricies a euismod nec, semper sed est. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean diam nisl, malesuada nec pellentesque nec, consectetur eget nisl. Donec pretium nisi arcu, ac malesuada augue pretium ac. Quisque est dui, imperdiet quis est eu, convallis dapibus elit. Fusce placerat, tortor dignissim sagittis rutrum, urna felis luctus diam, vitae pulvinar magna erat a tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. "
ArrayFromString = stringToArray.split()

print(ArrayFromString)

# Metodo join()
ResultadoMetodoJoin = "WEQ321/=-MER2#@".join(ArrayFromString)
ResultadoDeSplitPorPatron = ResultadoMetodoJoin.split("WEQ321/=-MER2#@")

print(ResultadoDeSplitPorPatron)
