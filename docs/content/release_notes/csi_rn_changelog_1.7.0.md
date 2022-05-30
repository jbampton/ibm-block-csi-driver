# 1.7.0 (September 2021)

IBM® block storage CSI driver 1.7.0 adds new support and enhancements:
- Now supports the CSI Topology feature
- New volume replication (remote copy) support for IBM Spectrum Virtualize Family storage systems
- Additional support for Kubernetes 1.22

Version 1.7.0 also resolves the following issue:

|Ticket ID|Severity|Description|
|---------|--------|-----------|
|**CSI-702**|Service|Modifying the controller or node **affinity** settings may not take effect.|