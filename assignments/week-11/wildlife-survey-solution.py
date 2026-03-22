# Solution file - instructor reference only

def count_observations(data):
    """
    Recursively count all integer observation values in a nested list.
    Base case: item is an integer -> return it directly.
    Recursive case: item is a list -> sum results of recursive calls.
    """
    total = 0
    for item in data:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += count_observations(item)
    return total


def find_species(data, target):
    """
    Recursively search nested survey data for all occurrences of target string.
    Returns a flat list of matches found at any depth.
    """
    results = []
    for item in data:
        if isinstance(item, str) and item == target:
            results.append(item)
        elif isinstance(item, list):
            results.extend(find_species(item, target))
    return results


def flatten_survey(data):
    """
    Recursively flatten a nested list to a single level.
    Non-list items are added directly; lists are flattened recursively.
    """
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten_survey(item))
        else:
            result.append(item)
    return result


def apply_formula(func, measurements):
    """
    Apply func to every item in measurements and return results as a list.
    Implements the map pattern manually using a loop.
    """
    results = []
    for item in measurements:
        results.append(func(item))
    return results


def get_notable_species(species_list, threshold):
    """
    Return only species records where observation count exceeds threshold.
    Use filter() with a lambda.
    """
    return list(filter(lambda record: record[1] > threshold, species_list))


def format_report_lines(records):
    """
    Format each (name, count, region) tuple as a display string.
    Use map() with a lambda.
    """
    return list(map(lambda r: f"  {r[0]:<22} {r[1]:<8} {r[2]}", records))
