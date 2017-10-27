# Author: Jaswanth
from common.database import Database

class ListSkill(object):

    def __init__(self):
        key = ""
        collection = ""
        skills = []

    @staticmethod
    def list_skills():
        skills = Database.list_values(collection='skillset', key='skill')
        return skills