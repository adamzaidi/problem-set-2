'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import seaborn as sns

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def first_question(felony_pred_universe):
    cat1 = sns.catplot(
        data=felony_pred_universe,
        x='charge_degree',
        y='prediction_felony',
        kind='bar'
    )
    cat1.savefig('./data/part4_plots/catplot_felony_prediction.png', bbox_inches='tight')

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def second_question(felony_pred_universe):
    cat2 = sns.catplot(
        data=felony_pred_universe,
        x='charge_degree',
        y='prediction_nonfelony',
        kind='bar'
    )
    cat2.savefig('./data/part4_plots/catplot_nonfelony_prediction.png', bbox_inches='tight')
    # In a print statement, answer the following question: What might explain the difference between the plots?
    print("People with felony charges seem to have higher predicted chances of being rearrested for a felony The nonfelony predictions dont change as much, which might mean the model is focusing more on whether the current charge is a felony.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def third_question(felony_pred_universe):
    cat3 = sns.catplot(
        data=felony_pred_universe,
        x='charge_degree',
        y='prediction_felony',
        hue='y_felony',
        kind='bar'
    )
    cat3.savefig('./data/part4_plots/catplot_felony_prediction_by_outcome.png', bbox_inches='tight')

    # In a print statement, answer the following question: 
    # What does it mean that prediction for arrestees with a current felony charge, 
    # but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
    # but who did get rearrested for a felony crime?
    print("It shows that the model puts a lot of weight on whether someone's current charge is a felony. It predicts them as higher risk even if they dont get rearrested, and it underrates people with misdemeanors who do end up reoffending. Basically, it might be missing other factors that better explain who actually gets rearrested.")
