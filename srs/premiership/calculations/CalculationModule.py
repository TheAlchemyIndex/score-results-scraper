import pandas as pd

from srs.premiership.calculations.calculators.MeanCalculator import calc_rolling_5_scores_mean
from srs.premiership.calculations.filters.ScoreFilter import filter_results
from srs.premiership.calculations.generators.CodeGenerator import generate_category_codes
from srs.premiership.constants import OriginalColumns, CalculatedColumns


def create_calculated_columns(first_season_start, first_season_end, last_season_end):
    """Reads match data from season csv data, creates calculated columns and writes to new files.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    while first_season_end <= last_season_end:
        file_path = r"data/rawData/groupedSeasons/All Seasons - " + str(first_season_start) + "-" \
                    + str(last_season_end) + ".csv"

        # Creates df from file path and converts date column to datetime
        df = pd.read_csv(file_path)
        df[OriginalColumns.DATE] = pd.to_datetime(df[OriginalColumns.DATE])

        # Filters to remove non-numeric data from scores and convert scores to numeric values
        df_filtered = filter_results(df)

        # Columns for calculating the mean of the last 5 scores for and against the home team
        last_5_scores_home_cols = [OriginalColumns.TEAM1_SCORE, OriginalColumns.TEAM2_SCORE]
        last_5_scores_home_new_cols = [CalculatedColumns.AVG_HOME_LAST_5_SCORES,
                                       CalculatedColumns.AVG_HOME_LAST_5_SCORES_AGAINST]

        # Calculates rolling mean of the last 5 scores for and against for each home team
        df_calc_last_5_scores = df_filtered.groupby(OriginalColumns.TEAM1_NAME) \
            .apply(lambda x: calc_rolling_5_scores_mean(x, last_5_scores_home_cols, last_5_scores_home_new_cols))
        df_calc_last_5_scores = df_calc_last_5_scores.droplevel(OriginalColumns.TEAM1_NAME)

        # Generates numeric codes for key columns that contain strings
        df_codes = generate_category_codes(df_calc_last_5_scores)

        # Sorts by date in ascending order
        df_codes.sort_values(by='date', inplace=True)

        # Writes season data to csv and increments first_season_end
        df_codes.to_csv("data/calculatedData/Results - " + str(first_season_start) + "-"
                        + str(last_season_end) + ".csv")
        first_season_end += 1