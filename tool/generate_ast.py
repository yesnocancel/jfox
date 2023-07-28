#!/usr/local/bin/python3

import sys

EXPRESSION_BASENAME = "Expr"
STATEMENT_BASENAME = "Stmt"

EXPRESSION_TYPES = {
  "Binary": "Expr left, Token operator, Expr right",
  "Grouping": "Expr expression",
  "Literal": "Object value",
  "Unary": "Token operator, Expr right"
}

STATEMENT_TYPES = {
  "Expression": "Expr expression",
  "Print": "Expr expression"
}

def write_visitor_interface(basename: str, expression_types: dict) -> str:
  s = "    interface Visitor<R> {\n"
  for class_name, class_fields in expression_types.items():
    s+= "        R visit"+class_name+basename+"("+class_name+" "+class_name.lower()+");\n"
  s+= "    }\n"
  s+= "\n"
  return s

def define_ast(basename: str, expression_types: dict) -> str:
  s = "package pizza.rotten.jfox;\n"
  s+= "\n"
  s+= "abstract class "+basename+" {\n"
  s+= "\n"
  s+= "    abstract <R> R accept(Visitor<R> visitor);\n"
  s+= "\n"

  s+= write_visitor_interface(basename, expression_types)

  for class_name, class_fields in expression_types.items():
    fields = class_fields.split(", ")
    s+= "    static class " + class_name + " extends " + basename + " {\n"
    
    # fields
    for field in fields:
      s+= "        final " + field + ";\n"   
    s+= "\n"

    # constructor
    s+= "        " + class_name + "(" + class_fields + ") {\n" 
    for field in fields:
      name = field.split(" ")[1]
      s+= "            this." + name + " = " + name + ";\n"
    s+= "        }\n"

    # visitor pattern
    s+= "        @Override\n"
    s+= "        <R> R accept(Visitor<R> visitor) {\n"
    s+= "            return visitor.visit"+class_name+basename+"(this);\n"
    s+= "        };\n"

    s+= "    }\n"
    s+= "\n"  

  s+= "}"

  return s

def write_file(basename: str, output_dir: str, content: str):
  filepath = output_dir + "/" + basename + ".java"
  file = open(filepath, 'w')
  file.write(content)
  file.close()
  
def main():
  if (len(sys.argv) != 2):
    print("Usage: generate_ast <output_directory>")
    sys.exit()

  file_content = define_ast(EXPRESSION_BASENAME, EXPRESSION_TYPES)
  write_file(EXPRESSION_BASENAME, sys.argv[1], file_content)

  file_content = define_ast(STATEMENT_BASENAME, STATEMENT_TYPES)
  write_file(STATEMENT_BASENAME, sys.argv[1], file_content)

if __name__=="__main__":
    main()