from collections import defaultdict
from neo4j.v1 import GraphDatabase, basic_auth
from random import choice
import papers as pp

NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'neo4j'
URI = "bolt://localhost:7687"
PATHS = 1000

def explore_diameter(papers):
    print("Approximating NEO4j diameter with a sample of ")
    driver = GraphDatabase.driver(URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    session = driver.session()

    count = 0
    sum = 0.0
    with driver.session() as session:

        for _ in range(PATHS):
            id1 = choice(list(papers.keys()))
            id2 = choice(list(papers.keys()))

            result = session.run(
                "MATCH path=shortestPath((p1:Paper {id:{id1}})-[*0..15]-(p2:Paper {id:{id2}})) \
                RETURN relationships(path)", {"id1": id1, "id2": id2})

            for record in result:
                sum += len(record["relationships(path)"])
            
            count += 1
            if count % 100 == 0: print("Already computed {0} paths".format(count))

    print("The diameter is {0}".format(sum/count))

papers = pp.Papers()
papers.load_papers()
explore_diameter(papers.papers)
