using UnityEngine;
using UnityEngine.AI;
public class MoveAgent : MonoBehaviour
{

    GameObject destination;
    NavMeshAgent agent;

    // Start is called before the first frame update
    void Start()
    {
        destination = GameObject.FindGameObjectWithTag("DroneTarget");
        agent = GetComponent<NavMeshAgent>();
        Vector3 position = destination.transform.position;
        Debug.Log(position);
        agent.SetDestination(destination.transform.position);
    }
}
