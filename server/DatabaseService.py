#!/usr/bin/env python3
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth('neo4j', 'neo4j'))

def list_by_title(title):
    with driver.session() as session:
        result1 = session.run('MATCH (node: Paper) WHERE node.title =~ {title} RETURN node', {'title':title+'.*'})
        nodes = []
        for r1 in result1:
            node = {}
            n1 = r1['node']
            id1 = n1['id']
            properties1 = dict(n1.items())
            result2 = session.run('MATCH (paper {id:{id}})-[:Cites]->(children) RETURN children', {'id':id1})
            children = {}
            for r2 in result2:
                n2 = r2['children']
                id2 = n2['id']
                properties2 = dict(n2.items())
                children[id2] = properties2
            properties1['children'] = children
            node[id1] = properties1
            nodes.append(node)
        return nodes
