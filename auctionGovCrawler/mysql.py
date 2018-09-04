#coding=utf-8
import MySQLdb
import time
from __builtin__ import str
from _ast import Str

class Mysql:
    # 数据库初始化
    def __init__(self):
        try:
            self.db = MySQLdb.connect('101.132.145.84', 'tlpp_kaifa', 'tlpp_kaifa', 'tonglunzq')
            self.cur = self.db.cursor()
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "连接数据库错误，原因%d: %s" % (e.args[0], e.args[1])
    def insertData(self,jsonDatas):
        try:
            self.db.set_character_set('utf8')
            sqlCheck = 'select count(*) from gov_auction_info where auction_id =' +str(jsonDatas['auctionId'])
            print sqlCheck
            self.cur.execute(sqlCheck) 
            if self.cur._rows[0][0] == 0:
                insertInfo = "insert into %s (%s) VALUES (%s)" % ('gov_auction_info', "auction_id,start_price,access_rice,cash_price,date_time,paimai_time,court,user,phone,url,title",str(jsonDatas['auctionId'])+",'"+str(jsonDatas['startPrice'])+
                                                                  "','"+ str(jsonDatas['accessPrice'])+"','"+ str(jsonDatas['cashPrice'])+
                                                                  "','"+str(jsonDatas['date'])+"','"+str(jsonDatas['paimaiStatus'])+
                                                                  "','"+str(jsonDatas['court'])+
                                                                  "','"+str(jsonDatas['user'])+
                                                                  "','"+str(jsonDatas['phone'])+
                                                                  "','"+str(jsonDatas['url'])+"','"+str(jsonDatas['title'])+"'")
                print insertInfo
                try:
                    result = self.cur.execute(insertInfo)
                    insert_id = self.db.insert_id()
                    self.db.commit()
                    # 判断是否执行成功
                    if result:
                        return insert_id
                    else:
                        return 0
                except MySQLdb.Error, e:
                    # 发生错误时回滚
                    self.db.rollback()
                    # 主键唯一，无法插入
                    if "key 'PRIMARY'" in e.args[1]:
                        print self.getCurrentTime(), "数据已存在，未插入数据"
                    else:
                        print self.getCurrentTime(), "插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
                        exit()
            else:
                updateInfo = 'update gov_auction_info set ' + 'title="' + str(jsonDatas['title']) + '",start_price="'+str(jsonDatas['startPrice'])+'",access_rice="'+ jsonDatas['accessPrice'] + '",cash_price="'+str(jsonDatas['cashPrice'])+'",date_time="'+ str(jsonDatas['date'])+'",paimai_time="'+str(jsonDatas['paimaiStatus'])+'",court="'+str(jsonDatas['court'])+'",user="'+str(jsonDatas['user'])+'",phone="'+str(jsonDatas['phone'])+'",url="'+str(jsonDatas['url'])+'" where auction_id='+str(jsonDatas['auctionId'])
                print updateInfo
                result = self.cur.execute(updateInfo)
                insert_id = self.db.insert_id()
                self.db.commit()
                # 判断是否执行成功
                if result:
                    return insert_id
                else:
                    return 0
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "数据库错误，原因%d: %s" % (e.args[0], e.args[1])
            exit()
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "数据库错误，原因%d: %s" % (e.args[0], e.args[1])
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
    def getIP(self):
        try:
            self.db.set_character_set('utf8')
            sqlGetData = "SELECT ip_port FROM ip_port"
            self.cur.execute(sqlGetData)
            return list(self.cur._rows)
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "数据库错误，原因%d: %s" % (e.args[0], e.args[1])
if __name__ == '__main__':
    mysql = Mysql()
    
    
    
    
    