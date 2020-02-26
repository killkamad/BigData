import psycopg2
import seaborn as sns

def aws():
    try:
        connection = psycopg2.connect(user='postgres',
                                      password='postgres',
                                      host='dbtest-1.cmwfjvlei66t.eu-central-1.rds.amazonaws.com',
                                      port='5432',
                                      database='postgres')
        cursor = connection.cursor()
        query = "Select * from exchanges"
        res = cursor.execute(query)
        res.cursor.execute(query)
        print('connected')
    except(Exception, psycopg2.Error) as error:
        print(error)


if __name__ == '__main__':
    aws()
iris = sns.load_dataset()