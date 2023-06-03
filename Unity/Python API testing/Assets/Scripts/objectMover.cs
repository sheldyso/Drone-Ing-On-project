using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class objectMover : MonoBehaviour
{
    public float angle;
    public float velocity;



    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        Vector3 currentPos = transform.position + transform.forward;
        Vector3 currentRot = transform.eulerAngles;
        Vector3 newPos = currentPos + new Vector3(velocity * Time.deltaTime, 0, 0);
        Vector3 newRot = currentRot + new Vector3(0, angle, 0);
        transform.position = newPos;
        transform.eulerAngles = newRot;
    }
}
