import xml.etree.ElementTree as ET

def archivoXML():
    #Aqui creamos el root Students
    p = ET.Element('Students')
    #Aqui los childs del Students
    a = ET.SubElement(p, 'student')
    #Modificamos y ponemos un atributo y un valor
    a.set('Frutas', 'Fresa')
    g = ET.SubElement(a, 'name')
    h = ET.SubElement(a, 'surname')
    i = ET.SubElement(a, 'email')
    j = ET.SubElement(a, 'dni')
    b = ET.SubElement(p, 'student')
    b.set('Frutas', 'Manzana')
    g1 = ET.SubElement(b, 'name')
    h1 = ET.SubElement(b, 'surname')
    i1 = ET.SubElement(b, 'email')
    j1 = ET.SubElement(b, 'dni')
    c = ET.SubElement(p, 'student')
    c.set('Frutas', 'Mango')
    g2 = ET.SubElement(c, 'name')
    h2 = ET.SubElement(c, 'surname')
    i2 = ET.SubElement(c, 'email')
    j2 = ET.SubElement(c, 'dni')
    d = ET.SubElement(p, 'student')
    d.set('Verduras', 'Remolacha')
    g3 = ET.SubElement(d, 'name')
    h3 = ET.SubElement(d, 'surname')
    i3 = ET.SubElement(d, 'email')
    j3 = ET.SubElement(d, 'dni')
    f = ET.SubElement(p, 'student')
    f.set('Verduras', 'Lechuga')
    g4 = ET.SubElement(f, 'name')
    h4 = ET.SubElement(f, 'surname')
    i4 = ET.SubElement(f, 'email')
    j4 = ET.SubElement(f, 'dni')

    #Creamos un archivo XML del codigo creado
    tree = ET.ElementTree(p)
    tree.write("ArchivoXML.xml")
    #Lo printamos por consola
    ET.dump(p)








