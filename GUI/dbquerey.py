from bson import ObjectId
from pymongo import MongoClient
import pymongo

client = MongoClient()

db = client.get_database("hackathon")
report = db.get_collection("reports")
re_id = 1

report_list = db.get_collection("reports")


def get_all_reports():
    return report_list.find({})


def get_appealed_reports():
    return report_list.find({'status': "appealed"})  # to change to appealed


def get_non_sent_reports():
    return report_list.find({'status': "not_sent"})  # to change to appealed


def get_report_img(report_id):
    return report_list.find({'report_id': report_id})[0]['image']


def get_report(report_id):
    return report_list.find({"_id": ObjectId(report_id)})  # {'_id': report_id})


def get_report_by_time(atime):
    return report_list.find({'time': atime})


def get_report_by_date(adate):
    return report_list.find({'date': adate})


def get_report_by_license(number):
    return report_list.find({'license_number': number})


def get_report_by_area(area):
    return report_list.find({'area': area})


def get_report_by_status(status):
    return report_list.find({'status': status})  # could be appealed, non-appealed, not-sent, denied


def set_status_to_sent():
    myquery = {"status": "not_sent"}
    newvalues = {"$set": {"status": "sent"}}

    report_list.update_many(myquery, newvalues)


def set_status_to_appealed():
    myquery = {"status": "sent"}
    newvalues = {"$set": {"status": "appealed"}}

    report_list.update_many(myquery, newvalues)


def set_status_to_non_appealed():
    myquery = {"status": "sent"}
    newvalues = {"$set": {"status": "non_appealed"}}


def add_report(license, date, time, image, area, status):
    # global re_id
    # re_id += 1
    report_info = {
        # 'report_id': re_id,
        'license_number': license,
        'date': date,
        'time': time,
        'image': image,
        'area': area,
        'status': status
    }
    report.insert_one(report_info)


def delete_report(report_id):
    try:
        to_delete = {"report_id": report_id}
        report.delete_one(to_delete)
    except:
        return -1
