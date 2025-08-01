'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def first_question(pred_universe):
    sns.countplot(data=pred_universe, 
                  x='fta')
    plt.title("FTA Counts")
    plt.savefig('./data/part3_plots/bar_fta.png', bbox_inches='tight')

# 2. Hue the previous barplot by sex
def second_question(pred_universe):
    sns.countplot(data=pred_universe, 
                  x='fta', 
                  hue='sex')
    plt.title("FTA Counts by Sex")
    plt.savefig('./data/part3_plots/bar_fta_by_sex.png', bbox_inches='tight')

# 3. Plot a histogram of age_at_arrest
def third_question(pred_universe):
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=20)
    plt.title("Age at Arrest Distribution")
    plt.savefig('./data/part3_plots/hist_age_at_arrest.png', bbox_inches='tight')

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100
def fourth_question(pred_universe):
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=[18,21,30,40,100])
    plt.title("Age at Arrest (Grouped Bins)")
    plt.savefig('./data/part3_plots/hist_age_groups.png', bbox_inches='tight')
