#!/usr/bin/env python3
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth('neo4j', 'neo4j'))


def explore(root, depth):
    name = dict(root.items())['name']
    properties = dict(root.items())
    if depth == 0:
        properties['children'] = []
    else:
        with driver.session() as session:
            result = session.run('MATCH (u {name:{name}})-[:Edge]->(v) RETURN v', {'name': name})
            children = []
            for record in result:
                child = record['v']
                children.append(explore(child, depth - 1))
            properties['children'] = children
    return properties


def get_by_title(title):
    with driver.session() as session:
        result = session.run('MATCH (node: Paper) WHERE node.title CONTAINS {title} RETURN node', {'title': title})
        for record in result:
            return explore(record['node'], 10)


def get_by_name(name):
    name = int(name)
    with driver.session() as session:
        result = session.run('MATCH (n) WHERE n.name={name} RETURN n', {'name': name})
        for record in result:
            d = explore(record['n'], 10)
            return d


def get_by_id(id):
    id = int(id)
    with driver.session() as session:
        result = session.run('MATCH (node: Paper) WHERE node.id={id} RETURN node', {'id': id})
        for record in result:
            return explore(record['node'], 10)


def list(title):
    with driver.session() as session:
        result = session.run("MATCH (p:Paper) WHERE p.title CONTAINS {title} RETURN p", {"title": title})
        nodes = []
        for item in result:
            node = item['p']
            nodes.append(dict(node.items()))
        return nodes
