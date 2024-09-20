from Model.DatabaseConnectivity import global_cursor, connection


class Itemlists:
    @classmethod
    def vegitems(cls):
        query = "Select * from veg_details;"
        global_cursor.execute(query)
        result = global_cursor.fetchall()
        print(result)
        return result

    @classmethod
    def groceryitems(cls):
        query = "Select * from grocery_details;"
        global_cursor.execute(query)
        result = global_cursor.fetchall()
        print(result)
        return result

    @classmethod
    def fruititems(cls):
        query = "Select * from fruit_details;"
        global_cursor.execute(query)
        result = global_cursor.fetchall()
        print(result)
        return result

    @classmethod
    def userselection(cls):
        choice = int(input("Enter Your Choice:\n"))
        choice = choice - 1
        return choice