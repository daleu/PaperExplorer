from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))


def find_paper_by_title(title):
    with driver.session() as session:
        result = session.run("MATCH(paper: Paper)-[:Cites]->(citation:Paper) WHERE paper.title =~ {title} RETURN properties(paper) as root, properties(citation) as child",
                             {"title": title + '.*'})
        for item in result:
            print(item)
        return result
