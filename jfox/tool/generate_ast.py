#!/usr/local/bin/python3

import sys

expression_types = {
  "Binary": "Expr left, Token operator, Expr right",
  "Grouping": "Expr expression",
  "Literal": "Object value",
  "Unary": "Token operator, Expr right"
}

def define_ast(output_dir, basename, types):
  filepath = output_dir + "/" + basename + ".java"
  file = open(filepath, 'w')

  s = """package pizza.rotten.jfox;
  
import java.util.List;

abstract class """+basename+""" {\n"""
  
  for class_name, class_fields in types.items():
    fields = class_fields.split(", ")

    s += "    static class " + class_name + " extends " + basename + " {\n"
    
    # fields
    for field in fields:
      s += "        final " + field + ";\n"   
    s += "\n"

    # constructor
    s += "        " + class_name + "(" + class_fields + ") {\n" 
    for field in fields:
      name = field.split(" ")[1]
      s += "            this." + name + " = " + name + ";\n"
    s += "        }\n"
    s += "    }\n"
    s += "\n"
  
  s += "}"

  file.write(s)
  file.close()

def main():
  if (len(sys.argv) != 2):
    print("Usage: generate_ast <output_directory>")
    sys.exit()

  define_ast(sys.argv[1], "Expr", expression_types)

if __name__=="__main__":
    main()