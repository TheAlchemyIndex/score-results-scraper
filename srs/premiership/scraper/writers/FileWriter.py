from srs.premiership.constants import OriginalColumns, Urls, Directories
from srs.premiership.scraper.writers.CsvWriter import write_to_csv
from srs.premiership.scraper.seasons.SeasonScraper import scrape_results

# Constant list for field names
FIELD_NAMES = [OriginalColumns.DATE, OriginalColumns.TIME, OriginalColumns.TEAM1_NAME, OriginalColumns.TEAM1_SCORE,
               OriginalColumns.TEAM2_NAME, OriginalColumns.TEAM2_SCORE, OriginalColumns.VENUE, OriginalColumns.REFEREE,
               OriginalColumns.TOTAL_SCORE, OriginalColumns.WINNER, OriginalColumns.EXTRA_TIME, OriginalColumns.DAY,
               OriginalColumns.MONTH, OriginalColumns.YEAR, OriginalColumns.SEASON]


def write_to_individual_files(first_season_start, first_season_end, last_season_end):
    """Writes match data to individual csv files for each season.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:
        url = Urls.PREMIERSHIP_URL_START + str(first_season_start) + "-" + str(first_season_end) \
              + Urls.PREMIERSHIP_URL_END
        file_name = Directories.INDIVIDUAL + str(first_season_start) + "-" + str(first_season_end) \
                    + Directories.FILE_NAME_SINGLE_SEASONS_END

        write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")
        first_season_start += 1
        first_season_end += 1


def write_to_single_file(first_season_start, first_season_end, last_season_end):
    """Writes match data to a single csv file containing data for all seasons.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    file_name = Directories.GROUPED + Directories.FILE_NAME_ALL_SEASONS_START + str(first_season_start) \
                + "-" + str(last_season_end) + ".csv"

    # Flag to check if the first season in range has been written to file
    first_season = True

    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:
        url = Urls.PREMIERSHIP_URL_START + str(first_season_start) + "-" + str(first_season_end) \
              + Urls.PREMIERSHIP_URL_END

        # If the first season in range is being written, the existing file is overwritten
        if first_season:
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")
            first_season = False
            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1
        # Otherwise the existing file is appended with the second season results onwards
        else:
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "a")
            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1
