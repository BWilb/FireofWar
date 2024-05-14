import sys
import pypyodbc


def initial_upload_database(nations):
    """function will deal with the game's initial upload to database"""

    records = []
    # records variable will store information regarding nations

    for i in range(0, len(nations)):
        records.append(
            [nations[i].name,
             nations[i].leader,
             nations[i].population,
             nations[i].national_happiness,
             nations[i].national_stability,
             nations[i].yearly_births,
             nations[i].yearly_deaths,
             nations[i].national_gdp,
             nations[i].national_debt]
        )

    # connecting to database
    DRIVER = "SQL Server"
    SERVER_NAME = "BRYCEPC\MSSQLSERVER01"
    DATABASE_NAME = "IronAndBlood"

    connection = f"""Driver={{{DRIVER}}};
                            Server={SERVER_NAME};
                            Database={DATABASE_NAME};
                            Trust_Connection=yes;
            """
    try:
        conn = pypyodbc.connect(connection)
        print('connection is successful')
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()

    recreating_db = """
    
    if DB_ID("IronAndBlood) IS NULL
    CREATE DATABASE IronAndBlood
    
    USE IronAndBlood
    IF SCHEMA_ID('nations') IS NULL
        BEGIN
            EXEC("CREATE SCHEMA nations AUTHORIZATION dbo")
        END
    
    GO
    USE IronAndBlood
    
    GO
    IF SCHEMA_ID('nations') IS NULL
        BEGIN
            EXEC('CREATE SCHEMA nations AUTHORIZATION dbo')
        END
    GO

    USE IronAndBlood
    IF OBJECT_ID('nations.Nation', 'U') IS NOT NULL
        DROP TABLE nations.Nation
    
    CREATE TABLE nations.Nation
    (NationID int primary key IDENTITY(1, 1) NOT NULL,
    CurrentDate date NOT NULL,
    NationName varchar(35) NOT NULL,
    NationLeader VARCHAR(35) NOT NULL,
    NationPopulation int NOT NULL,
    NationalHappiness float NOT NULL,
    NationalStability float NOT NULL,
    BirthRate float NOT NULL,
    NationGDP float NOT NULL,
    NationalDebt float NOT NULL
    )
    """
    # script for recreating database every time game is played by user

    try:
        cursor.execute(recreating_db)
    except Exception as e:
        cursor.rollback()
        print(e.value)
        print("Failed to push to database")

    else:
        print("database successfully recreated")
        cursor.commit()
    finally:
        if conn.connected == 1:
            print("connection closed")
            # conn.close()

    # initial insertion of nation data

    insert_statement = """
        INSERT INTO nations.Nation
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
    try:

        # inserting data from AI nations and user nation
        for record in records:
            cursor.execute(insert_statement, record)

        pass
    except Exception as e:
        cursor.rollback()
        print(e.value)
        print("Failed to push to database")
    else:
        print("records inserted successfully")
        cursor.commit()
    finally:
        if conn.connected == 1:
            print("connection closed")
            # conn.close()