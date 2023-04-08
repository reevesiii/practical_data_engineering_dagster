from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="pde_dagster",
        packages=find_packages(exclude=["pde_dagster_tests"]),
        install_requires=[
            "dagster",
        ],
    )
