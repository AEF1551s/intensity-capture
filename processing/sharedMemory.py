# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# sharedMemory.py
import mmap
import os

FRAME_SIZE = 829440  # 1440x576 bytes

def openSharedMemory():
    shmName = "shared_frame_1"
    shmFd = os.open(f"/dev/shm/{shmName}",os.O_RDWR)
    if shmFd < 0:
        raise OSError("Failed to create shared memory")

    # Resize
    os.ftruncate(shmFd, FRAME_SIZE)

    # Map shared memory object
    mapObj = mmap.mmap(shmFd, FRAME_SIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

    if mapObj == -1:
        os.close(shmFd)
        raise OSError("Failed to map shared memory block")

    return mapObj
