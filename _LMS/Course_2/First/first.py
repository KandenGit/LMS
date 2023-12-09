import pandas as pd

dict = {
    "Names": ["John", "Bill", "Edvard", "Bard", "Igor", "Yelisey", "Stepan"],
    "Ages": [12, 15, 18, 10, 11, 11, 11],
    "Student": [0, 0, 0, 1, 1, 0, 0]
}

df = pd.DataFrame(dict)
#sliced = pd.concat([df.head(3), df.tile(3)])
to_str = df.to_string(max_rows=6)
print(to_str)

df.to_csv('first.csv')
