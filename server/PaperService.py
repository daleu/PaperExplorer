#!/usr/bin/env python3
import DatabaseService

neo4j = DatabaseService


def get_paper(title):
    nodes = neo4j.get_by_title(title)
    return nodes


def list(title):
    return neo4j.list_by_title(title)
