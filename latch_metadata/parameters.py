
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
    'mode': NextflowParameter(
        type=typing.Optional[str],
        default='rd',
        section_title='Main options',
        description="The pipeline mode to use, either 'rd' for R&D or 'ht' for High-Throughput",
    ),
    'duplex_seq': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Enable when the input is duplex sequenecing.',
    ),
    'groupreadsbyumi_strategy': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Read grouping options',
        description='Grouping strategy',
    ),
    'groupreadsbyumi_edits': NextflowParameter(
        type=typing.Optional[int],
        default=None,
        section_title=None,
        description='Maximum number of edits',
    ),
    'call_min_reads': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Consensus reads options',
        description='Minimum reads to call a consensus',
    ),
    'call_min_baseq': NextflowParameter(
        type=typing.Optional[int],
        default=None,
        section_title=None,
        description='Minimum input base quality',
    ),
    'filter_min_reads': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Consensus filtering options',
        description='Minimum reads to keep a consensus',
    ),
    'filter_min_baseq': NextflowParameter(
        type=typing.Optional[int],
        default=None,
        section_title=None,
        description='Minimum consensus base quality',
    ),
    'filter_max_base_error_rate': NextflowParameter(
        type=typing.Optional[float],
        default=None,
        section_title=None,
        description='The maximum error rate for a single consensus base',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA genome file.',
    ),
    'fasta_fai': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to FASTA reference index.',
    ),
    'save_reference': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If generated by the pipeline save the STAR index in the results directory.',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

