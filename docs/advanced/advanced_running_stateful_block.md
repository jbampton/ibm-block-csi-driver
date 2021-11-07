# Running a stateful container with raw block volume configurations

1. Follow the instructions for running a stateful container, as detailed in [Sample configurations for running a stateful container](../content/using/csi_ug_using_sample.md).
2. Check the newly created pod.

    Display the newly created pod (make sure the pod status is _Running_).
    <pre>
    $> kubectl get pod demo-statefulset-raw-block-0
    NAME                 READY   STATUS    RESTARTS   AGE
    demo-statefulset-raw-block-0   1/1     Running   0          43s  
3. Write data to the persistent volume of the pod.

    The PV should be mounted inside the pod at `/dev/block`.
    <pre>
    $> kubectl exec demo-statefulset-raw-block-0 -- bash -c "echo "test_block" | dd conv=unblock of=/dev/block"
    0+1 records in
    0+1 records out
    11 bytes copied, 9.3576e-05 s, 118 kB/s
        
    $> kubectl exec demo-statefulset-raw-block-0 -- bash -c "od -An -c -N 10 /dev/block"
    t e s t _ b l o c k
4. Delete StatefulSet and then recreate, in order to validate that the data (`test_block` in `/dev/block`) remains in the persistent volume.
    1. Delete the StatefulSet.
        <pre>
        $> kubectl delete statefulset/statefulset-name
        statefulset/statefulset-name deleted
    2. Wait until the pod is deleted. Once deleted, the `"statefulset-name" not found` is returned.
           
            $> kubectl get statefulset/statefulset-name
            Error from server (NotFound): statefulsets.apps <statefulset-name> not found
    3. Recreate the StatefulSet and verify that the content written to `/dev/block` exists.
        <pre>
        $> kubectl create -f demo-statefulset-raw-block.yaml
        statefulset/statefulset-name created
            
        $> kubectl exec demo-statefulset-raw-block-0 -- bash -c "od -An -c -N 10 /dev/block"
        t   e   s   t   _   b   l   o   c   k
5. Delete StatefulSet and the PVC.
    <pre>
    $> kubectl delete statefulset/statefulset-name
    statefulset/statefulset-name deleted
        
    $> kubectl get statefulset/statefulset-name
    Error from server (NotFound): statefulsets.apps "statefulset-name" not found
        
    $> kubectl delete pvc/demo-pvc-raw-block
    persistentvolumeclaim/demo-pvc-raw-block deleted
        
    $> kubectl get pv,pvc
    No resources found.