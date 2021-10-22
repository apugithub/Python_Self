import docker

client = docker.from_env()


def show_all_images():
    for i in client.images.list():
        print(i)


def delete_all_stopped_containers():
    client.containers.prune(filters=None)


def get_all_container_list():
    containers = client.containers.list()
    for i in containers:
        print(i.name, i)

# delete_all_stopped_containers()
