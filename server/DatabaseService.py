from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))


def list_by_title(title):
    with driver.session() as session:
        result = session.run("MATCH (p:Paper) WHERE p.title =~ {title} RETURN p", {"title": ".*"+title + ".*"})
        nodes = []
        for item in result:
            node = item["p"].__dict__["properties"]
            nodes.append(node)
    return nodes
