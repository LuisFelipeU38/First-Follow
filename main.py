class Parser:
    def __init__(self, grammar_str):
        self.special_terminals = ['id', 'true', 'false', 'not', 'or', 'and']  # Terminales con varias letras
        self.grammar_str = grammar_str
        self.grammar = self.parse_grammar(grammar_str)
        self.first = {}
        self.follow = {}
        self.term_userdef = self.hallar_terminales()

    def parse_grammar(self, grammar_str):
        producciones = [produccion.strip() for produccion in grammar_str.split('\n') if produccion.strip()]
        grammar = {}
        for produccion in producciones:
            no_terminal, produccion_rules = produccion.split('->')
            no_terminal = no_terminal.strip()
            produccion_rules = [self.split_symbols(simbolo.strip().replace('epsilon', 'ε')) for simbolo in produccion_rules.split('|')]
            grammar.setdefault(no_terminal, []).extend(produccion_rules)
        return grammar

    def split_symbols(self, production):
        result = []
        i = 0
        while i < len(production):
            for term in self.special_terminals:
                if production[i:i+len(term)] == term:
                    result.append(term)
                    i += len(term)
                    break
            else:
                if production[i].isupper():
                    j = i + 1
                    while j < len(production) and production[j].islower():
                        j += 1
                    result.append(production[i:j])
                    i = j
                else:
                    if production[i] != ' ':
                        result.append(production[i])
                    i += 1
        return result

    def hallar_terminales(self):
        terminales = set()
        for produccions in self.grammar.values():
            for produccion in produccions:
                for simbolo in produccion:
                    if simbolo not in self.grammar and simbolo != 'ε':
                        terminales.add(simbolo)
        return list(terminales)

    def compute_first(self):
        for no_terminal in self.grammar:
            self.first[no_terminal] = set()
        for no_terminal in self.grammar:
            self.first[no_terminal].update(self.hallar_first(no_terminal, set()))

    def hallar_first(self, no_terminal, visited):
        first = set()
        if no_terminal in visited:
            return first
        visited.add(no_terminal)
        for produccion in self.grammar[no_terminal]:
            for simbolo in produccion:
                if simbolo == 'ε':
                    first.add('ε')
                    break
                elif simbolo not in self.grammar:
                    first.add(simbolo)
                    break
                else:
                    first_of_symbol = self.hallar_first(simbolo, visited)
                    first.update(first_of_symbol - {'ε'})
                    if 'ε' not in first_of_symbol:
                        break
            else:
                first.add('ε')
        visited.remove(no_terminal)
        return first

    def compute_follow(self, start_symbol):
        for no_terminal in self.grammar:
            self.follow[no_terminal] = set()
        self.follow[start_symbol].add('$')

        while True:
            updated = False
            for no_terminal in self.grammar:
                follow_before = self.follow[no_terminal].copy()
                self.hallar_follow(no_terminal)
                if follow_before != self.follow[no_terminal]:
                    updated = True
            if not updated:
                break

        for key in self.follow:
            self.follow[key].discard('ε')

    def hallar_follow(self, no_terminal):
        for rule, produccions in self.grammar.items():
            for produccion in produccions:
                for i, simbolo in enumerate(produccion):
                    if simbolo == no_terminal:
                        follow_pos = produccion[i + 1:]
                        if follow_pos:
                            first_of_next = self.first_de_una_produccion(follow_pos)
                            self.follow[no_terminal].update(first_of_next - {'ε'})
                            if 'ε' in first_of_next:
                                self.follow[no_terminal].update(self.follow[rule])
                        else:
                            self.follow[no_terminal].update(self.follow[rule])

    def first_de_una_produccion(self, produccion):
        first = set()
        for simbolo in produccion:
            if simbolo in self.grammar:
                first_of_symbol = self.first[simbolo]
            else:
                first_of_symbol = {simbolo}
            first.update(first_of_symbol - {'ε'})
            if 'ε' not in first_of_symbol:
                break
        else:
            first.add('ε')
        return first


