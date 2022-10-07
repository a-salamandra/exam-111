# Задача консенсуса DNA ридов
# При чтении DNA последовательностей могут возникать единичные ошибки,
# выражающиеся в неверной букве в строке.
# Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
# в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
# Т.е. для строк
# ATTA
# ACTA
# AGCA
# ACAA
# консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
# Для входного списка из N строк одинаковой длины построить консенсус-строку.

dna_reads = [
    ['A', 'T', 'T', 'A'],
    ['A', 'C', 'T', 'A'],
    ['A', 'G', 'C', 'A'],
    ['A', 'C', 'A', 'A'],
             ]

def read_dna(dna_reads):

    read_length = len(dna_reads[0])
    letters_dictionary = {i: {} for i in range(read_length)}
    for read in dna_reads:
        for i in range(read_length):
            if read[i] not in letters_dictionary[i]:
                letters_dictionary[i][read[i]] = 1
            else:
                letters_dictionary[i][read[i]] += 1
    #print(letters_dictionary)

    result = ""
    for item in letters_dictionary.items():
        most_frequent_letter = max(item[1], key=item[1].get)
        #print(item[1])
        #print(l)
        result += "".join(most_frequent_letter)
    return result


print(read_dna(dna_reads))