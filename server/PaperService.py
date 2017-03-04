import DatabaseService

neo4j = DatabaseService


def get_paper(title):
    nodes = neo4j.find_paper_by_title(title)
    return nodes