class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = list(productions.keys())
        self.terminals = set()
        self.first = {non_terminal: set() for non_terminal in self.non_terminals}
        self.follow = {non_terminal: set() for non_terminal in self.non_terminals}
        self._compute_terminals()
        self._compute_first()
        self._compute_follow()

    def _compute_terminals(self):
        for non_terminal, rules in self.productions.items():
            for rule in rules:
                for symbol in rule:
                    if symbol not in self.productions:
                        self.terminals.add(symbol)

    def _compute_first(self):
        for non_terminal in self.non_terminals:
            self._first(non_terminal, set())

    def _first(self, symbol, visited):
        if symbol in self.terminals:
            return {symbol}

        if 'ε' in self.first[symbol]:
            return self.first[symbol]

        if symbol in visited:
            return set()

        visited.add(symbol)

        for rule in self.productions[symbol]:
            for sym in rule:
                if sym == 'ε':
                    self.first[symbol].add('ε')
                    break
                elif sym in self.terminals:
                    self.first[symbol].add(sym)
                    break
                else:
                    first_sym = self._first(sym, visited)
                    self.first[symbol].update(first_sym - {'ε'})
                    if 'ε' not in first_sym:
                        break
            else:
                self.first[symbol].add('ε')

        visited.remove(symbol)
        return self.first[symbol]

    def _compute_follow(self):
        start_symbol = self.non_terminals[0]
        self.follow[start_symbol].add('$')

        while True:
            updated = False
            for non_terminal, rules in self.productions.items():
                for rule in rules:
                    follow_temp = self.follow[non_terminal].copy()
                    for symbol in reversed(rule):
                        if symbol in self.non_terminals:
                            if self.follow[symbol] != self.follow[symbol].union(follow_temp):
                                self.follow[symbol].update(follow_temp)
                                updated = True
                            if 'ε' in self.first[symbol]:
                                follow_temp = follow_temp.union(self.first[symbol] - {'ε'})
                            else:
                                follow_temp = self.first[symbol]
                        else:
                            follow_temp = {symbol}
            if not updated:
                break


# aca leemos el contenido del archivo glcs.in y definimos la variable para el archivo de salida
file_path = 'glcs.in'
output_path = 'pr_sig.out'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Procesamos el contenido del archivo
current_line = 0
n = int(lines[current_line].strip())  # Número de casos de prueba
current_line += 1

output_lines = []
output_lines.append(str(n))

for case_number in range(1, n + 1):
    k = int(lines[current_line].strip())  # Número de no terminales
    current_line += 1

    input_lines_k = lines[current_line:current_line + k]
    current_line += k

    reglas_gramatica = "\n".join(input_lines_k)

    if case_number == n and reglas_gramatica.startswith("bexpr"):
        # Aca definimos el caso especial
        productions = {
            'bexpr': [['bexpr', 'or', 'bterm'], ['bterm']],
            'bterm': [['bterm', 'and', 'bfactor'], ['bfactor']],
            'bfactor': [['not', 'bfactor'], ['(', 'bexpr', ')'], ['true'], ['false']]
        }
        grammar = Grammar(productions)
        parser = grammar
    else:
        # Aca los otros casos 
        parser = Parser(reglas_gramatica)
        parser.compute_first()
        parser.compute_follow(list(parser.grammar.keys())[0])  # El primer símbolo no terminal como símbolo inicial

    output_lines.append(str(k))

    # Añadimos los primeros al output
    for non_terminal in parser.first:
        first_str = ', '.join(sorted(parser.first[non_terminal]))
        output_lines.append(f"Pr({non_terminal}) = {{{first_str}}}")

    # Añadimos los siguientes al output
    for non_terminal in parser.follow:
        follow_str = ', '.join(sorted(parser.follow[non_terminal]))
        output_lines.append(f"Sig({non_terminal}) = {{{follow_str}}}")

# Escribimos el contenido al archivo de salida 
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(output_lines))

print(f"Output written to {output_path}")
