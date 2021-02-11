from businessException import BusinessException
from datetime import datetime, timedelta

class dateUtil:

    def make_date_dict(startTime, stopTime):
        start = startTime.split(";")
        end = stopTime.split(";")
        yyyy_s = int(start[0][0:4])
        MM_s = int(start[0][4:6])
        dd_s = int(start[0][6:8])
        hh_s = int(start[1][0:2])
        mm_s = int(start[1][2:4])
        yyyy_e = int(end[0][0:4])
        MM_e = int(end[0][4:6])
        dd_e = int(end[0][6:8])
        hh_e = int(end[1][0:2])
        mm_e = int(end[1][2:4])
        startDate = datetime(yyyy_s,MM_s,dd_s,hh_s,mm_s,00)
        endDate = datetime(yyyy_e,MM_e,dd_e,hh_e,mm_e,00)

        
        date_dict_list = []

        checkFlg = True
        while(checkFlg):
            date_dict = {}
            tempDate = startDate + timedelta(days=2) - timedelta(minutes=1)
            if tempDate >= endDate :
                tempDate = endDate
                checkFlg = False

            start = startDate.strftime("%Y%m%d%H%M")
            stop = tempDate.strftime("%Y%m%d%H%M")
            startDate = tempDate + timedelta(minutes=1)

            date_dict["startDate"] = start[0:8]
            date_dict["startTime"] = start[8:16]
            date_dict["stopDate"] = stop[0:8]
            date_dict["stopTime"] = stop[8:16]

            date_dict_list.append(date_dict)

        return date_dict_list

    def validate(startTime, stopTime):
        # 日付が正しいか
        try:
            start = startTime.split(";")
            end = stopTime.split(";")
            yyyy_s = int(start[0][0:4])
            MM_s = int(start[0][4:6])
            dd_s = int(start[0][6:8])
            hh_s = int(start[1][0:2])
            mm_s = int(start[1][2:4])
            yyyy_e = int(end[0][0:4])
            MM_e = int(end[0][4:6])
            dd_e = int(end[0][6:8])
            hh_e = int(end[1][0:2])
            mm_e = int(end[1][2:4])
            startDate = datetime(yyyy_s,MM_s,dd_s,hh_s,mm_s,00)
            endDate = datetime(yyyy_e,MM_e,dd_e,hh_e,mm_e,00)
            if startDate >= endDate:
                raise BusinessException("開始日付>=終了日付となっています")
                pass
        except (ValueError, IndexError):
            raise BusinessException("フォーマットが違います")
            pass



        



