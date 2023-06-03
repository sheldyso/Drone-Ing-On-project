using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
//using System.Data.SQLite;
using Unity.VisualScripting.Dependencies.Sqlite;
using UnityEditor.MemoryProfiler;

public class positionTracker : MonoBehaviour
{
    public bool trackX = true;
    public bool trackY = true;
    public bool trackZ = true;
    public string databasePath;
    //public string tableName;

    private float rollingTime = 0.0f;
    public float updatePeriodSeconds = 1.0f;

    private SQLiteConnection connection;

    static SQLiteConnection CreateConnection(string databasePath) {
        SQLiteConnection connection;
        //string filePath = Application.dataPath + "/Scripts/" + databaseName + ".db";
        //Debug.Log(filePath);
        connection = new SQLiteConnection(databasePath, true);
        try {
            // Test a query to the database to check connection
            connection.Execute("SELECT * FROM dronePos");

        }
        catch (Exception ex) {

        }
              
        return connection;
    }


    // Start is called before the first frame update
    void Start()
    {
        connection = CreateConnection(databasePath);
        
        // Flush the database on script start
        _ = connection.Execute("DELETE FROM dronePos");

        //Debug.Log(connection.Execute("SELECT * FROM dronePos"));
    }

    // Update is called once per frame
    void Update()
    {
        rollingTime += Time.deltaTime;
        if (rollingTime >= updatePeriodSeconds) {

            // Update position to database for every specified seconds.
            
            Vector3 currentPos = transform.position;
            _ = connection.Execute(string.Format("INSERT INTO dronePos (xPos, yPos, zPos) VALUES ({0}, {1}, {2})", currentPos.x, currentPos.y, currentPos.z));
            rollingTime = 0.0f;
        }
    }
}
