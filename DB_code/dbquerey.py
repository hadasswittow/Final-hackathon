from pymongo import MongoClient
import pymongo

client = MongoClient()

db = client.get_database("hackaton")
report = db.get_collection("reports")
re_id = 1

# report_info = [
#     {
#         'report_id': 1,
#         'license_number': '1233456',
#         'date': '11.12.13',
#         'time': '10:50',
#         'image': 'link',
#         'area': '90',
#     },
#     {
#         'report_id': 2,
#         'license_number': '234556',
#         'date': '12.12.13',
#         'time': '10:50',
#         'image': 'link',
#         'area': '90',
#     },
#     {
#         'report_id': 3,
#         'license_number': '564478',
#         'date': '11.12.13',
#         'time': '10:50',
#         'image': 'link',
#         'area': '90',
#     },
# ]
# report.insert_many(report_info)

report_list = db.get_collection("reports")


def get_all_reports():
    return report_list.find({})


def get_report_img(report_id):
    return report_list.find({'report_id': report_id})[0]['image']


def get_report(report_id):
    return report_list.find({'report_id': report_id})


def get_report_by_time(atime):
    return report_list.find({'time': atime})


def get_report_by_date(adate):
    return report_list.find({'date': adate})


def get_report_by_license(number):
    return report_list.find({'license_number': number})


def get_report_by_area(area):
    return report_list.find({'area': area})


def add_report(license, date, time, image, area):
    global re_id
    re_id += 1
    report_info = {
        'report_id': re_id,
        'license_number': license,
        'date': date,
        'time': time,
        'image': image,
        'area': area,
    }
    report.insert_one(report_info)


def delete_report(report_id):
    try:
        to_delete = {"report_id": report_id}
        report.delete_one(to_delete)
    except:
        return -1
