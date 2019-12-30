import dbquerey
def try_all():
    all = dbquerey.get_all_reports()
    for i in all:
        print(i)

def try_get_report_img():
    print(dbquerey.get_report_img(1))

def try_get_report():
    r = dbquerey.get_report(2)
    for i in r:
        print(i)

def main():
    try_all()
    try_get_report_img()
    try_get_report()


main()