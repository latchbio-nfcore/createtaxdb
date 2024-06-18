
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'dbname': NextflowParameter(
        type=str,
        default=None,
        section_title=None,
        description='Specify name that resulting databases will be prefixed with.',
    ),
    'accession2taxid': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='NCBI-style four-column accession to taxonomy ID map file',
    ),
    'prot2taxid': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Two column protein sequence accession ID to taxonomy map file.',
    ),
    'nucl2taxid': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Two column nucleotide sequence accession ID to taxonomy map file.',
    ),
    'nodesdmp': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to NCBI-style taxonomy node dmp file.',
    ),
    'namesdmp': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to NCBI-style taxonomy names dmp file.',
    ),
    'malt_mapdb': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to MEGAN6/MALT mapping db file',
    ),
    'save_concatenated_fastas': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Save concatenated input FASTAs',
    ),
    'build_bracken': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='Database Building Options',
        description='Turn on extending of Kraken2 database to include Bracken files. Requires nucleotide FASTA File input.',
    ),
    'build_centrifuge': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of Centrifuge database. Requires nucleotide FASTA file input.',
    ),
    'build_diamond': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of DIAMOND database. Requires amino-acid FASTA file input.',
    ),
    'build_kaiju': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of Kaiju database. Requires amino-acid FASTA file input.',
    ),
    'build_malt': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of MALT database. Requires nucleotide FASTA file input.',
    ),
    'malt_sequencetype': NextflowParameter(
        type=typing.Optional[str],
        default='DNA',
        section_title=None,
        description='Specify type of input sequence being given to MALT',
    ),
    'build_kraken2': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of Kraken2 database. Requires nucleotide FASTA file input.',
    ),
    'kraken2_keepintermediate': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Retain intermediate Kraken2 build files for inspection.',
    ),
    'build_krakenuniq': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Turn on building of KrakenUniq database. Requires nucleotide FASTA file input.',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

