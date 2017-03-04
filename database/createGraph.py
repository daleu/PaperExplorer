from collections import defaultdict
from neo4j.v1 import GraphDatabase, basic_auth
import papers as pp

NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'neo4j'
URI = "bolt://localhost"


def create_nodes(papers):
    print("Creating NEO4j nodes")
    driver = GraphDatabase.driver(URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

    count = 0
    with driver.session() as session:
        for key, value in papers.items():
            session.run(
                "CREATE (p:Paper {id: {id}, title: {title}, author: {author}, date: {date}})",
                {"id": key, "title": value.title, "author": value.author, "date": value.date})

            count += 1
            if count % 1000 == 0: print("Already processed {0} papers".format(count))


def create_edges(papers):
    print("Creating NEO4j edges")
    driver = GraphDatabase.driver(URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

    count = 0
    with driver.session() as session:

        # Create an index on id to speed up the insertion of edges
        session.run("CREATE INDEX ON :Paper(id)")

        for key, value in papers.items():
            for citation in value.citations:
                session.run(
                    "MATCH (p1:Paper {id: {id1}}), (p2:Paper {id: {id2}}) \
                    CREATE (p1)-[:Cites]->(p2) CREATE (p2)-[:IsCitedBy]->(p1)",
                    {"id1": key, "id2": citation})

            count += 1
            if count % 1000 == 0: print("Already processed {0} papers".format(count))


papers = pp.Papers()
papers.load_papers()
create_nodes(papers.papers)
create_edges(papers.papers)
