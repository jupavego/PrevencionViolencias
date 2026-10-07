# -*- coding: utf-8 -*-
import importlib, sys, os
sys.path.insert(0, os.path.dirname(__file__))
for n in sys.argv[1:] or ['0','1','2','3','4','5']:
    try:
        m = importlib.import_module(f'cap{n}')
    except ModuleNotFoundError:
        continue
    open(('portada' if n == '0' else f'capitulo{n}') + '.html', 'w', encoding='utf-8').write(m.html())
    print('ok', n)
