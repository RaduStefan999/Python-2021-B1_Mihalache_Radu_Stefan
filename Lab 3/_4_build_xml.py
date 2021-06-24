def build_xml_element (node_name, node_content, **atributes) :
    
    return '<' + node_name + ' href = "' + atributes["href"] + '"' + ' _class = "' + atributes["_class"] + '"' + ' id = "' + atributes["id"] + '">' + node_content + '<' + node_name + '/>'


print ( build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") )