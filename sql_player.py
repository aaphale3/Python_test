#This program connects to SQL Server using ODBC, extracts the data, executes a complex query, and prints the data to a console.


import pyodbc

try:
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-51OBS5K\SQLEXPRESS01;"
                          "Database=Sport;"
                          "Trusted_Connection=yes;")

    #result_list = []
    cursor = cnxn.cursor()
    cursor.execute('SELECT Player.First_Name, Player.Last_Name, Stat.[3P_pct], Stat.FT_pct, Stat.PPG, Stat.RPG, Stat.APG, Stat.MPG,\
    Stat.Serum_Glucose, Stat.Blood_Type, Stat.MCV, Stat.Creatinine, Stat.Creatine_kinase, Stat.Carb_intake,\
    Stat.Protein_intake FROM Player INNER JOIN Stat ON Player.Player_ID = Stat.Player_ID')

    for row in cursor:
    #    result_list.append(row)
        print('row = %r' % (row,))
    #print(row[0] + " " + row[1])

except KeyboardInterrupt: #if operation is canceled (Ctrl - C or clear)
    print("You canceled the operation.")
except:
    print("Unexpected error occurred. Please contact administrator.")
#print(result_list)
