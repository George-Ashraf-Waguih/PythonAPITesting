import configparser
import mysql.connector
from mysql.connector import Error



def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    return "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"


connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database']
}


def getConnection():
    try:
        connection = mysql.connector.connect(**connect_config)
        if connection.is_connected():
            print("Connection Successful")
            return connection
    except Error as e:
        print(e)


def getQuery(query):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    connection.close()
    return row
