from neo4j.v1 import GraphDatabase, basic_auth, Node

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))


def find_paper_by_title(title):
    with driver.session() as session:
        result = session.run('MATCH (paper:Paper {title:{title}}) RETURN paper.title', {"title": title})
        nodes = []
        for item in result:
            nodes.append(item)
        return result

