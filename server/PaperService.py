#!/usr/bin/env python3
import DatabaseService

neo4j = DatabaseService


def get_paper_by_title(title):
    nodes = neo4j.get_by_title(title)
    return nodes


def get_paper_by_id(id):
    nodes = neo4j.get_by_id(id)
    return nodes


def list(title):
    return neo4j.list(title)
