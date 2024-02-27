import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr


def calculate_and_print_pvalues(df):
    # get rid of the NaN values, otherwise one is unable to use this function
    df_cleaned = df.dropna()
    for column_i in df.columns:
        for column_j in df.columns:
            if column_i == column_j:
                continue
            else:
                corr_coeff, p_val = pearsonr(df_cleaned[column_i], df_cleaned[column_j])
                print(column_i + " AND " + column_j)
                print("Correlation Coeefficient: ", corr_coeff, "p-value: ", p_val)


excel_path = 'survey_results.xlsx'
all_prompts = ['s', 'ui', 'nsi', 'op', 'eng', 'end']
eval_criteria = ['correctness', 'friendliness', 'ease_of_reading', 'length']

columns_to_read = []

# Specifying all the columns that should be extracted from the Excel file
for prompt in all_prompts:
    for i in range(1, 4):
        for criteria in eval_criteria:
            column = criteria + '_' + prompt + str(i)
            columns_to_read.append(column)

df = pd.read_excel(excel_path, sheet_name='w_tokens', usecols=columns_to_read, nrows=59)

# creating a main and empty DataFrame with four columns of the features for which we would like to plot the
# correlation matrix
df_corr = pd.DataFrame(columns=['correctness', 'friendliness', 'ease_of_reading', 'output_tokens'])

for prompt in all_prompts:
    for i in range(1, 4):
        correctness = str('correctness' + '_' + prompt + str(i))
        friendliness = str('friendliness' + '_' + prompt + str(i))
        ease_of_reading = str('ease_of_reading' + '_' + prompt + str(i))
        output_tokens = str('length' + '_' + prompt + str(i))

        new_df = df[[correctness, friendliness, ease_of_reading, output_tokens]].copy()
        new_df.columns = ['correctness', 'friendliness', 'ease_of_reading', 'output_tokens']

        # attach the specified columns to the main DataFrame (df_corr)
        df_corr = pd.concat([df_corr, new_df])

# calculate the correlation matrix
correlation_matrix = df_corr.corr()

# calculating the p-values
calculate_and_print_pvalues(df_corr)

# plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="crest", fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

