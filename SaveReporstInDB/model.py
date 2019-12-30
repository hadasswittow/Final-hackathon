from pymongo import MongoClient

class DB:

    def __init__(self):
        client = MongoClient()
        self.db = client.get_database("hackathon")
        self.reports = self.db.get_collection("reports")


    def insert_report(self, li_num, _date, _time, img,area):
        report = {
            'license_number': li_num,
            'date': _date,
            'time': _time,
            'image': img,
            'area': area,
            'status': 'not sent'
        }

        self.reports.insert_one( report)