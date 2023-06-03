using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.Scripting.Python;

public class ScriptRunner : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //Debug.Log($"This is at: {Application.dataPath}/Scripts/Python/test.py");
        PythonRunner.RunFile($"{Application.dataPath}/Scripts/Python/test.py");
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
