## Running a stateful container with file system configurations

1. Follow the instructions for running a stateful container, as detailed in [Sample configurations for running a stateful container](../content/using/csi_ug_using_sample.md).
2. Check the newly created pod.

    Display the newly created pod (make sure the pod status is _Running_).

    <pre>
    $> kubectl get pod demo-statefulset-file-system-0
    NAME                 READY   STATUS    RESTARTS   AGE
    demo-statefulset-file-system-0   1/1     Running   0          43s
3. Write data to the persistent volume of the pod.

    The PV should be mounted inside the pod at `/data`.

    <pre>
    $> kubectl exec demo-statefulset-file-system-0 -- touch /data/FILE
    $> kubectl exec demo-statefulset-file-system-0 -- ls /data/FILE
    /data/FILE
4. Delete StatefulSet and then recreate, in order to validate data (`/data/FILE`) remains in the persistent volume.

    1. Delete the StatefulSet.

        <pre>
        $> kubectl delete statefulset/statefulset-name
        statefulset/statefulset-name deleted

    2. Wait until the pod is deleted. Once deleted, the `"statefulset-name" not found` is returned.

            $> kubectl get statefulset/statefulset-name
            Error from server (NotFound): statefulsets.apps <statefulset-name> not found

    3. Verify that the multipath was deleted and that the PV mountpoint no longer exists by establishing an SSH connection and logging into the worker node.
          
        <pre>
        $> ssh root@k8s-node1
            
        $>[k8s-node1] df | egrep pvc
        $>[k8s-node1] multipath -ll
        $>[k8s-node1] lsblk /dev/sdb /dev/sdc
        lsblk: /dev/sdb: not a block device
        lsblk: /dev/sdc: not a block device

    4. Recreate the StatefulSet and verify that `/data/FILE` exists.

        <pre>
        $> kubectl create -f demo-statefulset-file-system.yaml
        statefulset/statefulset-name created
            
        $> kubectl exec demo-statefulset-file-system-0 -- ls /data/FILE
        /data/FILE

5. Delete StatefulSet and the PVC.

        $> kubectl delete statefulset/statefulset-name
        statefulset/statefulset-name deleted
            
        $> kubectl get statefulset/statefulset-name
        Error from server (NotFound): statefulsets.apps <statefulset-name> not found.
            
        $> kubectl delete pvc/demo-pvc-file-system
        persistentvolumeclaim/demo-pvc-file-system deleted
            
        $> kubectl get pv,pvc
        No resources found.