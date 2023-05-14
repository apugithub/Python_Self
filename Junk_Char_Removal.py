import re
import pandas as pd

df = pd.read_csv('<csv_with_junk_char>').fillna('')
df['Junk_Char-col'] = df['Junk_Char-col'].map(lambda x: re.sub('[^A-Za-z0-9]+', ' ', x))

df.to_csv('<csv_output_path>')