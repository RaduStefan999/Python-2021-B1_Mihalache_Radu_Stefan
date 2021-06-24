def build_xml_element (node_name, node_content, href, _class, id) :
    
    return '<' + node_name + ' href = "' + href + '"' + ' _class = "' + _class + '"' + ' id = "' + id + '">' + node_content + '<' + node_name + '/>'


print ( build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") )