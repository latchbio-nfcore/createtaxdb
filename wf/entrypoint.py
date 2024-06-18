from dataclasses import dataclass
from enum import Enum
import os
import subprocess
import requests
import shutil
from pathlib import Path
import typing
import typing_extensions

from latch.resources.workflow import workflow
from latch.resources.tasks import nextflow_runtime_task, custom_task
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir
from latch.ldata.path import LPath
from latch_cli.nextflow.workflow import get_flag
from latch_cli.nextflow.utils import _get_execution_name
from latch_cli.utils import urljoins
from latch.types import metadata
from flytekit.core.annotation import FlyteAnnotation

from latch_cli.services.register.utils import import_module_by_path

meta = Path("latch_metadata") / "__init__.py"
import_module_by_path(meta)
import latch_metadata

@custom_task(cpu=0.25, memory=0.5, storage_gib=1)
def initialize() -> str:
    token = os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")
    if token is None:
        raise RuntimeError("failed to get execution token")

    headers = {"Authorization": f"Latch-Execution-Token {token}"}

    print("Provisioning shared storage volume... ", end="")
    resp = requests.post(
        "http://nf-dispatcher-service.flyte.svc.cluster.local/provision-storage",
        headers=headers,
        json={
            "storage_gib": 100,
        }
    )
    resp.raise_for_status()
    print("Done.")

    return resp.json()["name"]






@nextflow_runtime_task(cpu=4, memory=8, storage_gib=100)
def nextflow_runtime(pvc_name: str, input: LatchFile, outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], dbname: str, accession2taxid: typing.Optional[LatchFile], prot2taxid: typing.Optional[str], nucl2taxid: typing.Optional[LatchFile], nodesdmp: typing.Optional[LatchFile], namesdmp: typing.Optional[LatchFile], malt_mapdb: typing.Optional[LatchFile], save_concatenated_fastas: typing.Optional[bool], build_bracken: typing.Optional[bool], build_centrifuge: typing.Optional[bool], build_diamond: typing.Optional[bool], build_kaiju: typing.Optional[bool], build_malt: typing.Optional[bool], build_kraken2: typing.Optional[bool], kraken2_keepintermediate: typing.Optional[bool], build_krakenuniq: typing.Optional[bool], multiqc_methods_description: typing.Optional[str], malt_sequencetype: typing.Optional[str]) -> None:
    try:
        shared_dir = Path("/nf-workdir")



        ignore_list = [
            "latch",
            ".latch",
            "nextflow",
            ".nextflow",
            "work",
            "results",
            "miniconda",
            "anaconda3",
            "mambaforge",
        ]

        shutil.copytree(
            Path("/root"),
            shared_dir,
            ignore=lambda src, names: ignore_list,
            ignore_dangling_symlinks=True,
            dirs_exist_ok=True,
        )

        cmd = [
            "/root/nextflow",
            "run",
            str(shared_dir / "main.nf"),
            "-work-dir",
            str(shared_dir),
            "-profile",
            "docker",
            "-c",
            "latch.config",
                *get_flag('input', input),
                *get_flag('outdir', outdir),
                *get_flag('email', email),
                *get_flag('multiqc_title', multiqc_title),
                *get_flag('dbname', dbname),
                *get_flag('accession2taxid', accession2taxid),
                *get_flag('prot2taxid', prot2taxid),
                *get_flag('nucl2taxid', nucl2taxid),
                *get_flag('nodesdmp', nodesdmp),
                *get_flag('namesdmp', namesdmp),
                *get_flag('malt_mapdb', malt_mapdb),
                *get_flag('save_concatenated_fastas', save_concatenated_fastas),
                *get_flag('build_bracken', build_bracken),
                *get_flag('build_centrifuge', build_centrifuge),
                *get_flag('build_diamond', build_diamond),
                *get_flag('build_kaiju', build_kaiju),
                *get_flag('build_malt', build_malt),
                *get_flag('malt_sequencetype', malt_sequencetype),
                *get_flag('build_kraken2', build_kraken2),
                *get_flag('kraken2_keepintermediate', kraken2_keepintermediate),
                *get_flag('build_krakenuniq', build_krakenuniq),
                *get_flag('multiqc_methods_description', multiqc_methods_description)
        ]

        print("Launching Nextflow Runtime")
        print(' '.join(cmd))
        print(flush=True)

        env = {
            **os.environ,
            "NXF_HOME": "/root/.nextflow",
            "NXF_OPTS": "-Xms2048M -Xmx8G -XX:ActiveProcessorCount=4",
            "K8S_STORAGE_CLAIM_NAME": pvc_name,
            "NXF_DISABLE_CHECK_LATEST": "true",
        }
        subprocess.run(
            cmd,
            env=env,
            check=True,
            cwd=str(shared_dir),
        )
    finally:
        print()

        nextflow_log = shared_dir / ".nextflow.log"
        if nextflow_log.exists():
            name = _get_execution_name()
            if name is None:
                print("Skipping logs upload, failed to get execution name")
            else:
                remote = LPath(urljoins("latch:///your_log_dir/nf_nf_core_createtaxdb", name, "nextflow.log"))
                print(f"Uploading .nextflow.log to {remote.path}")
                remote.upload_from(nextflow_log)



@workflow(metadata._nextflow_metadata)
def nf_nf_core_createtaxdb(input: LatchFile, outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})], email: typing.Optional[str], multiqc_title: typing.Optional[str], dbname: str, accession2taxid: typing.Optional[LatchFile], prot2taxid: typing.Optional[str], nucl2taxid: typing.Optional[LatchFile], nodesdmp: typing.Optional[LatchFile], namesdmp: typing.Optional[LatchFile], malt_mapdb: typing.Optional[LatchFile], save_concatenated_fastas: typing.Optional[bool], build_bracken: typing.Optional[bool], build_centrifuge: typing.Optional[bool], build_diamond: typing.Optional[bool], build_kaiju: typing.Optional[bool], build_malt: typing.Optional[bool], build_kraken2: typing.Optional[bool], kraken2_keepintermediate: typing.Optional[bool], build_krakenuniq: typing.Optional[bool], multiqc_methods_description: typing.Optional[str], malt_sequencetype: typing.Optional[str] = 'DNA') -> None:
    """
    nf-core/createtaxdb

    Sample Description
    """

    pvc_name: str = initialize()
    nextflow_runtime(pvc_name=pvc_name, input=input, outdir=outdir, email=email, multiqc_title=multiqc_title, dbname=dbname, accession2taxid=accession2taxid, prot2taxid=prot2taxid, nucl2taxid=nucl2taxid, nodesdmp=nodesdmp, namesdmp=namesdmp, malt_mapdb=malt_mapdb, save_concatenated_fastas=save_concatenated_fastas, build_bracken=build_bracken, build_centrifuge=build_centrifuge, build_diamond=build_diamond, build_kaiju=build_kaiju, build_malt=build_malt, malt_sequencetype=malt_sequencetype, build_kraken2=build_kraken2, kraken2_keepintermediate=kraken2_keepintermediate, build_krakenuniq=build_krakenuniq, multiqc_methods_description=multiqc_methods_description)

