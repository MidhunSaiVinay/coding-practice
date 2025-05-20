class SnapshotArray:
    def __init__(self, length: int):
        # Initialize array with length and snap_id
        self.array = [{0: 0} for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # Set value at current snap_id
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        # Increment snap_id and return previous snap_id
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Get the value at the given snap_id
        history = self.array[index]
        # Find the most recent snapshot that exists
        while snap_id not in history and snap_id > 0:
            snap_id -= 1
        return history.get(snap_id, 0)