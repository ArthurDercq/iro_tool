import sqlite3
import pandas as pd

# Connexion à la base de données (créée si elle n'existe pas)

def connect_to_db():
    conn = sqlite3.connect('data/iro_v1')
    cursor = conn.cursor()

    return conn, cursor

def get_topic_name():
    conn, cursor = connect_to_db()
    query_topic_name= """SELECT topic_name FROM topics;"""
    cursor.execute(query_topic_name)
    topics = cursor.fetchall()
    topics = [topic[0] for topic in topics]
    return topics


def get_topicID(topic_name):
    conn, cursor = connect_to_db()
    query_topic_name= """SELECT topic_id FROM topics WHERE topic_name = ?"""
    cursor.execute(query_topic_name, (topic_name,))
    id = cursor.fetchall()
    id = [topic[0] for topic in id]
    return id[0]


def get_sector():
    conn, cursor = connect_to_db()
    query_sector_name= """SELECT company_sector FROM companies;"""
    cursor.execute(query_sector_name)
    sectors = cursor.fetchall()
    sectors = [sector[0] for sector in sectors]
    return sectors

# def get_impact(topic_selector):
#     conn, cursor = connect_to_db()
#     query_Impact_from_topics="""SELECT impacts.impact_name, companies.company_sector
#                 FROM impacts
#                 JOIN companies ON impacts.company_id = companies.company_id
#                 WHERE impacts.topic_id = ?"""
#     cursor.execute(query_Impact_from_topics, (topic_selector,))
#     impacts = cursor.fetchall()
#     impacts = [impact[0] for impact in impacts]
#     if len(impacts) == 0:
#         print("No impacts found")
#     else:
#         return impacts

def get_impact(topic_selector):
    conn, cursor = connect_to_db()
    query_Impact_from_topics="""SELECT impacts.impact_name, companies.company_name
            FROM impacts
            JOIN companies ON impacts.company_id = companies.company_id
            WHERE impacts.topic_id = ?
            """
    cursor.execute(query_Impact_from_topics, (topic_selector,))
    impacts = cursor.fetchall()
    if len(impacts) == 0:
        print("No impacts found")
    else:
        return impacts


def get_risk(topic_selector):
    conn, cursor = connect_to_db()
    query_risk_name= """SELECT risks.risk_name, companies.company_name
                    FROM risks
                    JOIN companies ON risks.company_id = companies.company_id
                    WHERE risks.topic_id = ?
                    """
    cursor.execute(query_risk_name, (topic_selector,))
    risks = cursor.fetchall()
    if len(risks) == 0:
        print("No risks found")
    else:
        return risks


def get_opportunity(topic_selector):
    conn, cursor = connect_to_db()
    query_opportunity_name= """SELECT opportunities.opportunity_name, companies.company_name
                            FROM opportunities
                            JOIN companies ON Opportunities.company_id = companies.company_id
                            WHERE opportunities.topic_id = ?
                            """;
    cursor.execute(query_opportunity_name,  (topic_selector,))
    opportunities = cursor.fetchall()
    if len(opportunities) == 0:
        print("No opportunities found")
    else:
        return opportunities
