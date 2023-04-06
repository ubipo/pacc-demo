from flows import pipe
from prefect.deployments import Deployment
from prefect.filesystems import Azure

az_block = Azure.load("paje")

deploy = Deployment.build_from_flow(
    flow=pipe,
    name="Azure Example - paje",
    storage=az_block,
)


if __name__ == "__main__":
    deploy.apply()
