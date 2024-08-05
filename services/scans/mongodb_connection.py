import pymongo

host="mongodb://192.168.1.198:27017/"
class mongodb_connection:

    @staticmethod
    def querry(table_name,search_querry):
        myclient = pymongo.MongoClient(host)
        mydb = myclient["security_scans"]
        mycol = mydb[table_name]

        mydoc = mycol.find(search_querry)

        for x in mydoc:
            print(x)
        myclient.close()
        return mydoc

    @staticmethod
    def addData(table_name,data):
        myclient = pymongo.MongoClient(host)
        mydb = myclient["security_scans"]
        mycol = mydb[table_name]

        #data = { "name": "John", "address": "Highway 37" }
        print(data)
        x = mycol.insert_one(data)
        myclient.close()

    @staticmethod
    def getNucleiScansSortByDate():
        myclient = pymongo.MongoClient(host)
        mydb = myclient["security_scans"]
        mycol = mydb["nuclei_scans"]

        results = mycol.find().sort("scan_date", -1)
        print(results)
        for x in results:
            print(x)
        myclient.close()
        return results
    
    @staticmethod
    def getNmapScansSortByDate():
        myclient = pymongo.MongoClient(host)
        mydb = myclient["security_scans"]
        mycol = mydb["nmap_scans"]

        results = mycol.find().sort("scan_date", -1)
        print(results)
        for x in results:
            print(x)
        myclient.close()
        return results

if __name__ == "__main__":
    #mongodb_connection.querry(search_querry={},table_name="nuclei_scans")
    mongodb_connection.getNucleiScansSortByDate()