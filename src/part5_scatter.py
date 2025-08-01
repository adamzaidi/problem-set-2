'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def first_question(felony_pred_universe):
    scatter1 = sns.lmplot(
        data=felony_pred_universe,
        x='prediction_felony',
        y='prediction_nonfelony',
        hue='has_felony_charge',
        fit_reg=False
    )
    scatter1.savefig('./data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')

    # In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
    print("The dots on the right side represent people with really high predicted felony risk. Most of them seem to have felony charges, which shows the model is heavily influenced by the charge type when predicting felony risk.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def second_question(felony_pred_universe):
    scatter2 = sns.lmplot(
        data=felony_pred_universe,
        x='prediction_felony',
        y='y_felony',
        fit_reg=False
    )
    scatter2.savefig('./data/part5_plots/scatter_felony_prediction_vs_outcome.png', bbox_inches='tight')

    # In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
    print("The plot shows that higher predictions dont always line up with actual rearrests. So the model doesnt look well-calibrated because it seems to overpredict risk for some and underpredict for others.")
