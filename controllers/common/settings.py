from controllers.common.config import config

NAME_PREFIX_SEPARATOR = "_"
ENDPOINTS_SEPARATOR = ", "

CSI_CONTROLLER_SERVER_WORKERS = 10

# array types
ARRAY_TYPE_XIV = 'A9000'
ARRAY_TYPE_SVC = 'SVC'
ARRAY_TYPE_DS8K = 'DS8K'
ALL_ARRAY_TYPES = [ARRAY_TYPE_XIV, ARRAY_TYPE_SVC, ARRAY_TYPE_DS8K]

PARAMETERS_NODE_ID_DELIMITER = config.parameters.node_id_info.delimiter
SPACE_EFFICIENCY_THIN = "thin"
SPACE_EFFICIENCY_COMPRESSED = "compressed"
SPACE_EFFICIENCY_DEDUPLICATED = "deduplicated"
SPACE_EFFICIENCY_DEDUPLICATED_THIN = "dedup_thin"
SPACE_EFFICIENCY_DEDUPLICATED_COMPRESSED = "dedup_compressed"
SPACE_EFFICIENCY_THICK = "thick"
SPACE_EFFICIENCY_NONE = "none"

HOST_DEFINITION_PLURAL = 'hostdefinitions'
CSI_IBM_GROUP = 'csi.ibm.com'
VERSION = 'v1'
HOST_DEFINITION_NODE_ID_FIELD = 'nodeId'
NAME_FIELD = 'name'
NAMESPACE_FIELD = 'namespace'
IO_GROUP_DELIMITER = ':'
IO_GROUP_LABEL_PREFIX = 'hostdefiner.block.csi.ibm.com/io-group-'
