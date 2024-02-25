c = {
 "Types": ["int", "float", "double", "char", "void", "bool", "string"],
 "Keywords": [ "auto", "break", "case", "const", "continue", "default", "do", "else", "enum", "extern", "for", "goto", "if", "register", "return", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "volatile", "while"],
   "Operators": ["+", "-", "*", "/", "%", "=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>"],
    "Punctuation": [",", ";", ":", ".", "->", "(", ")", "[", "]", "{", "}"],
    "Data Types": ["int", "float", "double", "char", "void"],
    "Control Flow": ["if", "else", "switch", "case", "default", "for", "while", "do", "break", "continue", "return", "goto"],
    "Modifiers": ["const", "volatile", "static", "extern", "register"],
    "Storage Classes": ["auto", "register", "static", "extern"],
    "Preprocessor Directives": ["#include", "#define", "#ifdef", "#ifndef", "#endif", "#if", "#else", "#elif", "#pragma"],
    "Function Specifiers": ["inline", "noinline", "noreturn"],
    "Miscellaneous": ["sizeof", "typedef", "enum", "struct", "union"],
    "Basic Functions": ["printf", "scanf", "getchar", "putchar", "gets", "puts", "malloc", "calloc", "realloc", "free", "exit", "abs", "labs", "fabs", "sqrt", "pow", "exp", "log", "log10", "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "sinh", "cosh", "tanh", "ceil", "floor", "fmod", "frexp", "ldexp", "modf", "rand", "srand", "strtod", "strtol", "strtoul", "system", "time", "difftime", "mktime", "clock", "strftime", "asctime", "ctime", "gmtime", "localtime", "strftime", "asctime", "ctime", "gmtime", "localtime", "time", "difftime", "mktime", "clock", "strftime", "asctime", "ctime", "gmtime", "localtime", "strftime", "asctime", "ctime", "gmtime", "localtime"],
}

python = {
    "Keywords": ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"],
    "Operators": ["+", "-", "*", "/", "%", "=", "==", "!=", ">", "<", ">=", "<=", "and", "or", "not", "is", "in", "not in"],
    "Punctuation": [",", ";", ":", ".", "(", ")", "[", "]", "{", "}"],
    "Data Types": ["int", "float", "bool", "str", "list", "tuple", "set", "dict"],
    "Control Flow": ["if", "else", "elif", "while", "for", "break", "continue", "pass", "return", "try", "except", "finally", "raise", "assert"],
    "Modifiers": ["global", "nonlocal"],
    "Built-in Functions": ["print", "input", "len", "range", "type", "int", "float", "str", "list", "tuple", "set", "dict", "bool", "abs", "max", "min", "sum", "sorted", "reversed", "zip", "enumerate", "map", "filter"],
    "Miscellaneous": ["import", "from", "as", "lambda", "yield", "async", "await"],
}

java = {
    "Keywords": ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private", "protected", "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try", "void", "volatile", "while"],
    "Operators": ["+", "-", "*", "/", "%", "=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", ">>>", "++", "--", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>="],
    "Punctuation": [",", ";", ":", ".", "->", "(", ")", "[", "]", "{", "}", "@", "::"],
    "Data Types": ["boolean", "byte", "char", "short", "int", "long", "float", "double", "void"],
    "Control Flow": ["if", "else", "switch", "case", "default", "while", "do", "for", "break", "continue", "return", "try", "catch", "finally", "throw"],
    "Modifiers": ["abstract", "final", "native", "private", "protected", "public", "static", "synchronized", "transient", "volatile"],
    "Exception Handling": ["try", "catch", "finally", "throw", "throws"],
    "Access Modifiers": ["private", "protected", "public"],
    "Miscellaneous": ["import", "package", "class", "interface", "extends", "implements", "this", "super", "new", "instanceof", "enum", "assert"],
    "Annotations": ["@Override", "@Deprecated", "@SuppressWarnings"],
    "Built-in Classes": ["Object", "String", "System", "Math", "Integer", "Double", "Float", "Boolean", "Character", "Byte", "Short", "Long", "Void", "Exception", "RuntimeException", "Throwable", "Error", "Class", "Thread", "Runnable", "ThreadGroup", "Process", "Runtime", "Package", "ClassLoader", "System", "Runtime", "ProcessBuilder", "StringBuilder", "StringBuffer", "Iterable", "Collection", "List", "Set", "Map", "Iterator", "Comparator", "Arrays", "Collections"],
    "Built-in Methods": ["equals", "hashCode", "toString", "getClass", "notify", "notifyAll", "wait", "finalize", "clone", "valueOf", "parseInt", "parseFloat", "parseDouble", "parseBoolean", "toString", "length", "charAt", "substring", "toUpperCase", "toLowerCase", "trim", "split", "concat", "replace", "startsWith", "endsWith", "contains", "isEmpty", "compareTo", "sort", "reverse", "add", "remove", "containsKey", "containsValue", "get", "put", "remove", "size", "isEmpty", "clear", "keySet", "values", "entrySet"]
}


asciidoc = {
    "titles": {
    "h1": "=",
    "h2": "==",
    "h3": "===",
    "h4": "===="
    },

    "syntax": {
       "bold": "*",
        "italic": "_",
        "bold_italic": "*_",
        "monospace": "`",
        "monospace_bold": "`*",
        "monospace_italic": "`_",
        "monospace_bold_italic": "`*_",
    },
    
    "lists": {
        "unordered": "*",
        "ordered": "."
    },
    
    "links": {
        "external": "http://",
        "internal": "link:"
    },
    
    "description_lists": {
        "term": "::",
        "horizontal": "[horizontal]",
    },
    
    "tables": {
        "header": "|===",
        "row": "|",
        "footer": "|==="
    }
}
