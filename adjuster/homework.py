#!/usr/bin/env python3
import csv

from adjuster.rest_service import RestService


def main():

    creatives = RestService.http_get_creatives()
    campaigns = RestService.http_get_campaigns()
    results = aggregate(campaigns, creatives)
    write_to_csv(results, "test.csv")


def aggregate(parents, children):
    """
    Aggregate Data
    :return:
    """
    parent_map = {parent.id: parent for parent in parents}
    for child in children:
        child_id = child.parentId
        if child_id in parent_map:
            parent_map[child_id].impressions += child.impressions
            parent_map[child_id].clicks += child.clicks
    return parent_map


def write_to_csv(aggregated, file_name):
    """

    :param aggregated:
    :param file_name:
    :return:
    """
    lst = list(aggregated.values())
    open_file = open(file_name, 'w')
    with open_file:
        writer = csv.DictWriter(open_file, fieldnames=lst[0].__dict__.keys())
        writer.writeheader()
        for campaign in lst:
            writer.writerow(campaign.__dict__)


if __name__ == "__main__":
    """
    Homework
    """
    main()
