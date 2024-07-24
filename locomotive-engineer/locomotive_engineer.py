"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    f, s, one, *rest = each_wagons_id
    return [one, *missing_wagons, *rest, f, s]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route = {**route, "stops": list(kwargs.values())}
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    consolidated_dict = {**route, **more_route_information}
    return consolidated_dict


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # [*r1], [*r2], [*r3] = zip(*wagons_rows)
    # return [r1, r2, r3]
    wagons = []
    for col in range(len(wagons_rows[0])):
        new_row = []
        for row in range(len(wagons_rows)):
            new_row.append(wagons_rows[row][col])
        wagons.append(new_row)
    return wagons
