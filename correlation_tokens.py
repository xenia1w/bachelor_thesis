import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

excel_path = '/Users/xmena/Documents/TU/BachelorThesis/survey_results_tokens.xlsx'
all_prompts = ['s', 'ui', 'nsi', 'op', 'eng', 'end']
eval_criteria = ['correctness', 'friendliness', 'ease_of_reading', 'length']

columns_to_read = []

for prompt in all_prompts:
    for i in range(1, 4):
        for criteria in eval_criteria:
            column = criteria + '_' + prompt + str(i)
            columns_to_read.append(column)

df = pd.read_excel(excel_path, sheet_name='w_tokens', usecols=columns_to_read, nrows=59)
df_corr = pd.DataFrame(columns=['correctness', 'friendliness', 'ease_of_reading', 'output_tokens'])

for prompt in all_prompts:
    for i in range(1, 4):
        correctness = str('correctness' + '_' + prompt + str(i))
        friendliness = str('friendliness' + '_' + prompt + str(i))
        ease_of_reading = str('ease_of_reading' + '_' + prompt + str(i))
        output_tokens = str('length' + '_' + prompt + str(i))

        new_df = df[[correctness, friendliness, ease_of_reading, output_tokens]].copy()
        new_df.columns = ['correctness', 'friendliness', 'ease_of_reading', 'output_tokens']

        df_corr = pd.concat([df_corr, new_df])

correlation_matrix = df_corr.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="crest", fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

