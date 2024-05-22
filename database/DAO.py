from database.DB_connect import DBConnect
from model.Prodotto import Prodotto


class DAO():

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT product_color 
                   FROM go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row["product_color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProdotti(c):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select  *
                   from go_products 
                    where Product_color = %s """

        cursor.execute(query, (c,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(p1, p2, anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select count(distinct gds2.Date) as PESO
                    from go_daily_sales gds, go_daily_sales gds2 
                    where gds.Retailer_code = gds2.Retailer_code and year(gds.Date) = %s and gds.Date=gds2.Date
                    and gds.Product_number= %s and gds2.Product_number = %s """

        cursor.execute(query, (anno, p1.Product_number, p2.Product_number,))

        for row in cursor:
            result = row["PESO"]    #mi restituisce solo un peso

        cursor.close()
        conn.close()
        return result








