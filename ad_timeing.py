import time
import mysql.connector


class AdTiming:

    def __init__(self):
        pass

    # Create a date and time expression in 'yyyy-mm-dd hh:mm:ss' format for the
    # current moment.
    def time_format(self):

        my_time = time.localtime(time.time())
        t_formatted = str(my_time.tm_year)\
                      + '-'+str(my_time.tm_mon).rjust(2, '0')\
                      + '-'+str(my_time.tm_mday).rjust(2, '0')\
                      + ' '+str(my_time.tm_hour).rjust(2, '0')+':'+str(my_time.tm_min).rjust(2, '0')\
                      + ':'+str(my_time.tm_sec).rjust(2, '0')
        return t_formatted


# Every 10 minutes check if there are new ads for the current hour.
class MysqlQuery:

    def __init__(self, table_name, time_now):
        self.table_name = table_name
        self.time_now = time_now

    # Cut the date-time expression so it encompasses the date and the hour.
    # Create SQL query that gets all the ad listings for the current hour.
    def query_match(self):
        print(self.time_now)
        self.time_now = self.time_now[0:13]
        print(self.time_now)

        query = '''
        SELECT id, start_time, ad_path FROM %s
        WHERE SUBSTRING(start_time, 1, 13) = \'%s\'; 
        ''' % (self.table_name, self.time_now)

        print('Query:', query)

        # Connecting to the database.
        connection = mysql.connector.connect(user='root', password='dance',
                                             host='localhost')

        # Create a cursor to operate in the database server.
        cursor = connection.cursor()
        cursor.execute(query)
        get_results = cursor.fetchall()
        print('MySQL results:', get_results)

        # If there are paid ad listings return the picture paths of these listings.
        if len(get_results) > 0:
            results = [result[2] for result in get_results]
            print('Ad timing results:', results)
            return results
        else:
            print('No results.')
            return []


# Call all the functions to get the paid paths for the current hour.
def paid_ad_paths(table_name):
    timing = AdTiming()
    f_time = timing.time_format()
    print('Formatted time:', f_time)
    query = MysqlQuery(table_name, f_time)
    path = query.query_match()
    return path
