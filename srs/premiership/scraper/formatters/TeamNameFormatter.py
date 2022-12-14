import re


def team_name_formatter(team_name_data):
    """Takes team information and reformats it.

    :param team_name_data: Team name information about a match
    :return: A reformatted version of the team name
    """
    # Removes any brackets and characters in between if found in the date
    formatted_team_name = re.sub("\((.*?)\)", "", team_name_data, flags=re.DOTALL).strip()

    if formatted_team_name == "Bath Rugby":
        return "Bath"
    elif formatted_team_name == "Bristol Bears":
        return "Bristol"
    elif formatted_team_name == "Exeter Chiefs":
        return "Exeter"
    elif formatted_team_name == "Leeds Carnegie":
        return "Leeds"
    elif formatted_team_name == "Leicester Tigers":
        return "Leicester"
    elif formatted_team_name == "Gloucester Rugby":
        return "Gloucester"
    elif formatted_team_name == "Newcastle Falcons":
        return "Newcastle"
    elif formatted_team_name == "Northampton Saints":
        return "Northampton"
    elif formatted_team_name == "Sale Sharks":
        return "Sale"
    elif formatted_team_name == "London Wasps":
        return "Wasps"
    elif formatted_team_name == "Worcester Warriors":
        return "Worcester"
    else:
        return formatted_team_name
