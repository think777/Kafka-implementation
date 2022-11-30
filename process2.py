def create_partition(self, table_path, partition_spec, partition, ignore_if_exists):
        """
        Create a partition.

        :param table_path: Path :class:`ObjectPath` of the table.
        :param partition_spec: Partition spec :class:`CatalogPartitionSpec` of the partition.
        :param partition: The partition :class:`CatalogPartition` to add.
        :param ignore_if_exists: Flag to specify behavior if a table with the given name already
                                 exists:
                                 if set to false, it throws a TableAlreadyExistException,
                                 if set to true, nothing happens.
        :raise: CatalogException in case of any runtime exception.
                TableNotExistException thrown if the target table does not exist.
                TableNotPartitionedException thrown if the target table is not partitioned.
                PartitionSpecInvalidException thrown if the given partition spec is invalid.
                PartitionAlreadyExistsException thrown if the target partition already exists.
        """
        self._j_catalog.createPartition(table_path._j_object_path,
                                        partition_spec._j_catalog_partition_spec,
                                        partition._j_catalog_partition,
                                        ignore_if_exists)