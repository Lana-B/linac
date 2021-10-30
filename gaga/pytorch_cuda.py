import torch

if not torch.cuda.is_available():
    print("GPU Not Available")
    exit(-1)

print("=" * 30)
print("HOUSE KEEPING")
print("=" * 30)

print("CUDA Available: ", torch.cuda.is_available())
print("CUDA Initialised: ", torch.cuda.is_initialized())
print("CUDA Architecture Lists: ", torch.cuda.get_arch_list())

device = torch.device("cuda")
n_devices = torch.cuda.device_count()
current_device_id = torch.cuda.current_device()
print("Torch Devices Count: ", n_devices)
print("Index Current device: ", current_device_id)

if n_devices > 1:
    devices_id = set(range(n_devices))
else:
    devices_id = [0]

print("=" * 30)
print("DEVICE(s) INFORMATION")
print("=" * 30)

for did in devices_id:
    print(f"Device {did}")
    cuda_dev = torch.device(f"cuda:{did}")
    print("\t", torch.cuda.get_device_capability(cuda_dev))

for did in devices_id:
    print(f"Device {did}")
    print("\tTotal Memory: ", torch.cuda.get_device_properties(did).total_memory)
    print("\tMemory Reserved: ", torch.cuda.memory_reserved(did))
    print("\tMemory Allocated: ", torch.cuda.memory_allocated(did))
    print("\tMAX Memory Allocated: ", torch.cuda.max_memory_allocated(did))
    print("\tMemory Summary: \n\t", torch.cuda.memory_summary(did))


if n_devices > 1:
    print("=" * 30)
    print("DEVICE(s) COMMUNICATION")
    print("=" * 30)

    print("Can default device acess Peers ?")

    peers = devices_id.difference({current_device_id})
    for did in peers:
        peer = torch.device(f"cuda:{did}")
        print(
            f"Access COMM: [{current_device_id} - {did}]",
            torch.cuda.can_device_access_peer(device, peer),
        )

