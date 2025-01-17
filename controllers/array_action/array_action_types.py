from dataclasses import dataclass, field

from controllers.common.node_info import Initiators


@dataclass
class Volume:
    capacity_bytes: int
    id: str
    internal_id: str
    name: str
    array_address: str
    source_id: str
    array_type: str
    pool: str
    space_efficiency_aliases: set = field(default_factory=set)
    volume_group_id: str = None


@dataclass
class Snapshot(Volume):
    pool: str = None
    is_ready: bool = False


@dataclass
class Replication:
    name: str
    copy_type: str
    is_ready: bool
    replication_type: str
    is_primary: bool
    volume_group_id: str = None


@dataclass
class ReplicationRequest:
    volume_internal_id: str
    other_volume_internal_id: str
    other_system_id: str
    copy_type: str
    replication_type: str
    replication_policy: str = None


@dataclass
class Host:
    name: str
    connectivity_types: list = field(repr=False)
    nvme_nqns: list = field(default_factory=list, repr=False)
    fc_wwns: list = field(default_factory=list, repr=False)
    iscsi_iqns: list = field(default_factory=list, repr=False)
    initiators: Initiators = field(init=False)

    def __post_init__(self):
        self.initiators = Initiators(nvme_nqns=self.nvme_nqns, fc_wwns=self.fc_wwns, iscsi_iqns=self.iscsi_iqns)


@dataclass
class ObjectIds:
    internal_id: str = ''
    uid: str = ''

    def __bool__(self):
        return bool(self.internal_id or self.uid)
