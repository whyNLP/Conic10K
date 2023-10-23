from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """
    dataset_path: str = field(
        metadata={
            "help": (
                "The path of the dataset"
            )
        }
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": (
                "For debugging purposes or quicker training, truncate the number of training examples to this "
                "value if set."
            )
        },
    )
    max_eval_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": (
                "For debugging purposes or quicker training, truncate the number of evaluation examples to this "
                "value if set."
            )
        },
    )
    block_size: Optional[int] = field(
        default=None,
        metadata={
            "help": (
                "Optional input sequence length after tokenization. "
                "The training dataset will be truncated in block of this size for training. "
                "Default to the model max input length for single sentence inputs (take into account special tokens)."
            )
        },
    )
    overwrite_cache: bool = field(
        default=True, metadata={"help": "Overwrite the cached training and evaluation sets"}
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    task: str = field(
        default="semantic_parsing",
        metadata={
            "choices": ['semantic_parsing', 'mathqa']
        }
    )
    no_instruct_loss: bool = field(
        default=False,
        metadata={"help": "Whether to use instruction loss or not."},
    )


@dataclass
class PeftArgs:
    """
    Lora arguments
    """
    use_lora: Optional[bool] = field(default=False)
    lora_rank: Optional[int] = field(
        default=8,
        metadata={
            "help": (
                "lora rank"
            )
        },
    )
    lora_alpha: Optional[int] = field(
        default=16,
        metadata={
            "help": (
                "lora alpha"
            )
        },
    )