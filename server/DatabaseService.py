#!/usr/bin/env python3
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth('neo4j', 'neo4j'))


def explore(root, depth):
    id = root['id']
    properties = dict(root.items())
    if depth == 0:
        properties['children'] = []
    else:
        with driver.session() as session:
            result = session.run('MATCH (node {id:{id}})-[:Cites]->(child) RETURN child', {'id':id})
            children = []
            for record in result:
                child = record['child']
                children.append(explore(child, depth - 1))
            properties['children'] = children
    return properties


def get_by_title(title):
    with driver.session() as session:
        result = session.run('MATCH (node: Paper) WHERE node.title CONTAINS {title} RETURN node', {'title': title})
        for record in result:
            return explore(record['node'], 2)


def get_by_id(id):
    with driver.session() as session:
        result = session.run('MATCH (node: Paper) WHERE node.id={id} RETURN node', {'id': id})
        for record in result:
            return explore(record['node'], 2)


def list(title):
    with driver.session() as session:
        result = session.run("MATCH (p:Paper) WHERE p.title CONTAINS {title} RETURN p", {"title": title})
        nodes = []
        for item in result:
            node = item['p']
            nodes.append(dict(node.items()))
        return nodes
