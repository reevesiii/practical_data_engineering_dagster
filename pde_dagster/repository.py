from dagster import load_assets_from_package_module, repository, define_asset_job

from pde_dagster import assets


@repository
def pde_dagster():
    return [
        load_assets_from_package_module(assets),
        define_asset_job(name="all_assets_job"),
    ]
