'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, felony_pred_universe = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1
    part3.first_question(pred_universe)

    # 2
    part3.second_question(pred_universe)

    # 3
    part3.third_question(pred_universe)

    # 4
    part3.fourth_question(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1
    part4.first_question(felony_pred_universe)

    # 2
    part4.second_question(felony_pred_universe)

    # 3
    part4.third_question(felony_pred_universe)

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    part5.first_question(felony_pred_universe)

    # 2
    part5.second_question(felony_pred_universe)


if __name__ == "__main__":
    main()
