from enum import Enum
import re

keywords = ["abstract", "continue", "for", "new", "switch",
            "assert", "default", "goto", "package", "synchronized",
            "boolean", "do", "if", "private", "this",
            "break", "double", "implements", "protected", "throw",
            "byte", "else", "import", "public", "throws",
            "case", "enum", "instanceof", "return", "transient",
            "catch", "extends", "int", "short", "try",
            "char", "final", "interface", "static", "void",
            "class", "finally", "long", "strictfp", "volatile",
            "const", "float", "native", "super", "while"]


class States(Enum):
    PARSING = 0
    CODE = 1
    COMMENT = 3


comment_character = "//"
multiline_comment_character_start = "/*"
multiline_comment_character_end = "*/"


def convert_word_to_keyword(word: str) -> str:
    if word in keywords:
        return f"<span>{word}</span>"
    return word


def get_file():
    with open("./example.java", "r") as f:
        return f.readlines()


class Parser:
    output = ""
    ignore_tags = True
    line_aggregator = ""

    def __init__(self, state):
        self.state = state

    def parse(self):
        if self.state == States.COMMENT:
            self.line_aggregator = self.line_aggregator.replace("\\r", "<br><br>")
            self.output += "<p>" + self.line_aggregator + "</p>"
        elif self.state == States.CODE:
            lines = self.line_aggregator.split('\n')
            helper = ""
            for x in range(len(lines)):
                background = "#111" if x % 2 == 0 else "black"
                error = "red" if "//error" in lines[x] else "black"
                lines[x] = lines[x].replace("//error", "")
                helper += f'<span style="background-color: {background}; display:inline-block;"><span style="float:left; background-color:{error};">{x}</span>   <span>{lines[x]}</span></span>'
            self.line_aggregator = helper
            for word in keywords:
                if word not in self.line_aggregator:
                    continue
                self.line_aggregator = self.line_aggregator.replace(f"{word} ", f"<span style=\"color: orange;\">{word}</span> ")

            self.line_aggregator = re.sub(r'(//.+)\n', r'<span style="color: gray !important;">\1</span>', self.line_aggregator)
            self.line_aggregator = re.sub(r'(\b\w+)\(', r'<span style="color: yellow;">\1</span>(', self.line_aggregator)
            self.output += '<pre style="background-color: black; color: white; padding: 15px; border: 4mm inset rgb(75, 52, 94)"><code style="display:flex; flex-direction: column">' + self.line_aggregator + "</code></pre>"
        self.line_aggregator = ""
        self.output += "\n"

    def aggregate_line(self, line):
        if self.ignore_tags:
            return

        self.line_aggregator += line

    def generate_file(self):
        f = open("./output.html", "w+")
        f.write(self.output)
        f.close()


def main():
    file_input = get_file()
    parser = Parser(States.PARSING)

    for line in file_input:
        parser.ignore_tags = False

        if line.startswith(multiline_comment_character_start + "comment:"):
            parser.state = States.COMMENT
            parser.ignore_tags = True
        if line.startswith(comment_character + "code:"):
            parser.state = States.CODE
            parser.ignore_tags = True
        elif line.startswith("endcomment" + multiline_comment_character_end) or line.startswith(
                comment_character + "endcode"):
            parser.parse()
            parser.state = States.PARSING
            continue

        parser.aggregate_line(line)

    parser.generate_file()


if __name__ == "__main__":
    main()
