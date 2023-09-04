""" В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
    Не учитывать знаки препинания и регистр символов.
    За основу возьмите любую статью из википедии или из документации к языку.
"""

import re

source_string = "Python - поразительный язык. Он поражает прежде всего тем, что в течение \
                многих лет остается актуальным и продолжает развиваться. \
                С давних пор одним из важнейших достоинств Python была операционная \
                совместимость, благодаря которой было неважно, что за операционная система \
                у вас или у ваших клиентов. Если для этой ОС существовал интерпретатор \
                Python, то ваши программы на Python в ней работали. И что еще важнее, \
                программы работали всегда одинаково в разных ОС. Однако в наше время это \
                качество уже стало обычным и для других современных языков программирования, \
                которые обеспечивают аналогичные возможности операционной совместимости. \
                Кроме того, с развитием облачных служб, приложений на основе неб-технологий \
                и надежных программных средств виртуализации уже не столь важно, чтобы \
                язык программирования работал во многих ОС. \
                Похоже, в наши дни на первый план выходит продуктивность работы программистов. \
                В постоянном стремлении к новшествам часто бывает важно сделать \
                прототип, который можно опробовать в полевых условиях на реальных пользователях, \
                а затем без проволочек развивать его до стадии полноценного продукта. \
                Python позволяет программистам проходить этот путь очень быстро. Официальный \
                каталог пакетов Python Package Index - огромная подборка программных библиотек \
                и фреймворков, которые вы можете легко использовать в своих \
                проектах. Благодаря этому каталогу вы тратите на работу гораздо меньше времени \
                и усилий. Широчайшая доступность библиотек, созданных сообществом, \
                в сочетании с четким и лаконичным синтаксисом, ориентированным на удобочитаемость \
                кода, облегчает создание и сопровождение программных продуктов. \
                Поэтому Python показывает вьщающиеся результаты по части продуктивности \
                работы программистов"

# for symbol in ",!?.-":
#    source_string = source_string.replace(symbol, "")
source_string = re.sub(r'\W ', ' ', source_string.lower())

freq_dict = dict()

for word in source_string.split():
    freq_dict[word] = freq_dict.get(word, 0) + 1

sorted_tuple = sorted(freq_dict.items(), key=lambda x: -x[1])

for nums in sorted_tuple[:10]:
    print(f"слово: '{nums[0]}' встречается {nums[1]} раз(а)")
