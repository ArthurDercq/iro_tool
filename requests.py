import sqlite3

# Connexion à la base de données (créée si elle n'existe pas)
conn = sqlite3.connect('data/iro.db')
cursor = conn.cursor()

def get_topic_name():
    query_topic_name= """SELECT Topic_name FROM Topic;"""
    cursor.execute(query_topic_name)
    topics = cursor.fetchall()
    topics = [topic[0] for topic in topics]
    return topics


def get_topicID(topic_name):
    query_topic_name= """SELECT Topic_id FROM Topic WHERE Topic_name = ?"""
    cursor.execute(query_topic_name, (topic_name,))
    id = cursor.fetchall()
    id = [topic[0] for topic in id]
    return id[0]


def get_sector():
    query_sector_name= """SELECT Company_sector FROM Companies;"""
    cursor.execute(query_sector_name)
    sectors = cursor.fetchall()
    sectors = [sector[0] for sector in sectors]
    return sectors

def get_impact(topic_selector):
    query_Impact_from_topics="""SELECT Impacts.Impact_name, Companies.Company_sector
                FROM Impacts
                JOIN Companies ON Impacts.Company_ID = Companies.Company_id
                WHERE Impacts.Topic_id = ?"""
    cursor.execute(query_Impact_from_topics, (topic_selector,))
    impacts = cursor.fetchall()
    impacts = [impact[0] for impact in impacts]
    if len(impacts) == 0:
        print("No impacts found")
    else:
        return impacts


def get_risk(topic_selector):
    query_risk_name= """SELECT Risks.Risk_name, Companies.Company_sector
                    FROM Risks
                    JOIN Companies ON Risks.Company_ID = Companies.Company_id
                    WHERE Risks.Topic_id = ?
                    """
    cursor.execute(query_risk_name, (topic_selector,))
    risks = cursor.fetchall()
    risks = [risk[0] for risk in risks]
    if len(risks) == 0:
        print("No risks found")
    else:
        return risks


def get_opportunity(topic_selector):
    query_opportunity_name= """SELECT Opportunities.Opportunity_name, Companies.Company_sector
                            FROM Opportunities
                            JOIN Companies ON Opportunities.Company_ID = Companies.Company_id
                            WHERE Opportunities.Topic_id = ?
                            """;
    cursor.execute(query_opportunity_name,  (topic_selector,))
    opportunities = cursor.fetchall()
    opportunities = [opportunity[0] for opportunity in opportunities]
    if len(opportunities) == 0:
        print("No opportunities found")
    else:
        return opportunities
