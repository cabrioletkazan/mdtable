# mdtable

Turn a CSV file into a Markdown table. Pure Python, no dependencies.

```
$ printf 'name,qty\napple,3\npear,12\n' | python -m mdtable -a lr
| name | qty |
| :--- | ---: |
| apple | 3 |
| pear | 12 |
```

## Use

```
python -m mdtable data.csv            # read a file
cat data.csv | python -m mdtable      # or stdin
python -m mdtable -d ';' data.csv     # other separators ('\t' for tabs)
python -m mdtable -a lcr data.csv     # left, centre, right alignment
```

From Python:

```python
from mdtable import to_markdown
print(to_markdown("a,b\n1,2\n"))
```

## Tests

```
python -m unittest discover -s tests
```

## Licence

MIT
